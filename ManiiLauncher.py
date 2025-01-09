import zipfile
import os
import shutil
import requests
from os import system as sys

script_dir = os.path.dirname(os.path.realpath(__file__))

schematics_zip = os.path.join(script_dir, "schematics.zip")
mods_zip = os.path.join(script_dir, "mods.zip")

appdata = os.environ.get('APPDATA')
schematics_path = r"\.minecraft\schematics"
mods_path = r"\.minecraft\mods"
extract_to1 = appdata + schematics_path
extract_to2 = appdata + mods_path

schematics_url = "https://github.com/ManiiProgramming/ManiiLauncher/releases/download/ModsAndSchematics/schematics.zip"
mods_url = "https://github.com/ManiiProgramming/ManiiLauncher/releases/download/ModsAndSchematics/mods.zip"

def download_file(url, destination_path):
    try:
        print(f"Downloading {url}...")
        response = requests.get(url)
        response.raise_for_status()
        with open(destination_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {url} to {destination_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")

def extract_zip(zip_path, extract_to):
    try:
        with zipfile.ZipFile(zip_path) as zf:
            file_list = zf.namelist()
            print(f"Files in archive: {file_list}")
            zf.extractall(path=extract_to)
        print(f"Extraction of {zip_path} completed.")
    except zipfile.BadZipFile:
        print(f"Error: {zip_path} is not a valid zip file.")
    except Exception as e:
        print(f"Error extracting {zip_path}: {e}")

def delete_directory(directory):
    try:
        if os.path.exists(directory):
            shutil.rmtree(directory)
            print(f"Deleted the folder {directory} and all the contents.")
        else:
            print(f"Folder {directory} doesn't exist.")
    except Exception as e:
        print(f"Error deleting {directory}: {e}")

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Deleted the file: {file_path}")
    else:
        print(f"File not found: {file_path}")



try:
    delete_file(r"mods.zip")
    delete_file(r"schematics.zip")

    delete_directory(extract_to1)
    delete_directory(extract_to2)
    print("NOTE: This part is only to check for existing files and remove them!")

    download_file(schematics_url, schematics_zip)
    download_file(mods_url, mods_zip)

    input("Mods and Schematics have been downloaded. Press enter to continue...")

    extract_zip(schematics_zip, extract_to1)
    extract_zip(mods_zip, extract_to2)

    input("Extraction complete. Press enter to delete excessive files and exit.")

    delete_file(r"mods.zip")
    delete_file(r"schematics.zip")

except Exception as e:
    print(f"Unexpected error: {e}")
