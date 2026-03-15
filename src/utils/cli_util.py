import os
import utils.directory_util as directory_util

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_any_input(message = ''):
    if message != '':
        print(message)
    input("(type anything to continue)")

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

def ask_directory():
    result = None
    directory = ''

    while result == None:
        directory = input("Type the observed directory: ")

        if directory_util.exists_directory(directory):
            clear_terminal()
            result = directory
        
        clear_terminal()
        print("Directory don't exist!")
    
    clear_terminal()
    return result




        

