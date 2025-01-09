import zipfile
import os
import shutil
import requests
import time
import sys

# Get the directory where the script is located (or where the executable is running from)
if getattr(sys, 'frozen', False):
    # Running as a bundled executable
    script_dir = sys._MEIPASS
else:
    # Running as a script
    script_dir = os.path.dirname(os.path.realpath(__file__))

# Define paths for downloaded zip files
downloads_folder = os.path.join(script_dir, "ManiiLauncher Downloads")
schematics_zip = os.path.join(downloads_folder, "schematics.zip")
mods_zip = os.path.join(downloads_folder, "mods.zip")

# Define the appdata paths for extraction
appdata = os.environ.get('APPDATA')
schematics_path = r"\.minecraft\schematics"
mods_path = r"\.minecraft\mods"
extract_to1 = os.path.join(appdata, schematics_path)
extract_to2 = os.path.join(appdata, mods_path)

# URLs for downloading the mods and schematics
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
    # Ensure the 'ManiiLauncher Downloads' directory exists
    create_directory(downloads_folder)

    # Delete any pre-existing files and directories from previous runs
    delete_file(schematics_zip)
    delete_file(mods_zip)
    delete_directory(extract_to1)
    delete_directory(extract_to2)
    print("\nNOTE: This part is only to check for existing files and remove them!\n\n")

    # Download the files
    download_file(schematics_url, schematics_zip)
    download_file(mods_url, mods_zip)

    input("Mods and Schematics have been downloaded. Press enter to continue...")
    os.system("cls") 
    time.sleep(1)  # Sleep to give a slight delay to make it look like something is happening

    # Extract the downloaded files
    extract_zip(schematics_zip, extract_to1)
    time.sleep(1)
    extract_zip(mods_zip, extract_to2)
    
    input("Extraction complete. Press enter to delete downloaded files and exit...")

    # Clean up the downloaded files
    delete_file(schematics_zip)
    delete_file(mods_zip)

except Exception as e:
    print(f"Unexpected error: {e}")
