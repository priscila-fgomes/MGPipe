def menu_trim() :

    option=str(input('Trim sequences ? [Y/N]: '))

    if option.lower() == 'y' :
        return True
        
    elif option.lower() == 'n' :
        return False
    
    elif option.lower() in ['q'] :
        print('Quit. See you latter')
        quit()
    else :
        print('Invalid option')
        menu_trim()