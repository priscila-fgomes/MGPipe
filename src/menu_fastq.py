# fastq_workflow
def menu_fastq() :
    import os
    from src.colors import bcolors

    option=str(input(f'''{bcolors.BLUE}Reads input folder:{bcolors.ENDC} '''))

    if option.lower() in ['q'] :
        print('Quit. See you latter')
        quit()
    else :
        if not os.path.isdir(option) :
            print(f'''{bcolors.WARNING}[Warning] {option} folder not found {bcolors.ENDC} \n''')
            menu_fastq()
    return option

# No longer necessary
def menu_fastq_out(arguments) :
    import os
    from src.colors import bcolors

    option=str(input(f'''{bcolors.BLUE}Reads output folder:{bcolors.ENDC} '''))
    
    if option.lower() in ['q'] :
        print('Quit. See you latter')
        quit()
    else :
        mg_out=os.path.join(arguments['project'],option)

        if os.path.isdir(mg_out) and not arguments['overwrite']:
            print(f'''{bcolors.WARNING}[Warning] {mg_out} folder exists {bcolors.ENDC} \n''')
            menu_fastq_out(arguments)

    return option