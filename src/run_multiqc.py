def run_multiqc(arguments) :
    import os
    import glob
    import subprocess   
    from time import time
    from src.colors import bcolors
    
    start_time = time()
# MultiQC report ############
    print(f'''{bcolors.BLUE}[Running]{bcolors.ENDC} Generating quality report ...''')

    cmd=['multiqc','-f',arguments['reads_out_folder'],'--outdir',arguments['reads_out_folder']]

    subprocess.run(cmd, stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)

    print(f'''
Open quality report with:

firefox ./{arguments['reads_out_folder']}/multiqc_report.html''')

    end_time = time()
    elapsed_time = end_time - start_time

    print(f'''{bcolors.GREEN}[  Done   ]{bcolors.ENDC} in {elapsed_time/60:5.2f} minutes\n''')
