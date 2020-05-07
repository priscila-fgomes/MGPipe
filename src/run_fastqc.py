def run_fastqc(arguments) :
    import os
    import glob
    import subprocess   
    from time import time

    # List all files from reads_folder
    fastq_files=glob.glob(arguments['reads_folder']+'/*.fastq')
    
    # list to string
    #fastq_files=' '.join(map(str,fastq_files))
    cmd=['fastqc']
    for fastq in fastq_files :
        cmd.append(fastq)
    cmd.extend(['-o',arguments['reads_out_folder'],'-t',arguments['nt']])
    
    if not os.path.isdir(arguments['reads_out_folder']) :
        os.makedirs(arguments['reads_out_folder'])

    print(f'''
[Running] FastQC for {len(fastq_files)} reads found in {arguments['reads_folder']}
          Using {arguments['nt']} CPU threads, Please Wait.''')


    start_time = time()

    with open(os.path.join(arguments['reads_out_folder'],"fastqc.log"), "wb") as file:
        subprocess.run(cmd, stdout=file,stderr=subprocess.DEVNULL)

    end_time = time()
    elapsed_time = end_time - start_time
    
    print(f'''{bcolors.GREEN}[  Done   ]{bcolors.ENDC} in {elapsed_time/60:5.2f} minutes\n''')
