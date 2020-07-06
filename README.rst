.. _documenting:

=====================================================================
MGPipe: Automated analysis of metagenomics amplicons sequencing reads
=====================================================================

MGPipe was developped to analyze sequencing reads from human or environmental samples and detect pathogenic bacteria of clinical and forense interest. In the GermPLEX (auto) mode, the pipeline will automatically align and analyse the sequencing reads according to our reference database: Germplex DB. Our modular pipeline also allows you to customize the alignment options, reference database and quality control or trim your sequencing reads before alignment.

Supervision:
------------
@ Universidade Federal do Rio de Janeiro - UFRJ

* Rosane Silva - silvaros@biof.ufrj.br  

Development lead
----------------
* Priscila da Silva Figueiredo Celestino Gomes - pfigueiredo@biof.ufrj.br

Contributors:
-------------
* Diego Enry Barreto Gomes - dgomes@pq.cnpq.br
* Victor Hugo Giordano Dias - victorhdias@biof.ufrj.br 



Installation:
-------------

.. code-block:: bash 

  # Install Miniconda from:
  https://docs.conda.io/en/latest/miniconda.html
 
  # Download MGPipe repository
  git clone https://github.com/priscila-fgomes/MGPipe.git 
  
  # Go to the program folder
  cd MGPipe

  # Install using the autoinstall script :)
  ./autoinstall

  # Make sure you always activate MGPipe environment before running !
  conda activate MGPipe
  
  #Please add MGPipe to your $PATH. Add these lines to your .bashrc or .bash_profile
  export MGPipe=${PWD}
  export PATH=\$PATH:\${MGPipe}

  # Automatic run, choose option 0. This mode compairs your reads to our GermPLEX Database
  mgpipe.py
  [0] - GermPLEX (Auto)
  
  # Full parameter and modules list:  
  mgpipe.py -h

  # To test, go to test folder and run "run_tests.bash"
  cd test/
  ./run_tests.bash

For other details and error FAQ check INSTALL.rst and ISSUES.rst on docs
