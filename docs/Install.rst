# Quick Install for the impacient
conda create -n MGPipe python=3.7
conda activate MGPipe
conda install -c bioconda samtools bowtie2 fastqc trim-galore 
conda install pandas seaborn 


# Installation instructions
```bash  
# Create an dedicated environment using a python version that works with all modules.
conda create -n MGPipe python=3.7

# Activate the MGPipe environment
conda activate MGPipe

# Bowtie2 is bla bla bla. Install with:
conda install -c bioconda bowtie2

# Samtools is bla bla bla. Install with:
conda install -c bioconda samtools

# Fastqc processes bla bla bla
conda install -c bioconda fastqc

# Trim-Galore 
conda install -c bioconda trim-galore

# Multiqc 
#conda install -c bioconda multiqc
pip install multiqc

# Addtional DataScience and plotting tools
conda install pandas 
conda install seaborn
```