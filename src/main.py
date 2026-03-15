import auth.google_auth as auth
import cli.file_selector as file_selector
import config.settings as settings
import integration.drive_provider as drive_provider
import utils.zip_handler as zip_handler
import utils.cli_util as cli_util

def settings_view():
    if not cli_util.ask_confirmation("Previous configuration not found!\nDo you want to configure the application?"):
        return False

    directory = cli_util.ask_directory()

    cli_util.wait_any_input(f'Directory found!: {directory}')

    drive_folder_id = cli_util.ask_text('Type the google drive folder id: ')

    settings.set_config(directory, drive_folder_id)

    cli_util.wait_any_input("Configurated with success! you'll be redirected to Home.")

    return True

def home_view():
    cli_util.ask_menu_home()



def start():
    try:
        if (not settings.has_valid_json()):
            if not settings_view():
                print('Exited')
                exit(0)
        home_view()
    except KeyboardInterrupt:
        print('Program killed by user')

if __name__ == '__main__':
    start()