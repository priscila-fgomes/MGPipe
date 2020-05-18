#!/bin/bash

# Activate MGPipe environment
conda activate MGPipe

#Run test for Quality control



#Run test for Trimming



# Run test for alignment of single-end reads
echo "Testing BLA"
python ../mgpipe.py \
--project test \
--forward_read mg_reads/Hum5000GE_R1.fastq \
--read_mode single-end \
--alignment_mode end-to-end \
--alignment single.sam


if [ ! -f test/single.sam ] ; 
    echo "Alignment failed"
    exit 1

echo "Done testing MGPipe"


#Run test for alignment of paired-end reads

python mgpipe.py \
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

