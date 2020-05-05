#!/usr/bin/env python
# coding: utf-8


# Config


# Imports -------------------------------------------------
import os
import sys
import gzip
import subprocess
import argparse

# Main Function
def main() :

    # Get command line
    arguments = get_cmd_line()
    
    write_summary(arguments['project'],
                  arguments['read_mode'],
                  arguments['r1'],
                  arguments['r2'],
                  arguments['alignment_mode'],
                  arguments['preset_option'],
                  arguments['alignment'],
                  arguments['nt'])

    make_folders(arguments['project'])

    run_bowtie2(arguments['project'],
                arguments['read_mode'],
                arguments['r1'],
                arguments['r2'],
                arguments['alignment_mode'],
                arguments['preset_option'],
                arguments['alignment'],
                arguments['nt'],
                arguments['overwrite'])

    run_sam(arguments['alignment'],arguments['depth'])

# Classes
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Functions 
def write_done(module,routine) :
    print(f"\033[1;32;40m [ DONE ] \033[0;37;40m {module} - {routine} ")

def run_sam(alignment,depth): 

    bam=alignment.split('.sam')[0]+'.bam'
    cmd=['samtools','view','-bS',alignment,'-o',bam]
    subprocess.call(cmd)   
    write_done('Samtools','view')

    bam_sorted=alignment.split('.sam')[0]+'_sorted.bam'   
    cmd=['samtools','sort',bam,'-o',bam_sorted]
    subprocess.call(cmd)
    write_done('Samtools','sort')

    cmd=['samtools','index',bam_sorted]
    subprocess.call(cmd)
    write_done('Samtools','index')

    cmd=['samtools','flagstat',bam_sorted]
    with open("alignment.log", "w") as file:
        subprocess.run(cmd, stdout=file)
    write_done('Samtools','flagstat')

    cmd=['samtools','idxstats', bam_sorted]
    with open("report.tsv", "w") as file:
        subprocess.run(cmd, stdout=file)
    write_done('Samtools','idxstats')

    if depth :    
        cmd=['samtools','depth', bam_sorted]
        with open("depth.tsv", "w") as file:
            subprocess.run(cmd, stdout=file)
        write_done('Samtools','Depth')


def run_bowtie2(project,read_mode,r1,r2,alignment_mode,preset_option,alignment,nt,overwrite) :

    if os.path.isfile(alignment) and not overwrite :
        write_done('Bowtie2','Alignment')
        return
    
    index_db=os.path.join(os.path.dirname(sys.argv[0]),'Index','DB')
    
    if read_mode in 'single-end' :
        cmd=['bowtie2',
            '-x',index_db,
            '-U',r1,
            '-q','--no-unal',
            '--'+alignment_mode,
            '--'+preset_option,
            '-S',alignment,
            '-p',str(nt)]
    else :
        cmd=['bowtie2',
            '-x',index_db,
            '-1',r1,
            '-2',r2,
            '-q','--no-unal',
            '--'+alignment_mode,
            '--'+preset_option,
            '-S',alignment,
            '-p',str(nt)]
      
    try :    
        subprocess.run(cmd,stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    except :
        print(f"ERROR: Bowtie2 failed to run.")

    if not os.path.isfile(alignment) :
        print('ERROR: Bowtie2 failed. {alignment} not created|')
        quit() 

    return  write_done('Bowtie','Alignment')



def write_summary(project,read_mode,r1,r2,alignment_mode,preset_option,alignment,nt) :
    print(f'''
###################################
# MG Pipe - Metagenimics Pipeline #
###################################

          Project : {project}

       Input Mode : {read_mode}
Forward Read (R1) : {r1}
Reverse Read (R2) : {r2}

   Alignment Mode : {alignment_mode}
    Preset Option : {preset_option}

 Alignment Output : {alignment}
      CPU Threads : {nt}

    ''')

def make_folders(project) :
    '''
    Creates "reports" and "alignment" folders at project folder
    '''
    try :
        os.makedirs(os.path.join(project,'reports'))
    except :
        pass

    try :
        os.makedirs(os.path.join(project,'alignments'))
    except :
        pass
    


def get_cmd_line():
    '''
    Get the command line
    '''
    parser = argparse.ArgumentParser(description = 'MG-Pipe - Metagenomics Pipeline.')
    
    # General arguments
    parser.add_argument('-p','--project',
                        action   = 'store',
                        dest     = 'project',
                        required = True,
                        help     = 'Project folder.')

    parser.add_argument('-O','--overwrite',
                        action   = 'store_true',
                        dest     = 'overwrite',
                        required = False,
                        default  = False,
                        help     = 'Overwrite outputs')
    

    # Bowtie specific arguments
    parser.add_argument('-rm','--read_mode',
                        action   = 'store',
                        dest     = 'read_mode',
                        required = False,
                        default  = 'single-end',
                        choices  = ('single-end','paired-end'),
                        help     = 'Read mode')

    parser.add_argument('-r1','--forward_read',
                        action   = 'store',
                        dest     = 'r1',
                        required = True,
                        help     = 'Forward read file (.fastq, fastq.gz, \
                                    comma-separated list of files')

    # Required if -pe is set
    parser.add_argument('-r2','--reverse_read',
                        action   = 'store',
                        dest     = 'r2',
                        required = False,
                        help     = 'Forward read file (.fastq, fastq.gz, \
                                    comma-separated list of files')
    
    # Bowtie Alignment modes ( Must be one or other )
    parser.add_argument('-a','--alignment_mode',
                        action   = 'store',
                        dest     = 'alignment_mode',
                        required = False,
                        default  = 'end-to-end',
                        choices  = ('end-to-end','local'),
                        help     = 'Alignment Mode [Default "end-to-end"]')


    parser.add_argument('--preset',
                        action   = 'store',
                        dest     = 'preset_option',
                        required = False,
                        default  = 'sensitive',
                        choices  = ('sensitive','very-sensitive','fast','very-fast'),
                        help     = 'Preset Options [Default "sensitive"]')


    # Bowtie output options
    parser.add_argument('--alignment',
                        action   = 'store',
                        dest     = 'alignment',
                        required = False,
                        default  = 'alignment.sam',
                        help     = 'Output name for alignment')

    parser.add_argument('-nt',
                        action   = 'store',
                        dest     = 'nt',
                        required = False,
                        default  = 8,
                        help     = 'Number of CPU threads')


    # Samtools options
    parser.add_argument('--depth',
                        action   = 'store_true',
                        dest     = 'depth',
                        required = False,
                        default  = False,
                        help     = 'Write Samtools depth')

    

    arg_dict = vars(parser.parse_args())

    # Update arguments
    if arg_dict['alignment_mode'] == 'local' :
            arg_dict.update({'preset_option': arg_dict['preset_option']+'-local'})


    return arg_dict


if __name__ == "__main__":
    main()
