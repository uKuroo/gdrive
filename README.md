# ☁️ GDrive Backup CLI

A Command Line Interface (CLI) tool developed in Python for local directory navigation, automatic folder compression, and automated uploads to Google Drive using Service Accounts. 

Ideal for general backup routines (such as saving game worlds, local projects, or important documents) straight to the cloud, without the need for manual login.

## ✨ Features

* **CLI File Explorer:** Navigate your local directories directly through the terminal.
* **Smart Compression:** Identifies if the selected item is a folder and offers the option to automatically zip it to uploading.
* **Automated Upload:** Integration with the Google Drive API (v3) via Service Account, creating dynamic folders (e.g., by date) and sending files silently and securely.
* **Modular Architecture:** Clean code separated by domains (Core, Auth, CLI, Integration, and Utils).

## 📂 Project Structure

The architecture was designed following the Separation of Concerns principle:

```text
GDRIVE/
│
├── src/
│   ├── auth/                   # Credential management and token generation
│   │   ├── credentials/        # ⚠️ (Add your credentials.json here)
│   │   └── google_auth.py      # API authentication logic
│   │
│   ├── cli/                    # User interface
│   │   └── cli_manager.py      # Menus and inputs
│   │
│   ├── config/                 # Static system configurations
│   │   └── settings.py         # Variable and path loading
│   │
│   ├── core/                   # Main business logic
│   │   └── file_selector.py    # Orchestrates file/folder selection
│   │
│   ├── integration/            # External API communication
│   │   └── drive_provider.py   # Upload and folder creation methods in GDrive
│   │
│   ├── utils/                  # Generic helper tools
│   │   ├── directory_util.py   # OS path manipulation
│   │   ├── parser.py           # Data formatting and conversion
│   │   └── zip_handler.py      # Compression logic (shutil/zipfile)
│   │
│   └── main.py                 # Application entrypoint
│
├── settings.json           # User configurations (Root folder ID, etc.)
├── requirements.txt        # Project dependencies (pip)
└── README.md               # Documentation

```

## (Optional) Create and activate a virtual environment
``` text
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

## Install the required libraries
``` text
pip install -r requirements.txt
```
