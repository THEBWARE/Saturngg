import os
import shutil
import time
import zipfile
import requests
from pathlib import Path

SATURN_GG_VERSION = "Saturn.gg-V1.1.4"
SATURN_GG_ZIP_URL = "https://github.com/THEBWARE/Saturngg/releases/download/Setup/Saturn.gg-V1.1.4.zip"
ROAMING_PATH = os.path.join(os.getenv('APPDATA'), SATURN_GG_VERSION)
LOCAL_WORKSPACE = "Workspace"

def download_and_extract():
    try:
        os.makedirs(ROAMING_PATH, exist_ok=True)
        response = requests.get(SATURN_GG_ZIP_URL, stream=True)
        zip_path = os.path.join(ROAMING_PATH, f"{SATURN_GG_VERSION}.zip")
        
        with open(zip_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(ROAMING_PATH)
        
        os.remove(zip_path)
        
        for root, dirs, files in os.walk(ROAMING_PATH):
            if "Saturn.gg.exe" in files:
                os.startfile(os.path.join(root, "Saturn.gg.exe"))
                break
            
    except:
        pass

def sync_workspace():
    local_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), LOCAL_WORKSPACE)
    os.makedirs(local_path, exist_ok=True)
    
    original_path = None
    for root, dirs, files in os.walk(ROAMING_PATH):
        if "Workspace" in dirs:
            original_path = os.path.join(root, "Workspace")
            break
    
    if not original_path:
        return
    
    last_state = {}
    
    while True:
        try:
            current_state = {}
            for root, dirs, files in os.walk(original_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, original_path)
                    current_state[rel_path] = os.path.getmtime(file_path)
            
            if last_state != current_state:
                if os.path.exists(local_path):
                    shutil.rmtree(local_path)
                os.makedirs(local_path, exist_ok=True)
                
                for root, dirs, files in os.walk(original_path):
                    for file in files:
                        src = os.path.join(root, file)
                        rel = os.path.relpath(src, original_path)
                        dst = os.path.join(local_path, rel)
                        os.makedirs(os.path.dirname(dst), exist_ok=True)
                        shutil.copy2(src, dst)
                
                last_state = current_state.copy()
            
            time.sleep(1)
            
        except:
            time.sleep(5)

def main():
    if not os.path.exists(ROAMING_PATH):
        download_and_extract()
    else:
        for root, dirs, files in os.walk(ROAMING_PATH):
            if "Saturn.gg.exe" in files:
                os.startfile(os.path.join(root, "Saturn.gg.exe"))
                break
        else:
            shutil.rmtree(ROAMING_PATH)
            download_and_extract()
    
    sync_workspace()

if __name__ == "__main__":
    main()
