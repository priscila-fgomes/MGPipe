.. _documenting:

=====================================================================
MGPipe: Automated analysis of metagenomics amplicons sequencing reads
=====================================================================

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


MGPipe is a modular pipeline that allows you QC, trimming, alignment and analyzes of your amplicon reads.

For installation details and error FAQ check INSTALL.rst and ISSUES.rst on docs

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

  # Automatic run:
  mgpipe.py
  [0] - GermPLEX (Auto)
  
  # Full parameter and modules list:  
  mgpipe.py -h

  # To test, go to test folder and run "run_tests.bash"
  cd test/
  ./run_tests.bash

