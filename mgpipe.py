#!/usr/bin/env python3
# coding: utf-8
# Config

import os

#
from src.colors import bcolors
from src.welcome import welcome
from src.get_cmd_line import get_cmd_line

# Menu/Configure modules
from src.menu_run_mode  import *
from src.menu_fastq     import *
from src.menu_trim      import *
from src.menu_sam       import *

# Run modules
from src.run_fastqc      import *
from src.run_trim        import *
from src.run_bowtie2     import *
from src.run_sam         import *
from src.run_multiqc     import *
from src.run_germplex    import *

# A warm welcome to the users :) 
welcome() 

# Get command line arguments (if any)
arguments = get_cmd_line()

# Project
if not arguments['project'] :
    arguments.update({'project': str(input(f'{bcolors.BLUE}# Choose a project name:{bcolors.ENDC}\n'))})

# Create project, raw data and log folders.
if not os.path.isdir(arguments['project']) :
    os.makedirs(arguments['project'])

if not os.path.isdir(os.path.join(arguments['project'],'raw_data')) :
    os.makedirs(os.path.join(arguments['project'],'raw_data'))

if not os.path.isdir(os.path.join(arguments['project'],'log')) :
    os.makedirs(os.path.join(arguments['project'],'log'))

# Sanity check for run_mode
if not arguments['run_mode'] :
    arguments.update({'run_mode': menu_run_mode()})

# GermPLEX mode
if arguments['run_mode'] == 'auto' :
    run_germplex(arguments)
    quit() 

# Quality control mode
if arguments['run_mode'] == 'quality-control' : 
    if not arguments['reads_folder'] :
        arguments['reads_folder'] = menu_fastq()

    run_fastqc(arguments)

# Alignment Mode 
if arguments['run_mode'] == 'alignment' : 
    arguments = set_bowtie2(arguments)
    run_bowtie2(arguments)


if arguments['run_mode'] == 'analyzes' : 
    if not arguments['sam'] :
        arguments['sam'] = menu_sam()

    run_sam(arguments)

    report_sam(arguments)


# Alignment Mode 
if arguments['run_mode'] == 'trim' : 
    run_trim(arguments)


if arguments['multiqc'] or arguments['run_mode'] == 'report':
    run_multiqc(arguments)