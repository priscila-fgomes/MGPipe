def menu_sam() :
    import os
    from src.colors import bcolors

    option=str(input(f'''{bcolors.BLUE}Alignment file (.sam):{bcolors.ENDC} '''))

    if option.lower() in ['q'] :
        print('Quit. See you latter')
        quit()
    else :
        if not os.path.isdir(option) :
            print(f'''{bcolors.WARNING}[Warning] {option} folder not found {bcolors.ENDC} \n''')
            menu_sam()
    return option