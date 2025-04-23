    import requests
import os
import zipfile
import time

def display_ascii_art():
    blue_color = "\033[94m"
    reset_color = "\033[0m"

    ascii_art = """
 ____        _                                 
/ ___|  __ _| |_ _   _ _ __ _ __    __ _  __ _ 
\___ \ / _` | __| | | | '__| '_ \  / _` |/ _` |
 ___) | (_| | |_| |_| | |  | | | || (_| | (_| |
|____/ \__,_|\__|\__,_|_|  |_| |_(_)__, |\__, |
                                   |___/ |___/ 
    """
    print(f"{blue_color}{ascii_art}{reset_color}")
    print("Much Better GUI And added script hub!")

def download_file(url, filename):
    print(f"Step 1: Downloading {filename}")
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f"Step 2: {filename} downloaded successfully.")

def unzip_file(filename, extract_to):
    print(f"Step 3: Unzipping {filename} to {extract_to}")
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Step 4: {filename} unzipped successfully.")

def main():
    display_ascii_art()
    url = "https://github.com/THEBWARE/Saturngg/releases/download/Setup/Saturn.gg-V1.1.4.zip"
    zip_filename = "Saturn.gg-V1.1.4.zip"
    extract_to = "Saturn.gg-V1.1.4"

    if not os.path.exists(extract_to):
        os.makedirs(extract_to)

    download_file(url, zip_filename)
    unzip_file(zip_filename, extract_to)

    print("All steps completed successfully.")
    time.sleep(5)

if __name__ == "__main__":
    main()
