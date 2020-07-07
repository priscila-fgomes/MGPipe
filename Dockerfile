#Download base image ubuntu 18.04
FROM continuumio/miniconda3:latest

MAINTAINER Priscila SFC Gomes <pfigueiredo@biof.ufrj.br>
LABEL version="1.0"
LABEL description="MGPipe Dockerfile."

#---------------------------------------------
# Update Ubuntu Software repository
# and install all required software
#---------------------------------------------
RUN apt-get -y update
RUN apt-get -y install git wget
RUN apt-get -y autoremove

#---------------------------------------------
# Preparing directories 
#---------------------------------------------
WORKDIR /home/

#---------------------------------------------
# Install miniconda
#--------------------------------------------
#RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh 
#RUN bash Miniconda3-latest-Linux-x86_64.sh -b -p /home/miniconda3
#RUN rm -rf Miniconda3-latest-Linux-x86_64.sh
#RUN eval "$(/home/miniconda3/bin/conda shell.bash hook)"
#RUN conda init
#RUN conda config --set auto_activate_base false

#---------------------------------------------
# Install conda packages for MGPipe
#--------------------------------------------
#RUN conda create -n MGPipe python=3.7 -y
#RUN conda activate MGPipe
RUN conda install -y -c bioconda  samtools bowtie2 fastqc trim-galore
RUN conda install -y pandas seaborn psutil 
RUN conda install -y -c plotly plotly plotly-orca
RUN pip install multiqc


#---------------------------------------------
# Clone MGPipe from GitHub
#--------------------------------------------
WORKDIR /home/
RUN git clone https://github.com/priscila-fgomes/MGPipe.git

RUN mkdir -p /data
RUN chmod 777 -R /data
WORKDIR /data/

ENV PATH "${PATH}:/home/MGPipe/"




