# menu_run_mode
def menu_run_mode() :
    from src.colors import bcolors

    print(f'''{bcolors.BLUE}
Choose run mode:{bcolors.ENDC}
[1] - Quality Control (QC)
[2] - Trim
[3] - Alignment (AL)
[q] - Quit
''')
    option=str(input(f'{bcolors.BOLD}Option: {bcolors.ENDC}'))

    if option == '1' :
        return 'quality-control'

    elif option == '2' :
        return 'trim'
        
    elif option == '3' :
        return 'alignment'
    
    elif option.lower() in ['q'] :
        print('Quit. See you latter')
        quit()
    else :
        print('Invalid option')
        menu_run_mode()