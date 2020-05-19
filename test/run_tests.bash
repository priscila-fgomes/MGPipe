#!/bin/bash

CONDA_BASE=$(conda info --base)
source $CONDA_BASE/etc/profile.d/conda.sh

# Activate MGPipe environment
conda activate MGPipe 


### algo aqui pra checar se os programas foram instalados...


echo "Testing Quality control"


#Run test for Quality control, with multiqc report
../mgpipe.py -v \
          --project test \
          --mode quality-control \
          --reads-folder mg_reads \
          --reads-out results \
          --multiqc
echo "Done"

echo "Testing Trimming"


#Run test for Trimming
../mgpipe.py -v \
             --project test \
             --mode trim \
             --length 140 \
             --quality 20 \
             --read-mode paired-end \
             --reads-folder mg_reads \
             --reads-out results \
             --multiqc

echo "Done"

echo "Testing aligment of single-end reads"

# Run test for alignment of single-end reads
../mgpipe.py -v \
             --project test \
             --mode alignment \
             --forward-read mg_reads/Hum5000GE_R1.fastq \
             --read-mode single-end \
             --alignment-mode end-to-end \
             --alignment single.sam

echo "Done"

echo "Testing alignment of paired-end reads"

# Run test for alignment of paired-end reads
../mgpipe.py -v \
             --project test \
             --mode alignment \
             --forward-read mg_reads/Hum5000GE_R1.fastq \
             --reverse-read mg_reads/Hum5000GE_R2.fastq \
             --read-mode paired-end \
             --alignment-mode end-to-end \
             --alignment paired.sam

echo "Done"

echo "Analyzing with Samtools"

# Run test for Samtools.
echo "Testing Samtools"
../mgpipe.py --project test --mode analyzes --depth --stats --sam test/paired.sam 


echo "Done"


if [ ! -f test/single.sam ] ; 
    echo "Alignment failed"
    exit 1

echo "Done testing MGPipe"


#Run test for alignment of paired-end reads

../mgpipe.py \
--project teste \
--forward_read mg_reads/Hum5000GE_R1.fastq  \
--reverse_read mg_reads/Hum5000GE_R2.fastq  \
--read_mode paired-end \
--alignment_mode end-to-end \
--alignment paired.sam

if [ ! -f test/paired.sam ] ;
    echo "Alignment failed"
    exit 1

echo "Done testing MGPipe"


#Run test for Analyzes


#Open reports

