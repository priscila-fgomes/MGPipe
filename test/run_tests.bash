#!/bin/bash

CONDA_BASE=$(conda info --base)
source $CONDA_BASE/etc/profile.d/conda.sh

# Activate MGPipe environment
conda activate MGPipe 


### algo aqui pra checar se os programas foram instalados...


echo "Testing Quality control"


#Run myproject for Quality control, with multiqc report
../mgpipe.py --project myproject \
             --mode quality-control \
             --reads-folder mg_reads \
             --reads-out results \
             --multiqc
echo "Done"

echo "Testing Trimming"


#Run myproject for Trimming
../mgpipe.py --project myproject \
             --mode trim \
             --length 140 \
             --quality 20 \
             --read-mode paired-end \
             --reads-folder mg_reads \
             --reads-out results \
             --multiqc

echo "Done"



echo "Bowtie --------------"
echo "Testing aligment of single-end reads"
# Run myproject for alignment of single-end reads
../mgpipe.py --project myproject \
             --mode alignment \
             --forward-read mg_reads/Hum5000GE_R1.fastq \
             --read-mode single-end \
             --alignment-mode end-to-end \
             --alignment single.sam

echo "Done"

echo "Testing alignment of paired-end reads"

# Run myproject for alignment of paired-end reads
../mgpipe.py --project myproject \
             --mode alignment \
             --forward-read mg_reads/Hum5000GE_R1.fastq \
             --reverse-read mg_reads/Hum5000GE_R2.fastq \
             --read-mode paired-end \
             --alignment-mode end-to-end \
             --alignment paired.sam

echo "Done"


echo "Testing aligment of single-end reads"
# Run myproject for alignment of single-end reads
../mgpipe.py --project myproject \
             --mode alignment \
             --forward-read mg_reads/Hum5000GE_R1.fastq \
             --read-mode single-end \
             --alignment-mode local \
             --alignment single_local.sam

echo "Done"

echo "Testing alignment of paired-end reads"

# Run myproject for alignment of paired-end reads
../mgpipe.py --project myproject \
             --mode alignment \
             --forward-read mg_reads/Hum5000GE_R1.fastq \
             --reverse-read mg_reads/Hum5000GE_R2.fastq \
             --read-mode paired-end \
             --alignment-mode local \
             --alignment paired_local.sam
echo "Done"


echo "Analyzing with Samtools"

# Run myproject for Samtools.
echo "Testing Samtools"
../mgpipe.py --project myproject --mode analyzes --depth --stats --sam myproject/paired.sam 


echo "Done"


# Test summary

report() {

analysis=$1
file=$2

if [ -f ${file} ] ; then 

    echo -e "\e[32m[ Done ]\e[39m ${analysis}"

else

    echo -e "\e[32m[ Fail ]\e[39m ${analysis}"

fi

}


# Run report for each Test ( Test name + Expected output file )
report 'Single alignment' 'myproject/single.sam'
report 'Paired alignment' 'myproject/paired.sam'

echo "Done myprojecting MGPipe"


#Run myproject for Analyzes


#Open reports

