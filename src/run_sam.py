def run_sam(arguments): 
    import os
    import subprocess   
    from time import time
    from src.colors import bcolors


    start_time = time()
    print(f'''[ Running ] Samtools''',end=' ')

    bam = arguments['alignment'].split('.sam')[0]+'.bam'
    cmd=['samtools','view','-bS',arguments['alignment'],'-o',bam]
    subprocess.call(cmd)

    bam_sorted=arguments['alignment'].split('.sam')[0]+'_sorted.bam'   
    cmd=['samtools','sort',bam,'-o',bam_sorted]
    subprocess.call(cmd)

    cmd=['samtools','index',bam_sorted]
    subprocess.call(cmd)

    cmd=['samtools','flagstat',bam_sorted]
    with open(os.path.join(arguments['project'],"alignment.log"), "w") as file:
        subprocess.run(cmd, stdout=file)

    if arguments['depth'] :    
        cmd=['samtools','depth', bam_sorted]
        with open(os.path.join(arguments['project'],"depth.tsv"), "w") as file:
            subprocess.run(cmd, stdout=file)

    cmd=['samtools','idxstats', bam_sorted]
    with open(os.path.join(arguments['project'],"report.tsv"), "w") as file:
        subprocess.run(cmd, stdout=file)

    end_time = time()
    elapsed_time = end_time - start_time
    
#    print(f'''{bcolors.GREEN}[  Done   ]{bcolors.ENDC} in {elapsed_time/60:5.2f} minutes\n''')
    print(f'''{bcolors.GREEN}[ Done ]{bcolors.ENDC}\n''')
