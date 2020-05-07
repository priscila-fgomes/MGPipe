# 
import os

#
from src.colors import bcolors
from src.welcome import welcome
from src.get_cmd_line import get_cmd_line

# Menu/Configure modules
from src.menu_run_mode  import *
from src.menu_fastq     import *
from src.menu_trim      import *
from src.menu_alignment import *

# Run modules
from src.run_fastqc      import *
from src.run_bowtie2     import *
from src.run_sam         import *

# summary
from src.write_summary import *


# A warm welcome to the users :) 
welcome() 

# Get command line arguments (if any)
arguments = get_cmd_line()

# Project
if not arguments['project'] :
    arguments.update({'project': str(input(f'{bcolors.BLUE}# Choose a project name:{bcolors.ENDC}\n'))})

# Update alignment 
arguments.update({'alignment': os.path.join(arguments['project'],arguments['alignment'])})

if not os.path.isdir(arguments['project']) :
    os.makedirs(arguments['project'])

if not arguments['run_mode'] :
    arguments.update({'run_mode': menu_run_mode()})

# Quality control mode
if arguments['run_mode'] == 'quality-control' : 
    if not arguments['reads_folder'] :
        arguments['reads_folder'] = menu_fastq()
    
    if not arguments['reads_out_folder'] :
        arguments['reads_out_folder'] = menu_fastq_out(arguments)

    arguments.update({'reads_out_folder': os.path.join(arguments['project'],arguments['reads_out_folder'])})

    run_fastqc(arguments)
    
    arguments['trim'] = menu_trim()  


# Alignment Mode 
if arguments['run_mode'] == 'alignment' : 

#    if [arguments['read_mode'] or arguments['alignment_mode'] or arguments['preset'] or arguments['r1'] :
    print (f'''{bcolors.WARNING}
[Setup] Bowtie2 Alignment{bcolors.ENDC}
    ''')

    if not arguments['read_mode'] :
        arguments['read_mode'] = menu_read_mode()

    if not arguments['alignment_mode'] :
        arguments['alignment_mode'] = menu_alignment_mode()

    if not arguments['preset'] :
        arguments['preset'] = menu_preset()
        if arguments['alignment_mode'] in ['local'] : 
            arguments['preset'] = arguments['preset']+'-local'

    if not arguments['r1'] :
        arguments['r1'] = str(input('Forward read file(s): '))

    if arguments['read_mode'] in ['paired-end'] and not arguments['r2'] :
        arguments['r2'] = str(input('Reverse read file(s) '))   # Required if Paired ends.

    write_summary(arguments)
    
    run_bowtie2(arguments)

    run_sam(arguments)