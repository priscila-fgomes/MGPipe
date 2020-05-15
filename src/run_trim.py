def run_trim(arguments) :
    import os
    import glob
    import subprocess   
    from time import time
    from src.colors import bcolors

    arguments['reads_out_folder'] = os.path.join(arguments['project'],arguments['reads_out_folder'])

    # List all files from reads_folder
    fastq_files=glob.glob(arguments['reads_folder']+'/*.fastq')

    cmd=['trim_galore']
    cmd.extend(['-j','4','--quality','20','--fastqc','--length',arguments['length'],'-o',arguments['reads_out_folder']])
    
    if arguments['read_mode'] == 'paired-end' :
        cmd.extend(['--paired'])

    if arguments['adapter'] :
        cmd.extend(['--adapter',arguments['adapter']])

    for fastq in fastq_files :
        cmd.append(fastq)

    if not os.path.isdir(arguments['reads_out_folder']) :
        os.makedirs(arguments['reads_out_folder'])

    print(f'''
[ Running ] Trim_galore for {len(fastq_files)} reads found in {arguments['reads_folder']}''',end='\t')

    if arguments['verbose'] : 
        print(f'''{' '.join(map(str,cmd))}''')

    start_time = time()

    
    with open(os.path.join(arguments['reads_out_folder'],"trim_galore.log"), "wb") as file:
        subprocess.run(cmd, stdout=file,stderr=subprocess.DEVNULL)

    end_time = time()
    elapsed_time = end_time - start_time
    
    #print(f'''{bcolors.GREEN}[  Done   ]{bcolors.ENDC} in {elapsed_time/60:5.2f} minutes\n''')
    print(f'''{bcolors.GREEN}[ Done ]{bcolors.ENDC} ''')



    # MultiQC report ############
    print(f'''
[Running] Generating MultiQC report ...''')


    cmd=['multiqc','-f',arguments['reads_out_folder'],'--outdir',arguments['reads_out_folder']]
    
    start_time = time()
    subprocess.run(cmd, stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    end_time = time()
    elapsed_time = end_time - start_time

    print(f'''{bcolors.GREEN}[  Done   ]{bcolors.ENDC} in {elapsed_time/60:5.2f} minutes\n''')

    print('''open MultiQC report with:

 firefox test/output/multiqc_report.html''')
