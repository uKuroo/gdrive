import json
import os
from pathlib import Path

OBSERVED_FOLDER = ''
DRIVE_FOLDER_ID = ''

HOME_DIR = os.path.expanduser("~")

CONFIG = {
  "OBSERVED_FOLDER": "",
  "DRIVE_FOLDER_ID": ""
}

def has_valid_json():
  path = Path("settings.json")

  if not path.exists():
        return False

  with open('settings.json', 'r', encoding='utf-8') as f:
    valid = True

    config = json.load(f)
    
    missing_keys = [key for key in CONFIG if key not in config]
    
    if missing_keys:
      valid = False

    return valid
    
def set_config(observed_folder, drive_folder_id):
  CONFIG['OBSERVED_FOLDER'] = observed_folder
  CONFIG['DRIVE_FOLDER_ID'] = drive_folder_id

  with open('settings.json', 'w', encoding='utf-8') as f:
    json.dump(CONFIG, f, ensure_ascii=False, indent=2)

def load_config():
  with open('src/config/config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

    OBSERVED_FOLDER = config.get("OBSERVED_FOLDER", "")
    DRIVE_FOLDER_ID = config.get("BASE_EXTENSION_FOLDER", "")