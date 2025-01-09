import zipfile
import os
import shutil
import requests
import time
import sys

if getattr(sys, 'frozen', False):
    script_dir = sys._MEIPASS
else:
    script_dir = os.path.dirname(os.path.realpath(__file__))

downloads_folder = os.path.join(script_dir, "ManiiLauncher Downloads")
schematics_zip = os.path.join(downloads_folder, "schematics.zip")
mods_zip = os.path.join(downloads_folder, "mods.zip")

user_home = os.environ.get('USERPROFILE')
appdata = os.path.join(user_home, "AppData", "Roaming")
minecraft_path = os.path.join(appdata, ".minecraft")
schematics_path = os.path.join(minecraft_path, "schematics")
mods_path = os.path.join(minecraft_path, "mods")

schematics_url = "https://github.com/ManiiProgramming/ManiiLauncher/releases/download/ModsAndSchematics/schematics.zip"
mods_url = "https://github.com/ManiiProgramming/ManiiLauncher/releases/download/ModsAndSchematics/mods.zip"

def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Directory created: {directory_path}")
    else:
        print(f"Directory already exists: {directory_path}")

def download_file(url, destination_path):
    try:
        print(f"Downloading {url}...")
        response = requests.get(url)
        response.raise_for_status()
        with open(destination_path, 'wb') as f:
            f.write(response.content)
        print(f"\nDownloaded {url} to {destination_path}")
    except requests.exceptions.RequestException as e:
        print(f"\nError downloading {url}: {e}")

def extract_zip(zip_path, extract_to):
    try:
        if not os.path.exists(extract_to):
            os.makedirs(extract_to)
            print(f"Directory created for extraction: {extract_to}")
        with zipfile.ZipFile(zip_path) as zf:
            file_list = zf.namelist()
            print(f"\nFiles in archive: {file_list}")
            zf.extractall(path=extract_to)
        print(f"\nExtraction of {zip_path} completed to {extract_to}")
    except zipfile.BadZipFile:
        print(f"\nError: {zip_path} is not a valid zip file.")
    except Exception as e:
        print(f"\nError extracting {zip_path}: {e}")

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Deleted the file: {file_path}")
    else:
        print(f"File not found: {file_path}")

def delete_directory(directory):
    try:
        if os.path.exists(directory):
            shutil.rmtree(directory)
            print(f"Deleted the folder {directory} and all the contents.")
        else:
            print(f"Folder {directory} doesn't exist.")
    except Exception as e:
        print(f"Error deleting {directory}: {e}")

try:
    create_directory(downloads_folder)

    delete_file(schematics_zip)
    delete_file(mods_zip)
    delete_directory(schematics_path)
    delete_directory(mods_path)
    print("\nNOTE: This part is only to check for existing files and remove them!\n\n")

    download_file(schematics_url, schematics_zip)
    print('\n')
    download_file(mods_url, mods_zip)

    input("\n\nMods and Schematics have been downloaded. Press enter to continue...")
    os.system("cls") 
    time.sleep(1)  # Sleep to give a slight delay to make it look like something is happening (Zip's are too light to take time)

    extract_zip(schematics_zip, schematics_path)
    time.sleep(1)
    print("\n\n\n")
    extract_zip(mods_zip, mods_path)
    
    input("\n\nExtraction complete. Press enter to delete downloaded files and exit...")

    delete_directory(downloads_folder)
    delete_file(schematics_zip)
    delete_file(mods_zip)

except Exception as e:
    print(f"Unexpected error: {e}")
