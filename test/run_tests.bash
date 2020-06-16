#!/bin/bash

clear
# Declare an associative array (so I can use "status)
declare -A status

# Config
###########################################################
CONDA_BASE=$(conda info --base)
source $CONDA_BASE/etc/profile.d/conda.sh


# Functions
###########################################################
verify_install() {
echo -ne "\e[95m[ MGPipe ]\e[0m Verifying installation. Please Wait... "

# List of programs this script checks
required_programs='bowtie2 samtools fastqc multiqc trim-galore plotly plotly-orca pandas seaborn psutil' 

if [ "$(conda env list |grep MGPipe)" == "" ] ; then
    echo -e '[Error] MGPipe environment not found \nplease review docs/Install.rst instructions'
    exit 1
fi

# Activate MGPipe environment
conda activate MGPipe

# Get conda package list
#echo "Getting Conda package list. Please wait"
conda_list=$(conda list |awk '{print $1}')

for program in ${required_programs} ; do

    if [[ ${conda_list} == *${program}* ]] ; then
        status[${program}]='\e[32mINSTALLED\e[39m'
    else
        status[${program}]='\e[31mNOT INSTALLED\e[39m'
    fi

done
echo -e '\e[32m[ DONE ]\e[39m'
}

report() {

analysis=$1
file=$2

if [ -f ${file} ] ; then 
    echo -e "\e[32m[ Done ]\e[39m ${analysis}"
else
    echo -e "\e[31m[ Fail ]\e[39m ${analysis}"
fi
}


run_tests() {
# Activate MGPipe environment
conda activate MGPipe 

echo "[ Testing ] FastQC - Quality control"

#Run myproject for Quality control, with multiqc report
mgpipe.py --project myproject \
          --mode quality-control \
          --reads-folder example_reads 


echo "[ Testing ] Trim Galore - Trimming"
mgpipe.py --project myproject \
          --mode trim \
          --length 100 \ 
          --quality 20 \
          --read-mode paired-end \
          --reads-folder example_reads 


echo "[ Testing ] Bowtie2 - Aligment of single-end reads, end-to-end"
mgpipe.py --project myproject \
          --mode alignment \
          --forward-read example_reads/Hum5000GE_R1.fastq \
          --read-mode single-end \
          --alignment-mode end-to-end \
          --alignment single.sam


echo "[ Testing ] Bowtie2 - Aligment of paired-end reads, end-to-end"
mgpipe.py --project myproject \
          --mode alignment \
          --forward-read example_reads/Hum5000GE_R1.fastq \
          --reverse-read example_reads/Hum5000GE_R2.fastq \
          --read-mode paired-end \
          --alignment-mode end-to-end \
          --alignment paired.sam

echo "[ Testing ] Bowtie2 - Aligment of single-end reads, local"
mgpipe.py --project myproject \
          --mode alignment \
          --forward-read example_reads/Hum5000GE_R1.fastq \
          --read-mode single-end \
          --alignment-mode local \
          --alignment single_local.sam


echo "[ Testing ] Bowtie2 - Aligment of paired-end reads, local"
mgpipe.py --project myproject \
          --mode alignment \
          --forward-read example_reads/Hum5000GE_R1.fastq \
          --reverse-read example_reads/Hum5000GE_R2.fastq \
          --read-mode paired-end \
          --alignment-mode local \
          --alignment paired_local.sam

echo "[ Testing ] Samtools - Alignment analyzes"
mgpipe.py --project myproject \
          --mode analyzes \
          --sam myproject/paired.sam \
          --depth --stats

echo "[ Testing ] MultiQC"
mgpipe.py --project myproject \
          --mode report

echo "[ DONE ] Testing"

}

run_report() {
echo -e "
##############################################
#          MGPipe - Test Summary             #
##############################################

Install summary
-------------------------------------------------
     bowtie2 : ${status['bowtie2']}
    samtools : ${status['samtools']}
      fastqc : ${status['fastqc']} 
     multiqc : ${status['multiqc']}
 trim_galore : ${status['trim-galore']}
      plotly : ${status['plotly']}
 plotly-orca : ${status['plotly-orca']}
      pandas : ${status['pandas']}
     seaborn : ${status['seaborn']}
      psutil : ${status['psutil']}

Test results
-------------------------------------------------"
report 'Quality control'             'myproject/Hum5000GE_R1_fastqc.html'
report 'Trimming'                    'myproject/Hum5000GE_R2_val_2.fq'
report 'Single alignment end-to-end' 'myproject/single.sam'
report 'Paired alignment end-to-end' 'myproject/paired.sam'
report 'Single alignment local'      'myproject/single_local.sam'
report 'Paired alignment local'      'myproject/paired_local.sam'
report 'Analysis'                    'myproject/report.html'
report 'MultiQC'                     'myproject/multiqc_report.html'

echo -e "\e[32m[ DONE ]\e[0m Testing MGPipe "

}


# Program
verify_install
run_tests
run_report
