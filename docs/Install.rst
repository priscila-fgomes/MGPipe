.. _documenting:
===============================
Installation instructions
===============================

Quick Install 
--------------------------------

.. code-block:: bash

    conda create -n MGPipe python=3.7
    conda activate MGPipe
    conda install -y -c bioconda samtools bowtie2 fastqc trim-galore pandas seaborn plotly-orca
    pip install multiqc


Detailed install
--------------------------------
.. code-block:: bash

  # Create an dedicated environment using a python version that works with all modules.
  conda create -n MGPipe python=3.7

  # Activate the MGPipe environment
  conda activate MGPipe

  # Bowtie2 is an ultrafast and memory-efficient tool for aligning sequencing reads to long reference sequences. Install with:
  conda install -y -c bioconda bowtie2

  # Samtools is is a suite of programs for interacting with high-throughput sequencing data. Install with:
  conda install -y -c bioconda samtools

  # Fastqc is a quality control tool for high throughput sequence data. Install with:
  conda install -y -c bioconda fastqc

  # Trim-Galore is a wrapper tool around Cutadapt and FastQC to consistently apply quality and adapter trimming to FastQ files. Install with:
  conda install -y -c bioconda trim-galore

  # Multiqc aggregate results from bioinformatics analyses across many samples into a single report. Install with:
  pip install multiqc

  # Addtional DataScience and plotting tools
  conda install -y pandas 
  conda install -y seaborn
  conda install -y plotly-orca

  conda install -c plotly plotly
  conda install -c plotly plotly-orca
