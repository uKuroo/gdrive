import auth.google_auth as auth
import core.file_selector as file_selector
import config.settings as settings
import integration.drive_provider as drive_provider
import utils.zip_handler as zip_handler
import cli.cli_manager as cli

def settings_view():
    if not cli.ask_confirmation("Previous configuration not found!\nDo you want to configure the application?"):
        return False

    directory = cli.ask_directory()

    cli.wait_any_input(f'Directory found!: {directory}')

    drive_folder_id = cli.ask_text('Type the google drive folder id: ')

    settings.set_config(directory, drive_folder_id)

    cli.wait_any_input("Configurated with success! you'll be redirected to Home.")

    return True

def home_view():
    while True:
        cli.clear_terminal()

        cli.ask_menu_home()
        
        choice = 1 # temporary

        if choice == 1:
            result = file_selector_view()

        if result == None:
            continue

def file_selector_view():
    file = file_selector.printar(settings.OBSERVED_FOLDER)

    if file == None:
        return None
    
    type = "FOLDER" if file.is_dir() else "FILE"

    print(f'Selected file to upload: [{type}] {file.name}')

    input('input to debug')

def start():
    try:
        if (not settings.has_valid_json()):
            if not settings_view():
                print('Exited')
                exit(0)

        settings.load_config()

        home_view()
    except KeyboardInterrupt:
        print('Program terminated by user')

if __name__ == '__main__':
    # file_selector.printar()
    start()