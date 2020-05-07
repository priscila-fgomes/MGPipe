def menu_read_mode() :
    from src.colors import bcolors

    print(f'''{bcolors.BLUE}Choose a read mode:{bcolors.ENDC}
[1] - Single-end
[2] - Paired-end
[q] - Quit
''')
    option=str(input(f'{bcolors.BOLD}Read mode: {bcolors.ENDC}'))

    if option == '1' :
        return 'single-end'
        
    elif option == '2' :
        return 'paired-end'
    
    elif option.lower() in ['q'] :
        print('Quit. See you latter')
        quit()
    else :
        print('Invalid option')
        menu_read_mode()

def menu_alignment_mode () :
    from src.colors import bcolors

    print(f'''{bcolors.BLUE}Choose an alignment mode:{bcolors.ENDC}
[1] - End-to-end (Default)
[2] - Local
[q] - Quit
''')
    option=str(input(f'{bcolors.BOLD}Alignment mode: {bcolors.ENDC}'))

    if option == '1' :
        return 'end-to-end'
    if option == '' :
        print('Using Default (end-to-end)')
        return 'end-to-end'
        
    elif option == '2' :
        return 'local'
    
    elif option.lower() in ['q'] :
        print('Quit. See you latter')
        quit()
    else :
        print('Invalid option')
        menu_alignment_mode()

def menu_preset () :
    from src.colors import bcolors

    print(f'''{bcolors.BLUE}Choose an preset mode:{bcolors.ENDC}
[1] - sensitive
[2] - very-sensitive
[3] - fast
[4] - very-fast
[q] - Quit
''')
    option=str(input(f'{bcolors.BOLD}Preset: {bcolors.ENDC}'))

    if option == '1' :
        return 'sensitive'
        
    elif option == '2' :
        return 'very-sensitive'

    elif option == '3' :
        return 'fast'

    elif option == '4' :
        return 'very-fast'

    elif option.lower() in ['q'] :
        print('Quit. See you latter')
        quit()
    else :
        print('Invalid option')
        menu_preset()