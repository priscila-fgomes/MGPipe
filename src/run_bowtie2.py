def run_bowtie2(arguments) :
    import os
    import sys
    import subprocess   
    from time import time
    from src.colors import bcolors

    if os.path.isfile(arguments['alignment']) and not arguments['overwrite'] :
        print(f'''
{bcolors.WARNING}[ Warning ] Bowtie2 results found.{bcolors.ENDC} {bcolors.GREEN}\t[ Done ]{bcolors.ENDC}''')
        return

    # Use the index provided by MG-Pipe's GitHub
    index_db=os.path.join(os.path.dirname(sys.argv[0]),'Index','DB')

    cmd=['bowtie2',
        '-x',index_db,
        '-q','--no-unal',
        '--'+arguments['alignment_mode'],
        '--'+arguments['preset'],
        '-S',arguments['alignment'],
        '-p',arguments['nt']]

    if arguments['read_mode'] in 'single-end' :
        cmd.append('-U')
        cmd.append(arguments['r1'])

    else :
        cmd.append('-1')
        cmd.append(arguments['r1'])
        cmd.append('-2')
        cmd.append(arguments['r2'])

    print(f'''[ Running ] Bowtie2''',end='  ')
    
    start_time = time()

    with open(os.path.join(arguments['project'],"bowtie2.log"), "wb") as file:
        subprocess.run(cmd, stdout=subprocess.DEVNULL,stderr=file)

    end_time = time()
    elapsed_time = end_time - start_time

#    print(f'''{bcolors.GREEN}[  Done   ]{bcolors.ENDC} in {elapsed_time/60:5.2f} minutes\n''')
    print(f'''{bcolors.GREEN}\t\t\t[ Done ]{bcolors.ENDC} \n''')

#    try :    
#        subprocess.run(cmd,stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
#    except :
#        print(f"ERROR: Bowtie2 failed to run.")

    if not os.path.isfile(arguments['alignment']) :
        print('ERROR: Bowtie2 failed. {alignment} not created|')
        quit() 

    if arguments['verbose'] :
        print(f'''{bcolors.BLUE}[ Verbose ]{bcolors.ENDC} Command line\n{' '.join(map(str,cmd))}''')

    return  
