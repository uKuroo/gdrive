from datetime import datetime
import auth.google_auth as auth
import core.file_selector as file_selector
import config.settings as settings
import integration.drive_provider as drive_provider
import utils.zip_handler as zip_handler
import cli.cli_manager as cli

def settings_view(configured = False):
    if not configured:
        if not cli.ask_confirmation("Previous configuration not found!\nDo you want to configure the application?"):
            return None

    directory = cli.ask_directory()

    cli.wait_any_input(f'Directory found!: {directory}')

    drive_folder_id = cli.ask_text("Type the google drive folder id: ", "Configuration")

    settings.set_config(directory, drive_folder_id)

    cli.wait_any_input("Configurated with success! you'll be redirected to Home.")

    return True

def file_selector_view():
    file = file_selector.printar(settings.OBSERVED_FOLDER)

    if file == None:
        return None
    
    if file.is_dir():
        if not cli.ask_confirmation(f'Do you want to compress {file.name} into a zip and upload it?'):
            return None

        return zip_handler.zip_folder(file.absolute())

    type = "FOLDER" if file.is_dir() else "FILE"

    print(f'Selected file to upload: [{type}] {file.name}')

    return file

def home_view():
    while True:
        cli.clear_terminal()

        choice = cli.ask_menu_home()

        if choice == 1:
            result = file_selector_view()
            if result == None:
                continue

            try:
                drive_provider.set_service(auth.authenticate_drive())
            except FileNotFoundError:
                cli.wait_any_input('')
            
            created_folder = drive_provider.create_drive_folder(datetime.now().strftime("%d-%m-%Y"))

            link = drive_provider.upload_to_drive(result.absolute(), created_folder)

            zip_handler.cleanup_temp_folder()

            cli.wait_any_input(f'File uploaded with succes!\nShared Link: {link}')

        if choice == 2:
            result = settings_view(True)

        if result == None:
            continue

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
    start()