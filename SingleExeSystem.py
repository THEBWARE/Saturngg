import os
import zipfile
import requests

SATURN_GG_VERSION = "Saturn.gg-V1.1.4"
SATURN_GG_ZIP_URL = "https://github.com/THEBWARE/Saturngg/releases/download/Setup/Saturn.gg-V1.1.4.zip"
ROAMING_PATH = os.path.join(os.getenv('APPDATA'), SATURN_GG_VERSION)

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

if __name__ == "__main__":
    main()
