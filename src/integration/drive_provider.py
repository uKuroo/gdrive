import os
import config.settings as settings
from pathlib import Path
from googleapiclient.http import MediaFileUpload

SERVICE = None

def set_service(service):
    global SERVICE
    SERVICE = service

def create_drive_folder(folder_name: str) -> str:
    file_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    
    file_metadata['parents'] = [settings.DRIVE_FOLDER_ID]
    
    folder = SERVICE.files().create(
        body=file_metadata,
        fields='id'
    ).execute()
    
    folder_id = folder.get('id')
    
    return folder_id

def upload_to_drive(file_path: str, parent_folder_id: str = None) -> str:
    target_file = Path(file_path)
    
    if not target_file.exists():
        raise FileNotFoundError(f"File not found for upload: {file_path}")

    file_metadata = {'name': target_file.name}
    if parent_folder_id:
        file_metadata['parents'] = [parent_folder_id]

    media = MediaFileUpload(
        str(target_file),
        resumable=True
    )

    uploaded_file = SERVICE.files().create(
        body=file_metadata,
        media_body=media,
        fields='id, webViewLink'
    ).execute()

    file_id = uploaded_file.get('id')
    shareable_link = uploaded_file.get('webViewLink')

    print(f"Upload complete! File ID: {file_id}")
    
    permission_body = {
        'type': 'anyone',
        'role': 'reader'
    }
    
    SERVICE.permissions().create(
        fileId=file_id,
        body=permission_body
    ).execute()
    
    return shareable_link