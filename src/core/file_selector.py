from pathlib import Path
import cli.cli_manager as cli

def printar(directory):
    cli.clear_terminal()

    path = Path(directory).expanduser()

    try:
        files = list(path.iterdir())
    except PermissionError:
        cli.wait_any_input("No permission to access the folder")
        return printar(Path(directory).parent)

    selected_file = cli.directory_navigate(files, directory)

    if selected_file == None:
        return None

    if selected_file == 'z':
        return Path(directory)
    
    if(selected_file.is_dir()):
        return printar(selected_file.as_posix())
    
    return selected_file
    