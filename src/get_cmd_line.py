def get_cmd_line():
    '''
    Get the command line
    '''
    import argparse
    import os
    parser = argparse.ArgumentParser(description = 'MG-Pipe - Metagenomics Pipeline.')
    
    # General arguments
    general = parser.add_argument_group('General','General arguments')

    # General arguments
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
                        choices  = ['auto','quality-control','trim','alignment','analyzes','report'],
                        help     = 'Run mode [quality-control, trim, alignment, analyzes, report]')

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

    # Bowtie/Trim specific arguments
    bowtie_trim = parser.add_argument_group('Read Mode for alignments','Bowtie or Trim_galore')
    bowtie_trim.add_argument('-rm','--read-mode',
                        action   = 'store',
                        dest     = 'read_mode',
                        choices  = ('single-end','paired-end'),
                        metavar  = '',
                        help     = 'Read mode [single-end or paired-end]')

# Fastqc
    fastqc = parser.add_argument_group('Quality Control','Specific arguments for FastQC')
    
    fastqc.add_argument('--reads-folder',
                        action   = 'store',
                        dest     = 'reads_folder',
                        metavar  = '',
                        help     = 'Folder containing FastQC files.')

    fastqc.add_argument('--reads-out',
                        action   = 'store',
                        dest     = 'reads_out_folder',
                        metavar  = '',
                        help     = 'Folder containing FastQC output files.')

 # Trim_galore
    trim_galore = parser.add_argument_group('Trimming','Specific arguments for Trimming')
    
    trim_galore.add_argument('--adapter',
                        action   = 'store',
                        dest     = 'adapter',
                        metavar  = '',
                        help     = 'Remove adapter sequence (eg. "AAAAA")')
    
    trim_galore.add_argument('--length',
                        action   = 'store',
                        dest     = 'length',
                        default  = 20,
                        metavar  = '',
                        help     = 'Discard reads that became shorter than length INT because of either quality or adapter trimming.')

    trim_galore.add_argument('--quality',
                        action   = 'store',
                        dest     = 'quality',
                        default  = 20,
                        metavar  = '',
                        help     = 'Trim by quality cutoff (eg. 20)')


    # Bowtie Alignment modes ( Must be one or other )
    bowtie = parser.add_argument_group('Alignment','Specific arguments for Bowtie2')


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
                        default  = 'sensitive',
                        metavar  = '',
                        help     = 'Preset Options: [sensitive], very-sensitive, fast, very-fast')

    # Bowtie output options
    bowtie.add_argument('--alignment',
                        action   = 'store',
                        dest     = 'alignment',
                        default  = 'alignment.sam',
                        metavar  = '',
                        help     = 'Output name for alignment')


# Samtools options
    samtools = parser.add_argument_group('Samtools arguments')

    samtools.add_argument('--sam',
                        action   = 'store',
                        dest     = 'sam',
                        metavar  = '',
                        help     = 'Alignment file (.sam)')

    samtools.add_argument('--depth',
                        action   = 'store_true',
                        dest     = 'depth',
                        help     = 'Write alignment depth')

    samtools.add_argument('--stats',
                        action   = 'store_true',
                        dest     = 'stats',
                        help     = 'Write alignment log')

#    samtools.add_argument('--report',
#                        action   = 'store_true',
#                        dest     = 'report',
#                        help     = 'Write alignment report')
    samtools.add_argument('--cutofft',
                        action   = 'store',
                        dest     = 'sam_report_cutoff',
                        type     = float,
                        default  = 1.0,
                        metavar  = '',
                        help     = 'Percentage of Mapped reads cutoff [1]')

# Multiqc options
    multiqc = parser.add_argument_group('Multiqc Report')
    
    multiqc.add_argument('--multiqc',
                        action   = 'store_true',
                        dest     = 'multiqc',
                        help     = 'Enable MultiQC report')
   

    arg_dict = vars(parser.parse_args())

    return arg_dict

