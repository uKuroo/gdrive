import os
from pathlib import Path
import utils.directory_util as directory_util
import config.settings as settings
import utils.parser as parser

LINE = '============================================================='

def print_center(message):
    message_len = len(message)
    line_len = len(LINE)
    diff = (line_len - message_len) // 2

    centered = ''

    for i in range(diff):
        centered += ' '

    print(LINE)
        
    print(f'{centered}{message}')

    print(LINE)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_any_input(message = ''):
    if message != '':
        print(message)
    input("(type anything to continue)")
    clear_terminal()

def ask_confirmation(message, default = True):
    result = None
    prompt = ''
    if default:
        prompt = '[Y/n]'
    else:
        prompt = '[y/N]'

    while result == None:
        print(message)
        print(prompt)
        answer = input().strip().lower()

        if answer == "":
            result = default
        
        if answer in ("y", "yes", "yup"):
            result = True
        
        if answer in ("n", "no", "nah"):
            result = False
        
        clear_terminal()
        print("Wrong input. Please type Y or N")

    clear_terminal()
    return result

def ask_text(message, center = None):
    if center:
        print_center(center)

    result = input(f'{message}\n-> ')
    
    clear_terminal()
    return result

def ask_menu_home():
    while True:
        clear_terminal()

        print_center('HOME')

        print('\n(1) Select File')
        print('(2) Configure')

        is_number, selected_option = parser.try_parse_int(input('\n-> '))

        if not is_number or selected_option < 0 or selected_option > 2:
            continue

        return selected_option

def ask_directory():
    result = None
    directory = ''

    clear_terminal()
    while result == None:
        print_center('Configuration')

        directory = input("Type the observed directory: \n-> ")

        dir = directory_util.exists_directory(directory)
        if dir and directory != '':
            clear_terminal()
            result = dir
        
        clear_terminal()
        print("Directory don't exist!")
    
    clear_terminal()
    return result

def directory_navigate(files, directory):
    print_center('Choose the file using the index')
    
    print(f'Current directory: {directory}\n')

    can_return = False
    if directory != Path(settings.OBSERVED_FOLDER).as_posix():
        can_return = True
        print('(0) ..\n')

    if not files:
        print('No files found!')
    else:
        for i, file in enumerate(files, start=1):
            type = "FOLDER" if file.is_dir() else "FILE"
            print(f'({i}) [{type}] {file.name}')

    print('\n(C) Redirect to home')
    print('(Z) Select the current directory (zip compact)')

    selected_index = input('\n-> ')

    if selected_index.lower() == 'c':
        return None
    
    if selected_index.lower() == 'z':
        return 'z'
    
    is_number, selected_index = parser.try_parse_int(selected_index)

    if not is_number or selected_index > len(files) or selected_index < 0:
        clear_terminal()
        return directory_navigate(files, directory)

    if selected_index == 0 and not can_return:
        clear_terminal()
        return directory_navigate(files, directory)
    elif selected_index == 0 and can_return:
        return Path(directory).parent

    return files[selected_index - 1]




        

