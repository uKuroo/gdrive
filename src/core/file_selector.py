from pathlib import Path
import cli.cli_manager as cli

def printar(directory):
    cli.clear_terminal()

    path = Path(directory).expanduser()

    files = list(path.iterdir())

    selected_file = cli.directory_navigate(files, directory)

    if selected_file == None:
        return None

    if selected_file == 'z':
        return Path(directory)
    
    if(selected_file.is_dir()):
        return printar(selected_file.as_posix())
    
    return selected_file
    