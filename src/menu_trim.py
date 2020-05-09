def menu_trim(arguments):
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
