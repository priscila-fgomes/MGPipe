def run_trim(arguments) :
    import os
    import glob
    import subprocess   
    from time import time
    from src.colors import bcolors

    # List all files from reads_folder
    fastq_files=glob.glob(arguments['reads_folder']+'/*.fastq')

    cmd=['trim_galore']
    cmd.extend(['-j','4',
                '--quality',str(arguments['quality']),
                '--fastqc',
                '--length',str(arguments['length']),
                '-o',arguments['project']])
    
    if arguments['read_mode'] == 'paired-end' :
        cmd.extend(['--paired'])

    if arguments['adapter'] :
        cmd.extend(['--adapter',arguments['adapter']])

    for fastq in fastq_files :
        cmd.append(fastq)

#    if not os.path.isdir(arguments['reads_out_folder']) :
#        os.makedirs(arguments['reads_out_folder'])

    print(f'''{bcolors.BLUE}[ Running ]{bcolors.ENDC} Trim_galore for {len(fastq_files)} reads found in {arguments['project']}''',end='\n')

    if arguments['verbose'] : 
        print(f'''{bcolors.BLUE}[ Verbose ]{bcolors.ENDC} Command line\n{' '.join(map(str,cmd))}''')


    start_time = time()
  
    with open(os.path.join(arguments['project'],"trim_galore.log"), "wb") as file:
        subprocess.run(cmd, stdout=file,stderr=subprocess.DEVNULL)

    end_time = time()
    elapsed_time = end_time - start_time
    
    #print(f'''{bcolors.GREEN}[  Done   ]{bcolors.ENDC} in {elapsed_time/60:5.2f} minutes\n''')
    print(f'''{bcolors.GREEN}[ Done ]{bcolors.ENDC} ''')
