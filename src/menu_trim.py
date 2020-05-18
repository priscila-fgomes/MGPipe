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



 # Trim_galore
    trim_galore = parser.add_argument_group('Trimming','Specific arguments for Trimming')
    
    trim_galore.add_argument('--adapter',
                        action   = 'store',
                        dest     = 'adapter',
                        metavar  = '',
                        help     = 'remove adapter sequence (eg. "AAAAA")')
    
    trim_galore.add_argument('--length',
                        action   = 'store',
                        dest     = 'length',
                        metavar  = '',
                        help     = 'trim at fix sequence lenght.')

    trim_galore.add_argument('--quality',
                        action   = 'store',
                        dest     = 'quality',
                        metavar  = '',
                        help     = 'trim by quality cutoff (eg. 20)')
