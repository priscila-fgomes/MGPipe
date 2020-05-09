def get_cmd_line():
    '''
    Get the command line
    '''
    import argparse
    import os
    parser = argparse.ArgumentParser(description = 'MG-Pipe - Metagenomics Pipeline.')
    
    # General arguments
    general = parser.add_argument_group('General','General arguments')

    general.add_argument('-p','--project',
                        action   = 'store',
                        dest     = 'project',
                        required = False,
                        metavar  = '',
                        help     = 'Project folder.')

    # General arguments
    general.add_argument('-m','--mode',
                        action   = 'store',
                        dest     = 'run_mode',
                        metavar  = '',
                        choices  = ['quality-control','trim','alignment'],
                        help     = 'Run mode [quality-control, tim or alignment]')

    general.add_argument('-nt','--threads',
                        action   = 'store',
                        dest     = 'nt',
                        metavar  = '',
                        default  = str(os.cpu_count()),
                        help     = 'Number of CPU threads')

    general.add_argument('-v','--verbose',
                        action   = 'store_true',
                        dest     = 'verbose',
                        help     = 'Verbose outputs')
    

    general.add_argument('-O','--overwrite',
                        action   = 'store_true',
                        dest     = 'overwrite',
                        help     = 'Overwrite outputs')
    

    # Bowtie Alignment modes ( Must be one or other )
    bowtie = parser.add_argument_group('Bowtie2','Specific arguments for Bowtie2')

    # Bowtie specific arguments
    bowtie.add_argument('-rm','--read-mode',
                        action   = 'store',
                        dest     = 'read_mode',
                        choices  = ('single-end','paired-end'),
                        metavar  = '',
                        help     = 'Read mode [single-end or paired-end]')

    bowtie.add_argument('-r1','--forward-read',
                        action   = 'store',
                        dest     = 'r1',
                        metavar  = '',
                        help     = 'Forward read file [.fastq, fastq.gz, \
                                    comma-separated list of files]')

    # Required if -pe is set
    bowtie.add_argument('-r2','--reverse-read',
                        action   = 'store',
                        dest     = 'r2',
                        metavar  = '',
                        help     = 'Forward read file [.fastq, fastq.gz, \
                                    comma-separated list of files]')

    bowtie.add_argument('-a','--alignment-mode',
                        action   = 'store',
                        dest     = 'alignment_mode',
                        metavar  = '',
                        choices  = ('end-to-end','local'),
                        help     = 'Alignment Mode [Default "end-to-end"]')


    bowtie.add_argument('-pr','--preset',
                        action   = 'store',
                        dest     = 'preset',
                        choices  = ('sensitive','very-sensitive','fast','very-fast'),
                        metavar  = '',
                        help     = 'Preset Options [Default "sensitive"]')

    # Bowtie output options
    bowtie.add_argument('--alignment',
                        action   = 'store',
                        dest     = 'alignment',
                        default  = 'alignment.sam',
                        help     = 'Output name for alignment')


    # Samtools options
    parser.add_argument('--depth',
                        action   = 'store_true',
                        dest     = 'depth',
                        help     = 'Write Samtools depth')


    # Fastqc
    fastqc = parser.add_argument_group('FastQ','Specific arguments for FastQC')
    
    fastqc.add_argument('--reads_folder',
                        action   = 'store',
                        dest     = 'reads_folder',
                        metavar  = '',
                        help     = 'Folder containing FastQC files.')

    fastqc.add_argument('--reads_out',
                        action   = 'store',
                        dest     = 'reads_out_folder',
                        metavar  = '',
                        help     = 'Folder containing FastQC output files.')

    # Trim_galore
    trim_galore = parser.add_argument_group('Trim','Specific arguments for Trimming')
    
    trim_galore.add_argument('--length',
                        action   = 'store',
                        dest     = 'length',
                        metavar  = '',
                        help     = 'Trim length.')

    trim_galore.add_argument('--adapter',
                        action   = 'store',
                        dest     = 'adapter',
                        metavar  = '',
                        help     = 'Adapter sequence. (eg. "AAAAA")')

    arg_dict = vars(parser.parse_args())

    return arg_dict

