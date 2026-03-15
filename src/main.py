import auth.google_auth as auth
import cli.file_selector as file_selector
import config.settings as settings
import integration.drive_provider as drive_provider
import utils.zip_handler as zip_handler
import utils.cli_util as cli_util

def settings_view():
    cli_util.ask_confirmation("Previous configuration not found!\nDo you want to configure the application?")

    directory = cli_util.ask_directory()

    cli_util.wait_any_input(f'Directory found!: {directory}')


def start():
    if (not settings.has_valid_json()):
        settings_view()

start()