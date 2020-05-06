# Quick Install for the impacient
conda create -n mgpipe
conda activate mgpipe 
conda install -c bioconda samtools bowtie2 fastqc trimmomatic multiqc pandas seaborn 


# Installation instructions
```bash  
# Create an dedicated environment
conda create -n mgpipe

# Activate the mgpipe environment
conda activate mgpipe

# Bowtie2 is bla bla bla. Install with:
conda install -c bioconda bowtie2

# Samtools is bla bla bla. Install with:
conda install -c bioconda samtools

# Fastqc processes bla bla bla
conda install -c bioconda fastqc

# Trimmomatic bla bla bla
conda install -c bioconda trimmomatic 

# Multiqc is a reporting tool bla bla bla.
conda install -c bioconda multiqc

# Addtional DataScience and plotting tools
conda install pandas
conda install seaborn
```