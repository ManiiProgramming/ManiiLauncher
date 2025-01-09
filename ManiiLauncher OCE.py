import zipfile
import os
import shutil
import requests
import time
import sys
from tqdm import tqdm

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

def download_file(url, destination_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        total_size = int(response.headers.get('content-length', 0))
        with open(destination_path, 'wb') as f, tqdm(
            desc=f"Downloading {os.path.basename(destination_path)}",
            total=total_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
                bar.update(len(chunk))
    except requests.exceptions.RequestException as e:
        print(f"\nError downloading {url}: {e}")

def extract_zip(zip_path, extract_to):
    try:
        if not os.path.exists(extract_to):
            os.makedirs(extract_to)
        with zipfile.ZipFile(zip_path) as zf:
            zf.extractall(path=extract_to)
    except zipfile.BadZipFile:
        print(f"\nError: {zip_path} is not a valid zip file.")
    except Exception as e:
        print(f"\nError extracting {zip_path}: {e}")

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

def delete_directory(directory):
    try:
        if os.path.exists(directory):
            shutil.rmtree(directory)
    except Exception as e:
        print(f"Error deleting {directory}: {e}")

try:
    create_directory(downloads_folder)

    delete_file(schematics_zip)
    delete_file(mods_zip)
    delete_directory(schematics_path)
    delete_directory(mods_path)

    download_file(schematics_url, schematics_zip)
    download_file(mods_url, mods_zip)

    extract_zip(schematics_zip, schematics_path)
    extract_zip(mods_zip, mods_path)

    delete_directory(downloads_folder)
    delete_file(schematics_zip)
    delete_file(mods_zip)

except Exception as e:
    print(f"Unexpected error: {e}")
