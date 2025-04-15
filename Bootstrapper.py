import requests
import os
import zipfile

def display_ascii_art():
    # ANSI escape code for blue text
    blue_color = "\033[94m"
    # ANSI escape code to reset text color to default
    reset_color = "\033[0m"

    ascii_art = r"""
  ____        _                                 
 / ___|  __ _| |_ _   _ _ __ _ __    __ _  __ _ 
 \___ \ / _` | __| | | | '__| '_ \  / _` |/ _` |
  ___) | (_| | |_| |_| | |  | | | || (_| | (_| |
 |____/ \__,_|\__|\__,_|_|  |_| |_(_)__, |\__, |
                                    |___/ |___/ 
    """
    print(f"{blue_color}{ascii_art}{reset_color}")

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
    display_ascii_art()  # Fixed: Correct function name
    url = "https://github.com/THEBWARE/Saturngg/releases/download/Source/Saturn.zip"
    zip_filename = "Saturn.zip"
    extract_to = "Saturn"

    # Ensure the directory exists
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)

    download_file(url, zip_filename)
    unzip_file(zip_filename, extract_to)

    print("All steps completed successfully.")

if __name__ == "__main__":
    main()
