def set_bowtie2(arguments) : 
    import os
    from src.menu_alignment import menu_read_mode,menu_alignment_mode,menu_preset
    from src.colors import bcolors

    # Update alignment path
    arguments.update({'alignment': os.path.join(arguments['project'],arguments['alignment'])})

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
    
    return arguments


def run_bowtie2(arguments) :
    import os
    import sys
    import subprocess   
    from time import time
    from src.colors import bcolors

    # Write summary
    if arguments['run_mode'] != 'auto':
        summary_bowtie2(arguments)

    if os.path.isfile(arguments['alignment']) and not arguments['overwrite'] :
        print(f'''
{bcolors.WARNING}[ Warning ]{bcolors.ENDC} Results found, skipping alignment  {bcolors.GREEN}\t[ Done ]{bcolors.ENDC}''')
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

    
    start_time = time()
    print(f'''{bcolors.BLUE}[ Running ]{bcolors.ENDC} Alignment (Bowtie2)''',end='')

    with open(os.path.join(arguments['project'],"log","bowtie2.log"), "wb") as file:
        subprocess.run(cmd, stdout=subprocess.DEVNULL,stderr=file)

    end_time = time()
    elapsed_time = end_time - start_time

#    print(f'''{bcolors.GREEN}[  Done   ]{bcolors.ENDC} in {elapsed_time/60:5.2f} minutes\n''')
    print(f'''{bcolors.GREEN}\t\t\t[ Done ]{bcolors.ENDC}''')

    if not os.path.isfile(arguments['alignment']) :
        print('\nERROR: Bowtie2 failed. {alignment} not created|')
        quit() 

    if arguments['verbose'] :
        print(f'''{bcolors.BLUE}[ Verbose ]{bcolors.ENDC} Command line\n{' '.join(map(str,cmd))}''')

    return  

def summary_bowtie2(arguments) :
    print(f'''
        ####################
        # Bowtie2  Summary #
        ####################

          Project : {arguments['project']}
         Run Mode : {arguments['run_mode']}

        Read Mode : {arguments['read_mode']}
Forward Read (R1) : {arguments['r1']}
Reverse Read (R2) : {arguments['r2']}

   Alignment Mode : {arguments['alignment_mode']}
    Preset Option : {arguments['preset']}

 Alignment Output : {arguments['alignment']}
      CPU Threads : {arguments['nt']}

    ''')