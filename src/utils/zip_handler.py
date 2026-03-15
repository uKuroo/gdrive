import shutil
import os
import cli.cli_manager as cli
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

def zip_folder(folder_path: str) -> Path:
    source_path = Path(folder_path)
    
    root_dir = PROJECT_ROOT
    temp_dir = root_dir / 'temp'
    
    temp_dir.mkdir(exist_ok=True)
    
    folder_name = source_path.name
    output_base_path = temp_dir / folder_name
    
    print(f"Compressing '{folder_name}' into temp directory...")

    zip_path = shutil.make_archive(
        base_name=str(output_base_path),
        format='zip',
        root_dir=str(source_path)
    )
    
    cli.wait_any_input(f"Compression complete: {zip_path}")
    
    return Path(zip_path)

def cleanup_temp_folder() -> None:
    root_dir = PROJECT_ROOT
    temp_dir = root_dir / 'temp'
    
    if temp_dir.exists() and temp_dir.is_dir():
        try:
            shutil.rmtree(temp_dir)
            return True
        except Exception as e:
            return False