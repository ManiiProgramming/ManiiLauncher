import zipfile
import os
import shutil
from os import system as sys

appdata = os.environ.get('APPDATA')
zip1_path = r"schematics.zip"
zip2_path = r"mods.zip"
schematics_path = "\.minecraft\schematics"
mods_path = "\.minecraft\mods"
extract_to1 = appdata+schematics_path
extract_to2 = appdata+mods_path

if os.path.exists(extract_to1):
    shutil.rmtree(extract_to1)
    print("Deleted the folder and all the contents of the folder.")
else:
    print("Folder doesn't exist.")

if os.path.exists(extract_to2):
    shutil.rmtree(extract_to2)
    print("Deleted the folder and all the contents of the folder.")
else:
    print("Folder doesn't exist.")

input("Mods and Schematics folders have been reset, press enter to continue...")

with zipfile.ZipFile(zip1_path) as zf:
    file_list = zf.namelist()
    print(f"Files in archive: {file_list}")
    zf.extractall(path=extract_to1)
with zipfile.ZipFile(zip2_path) as zf:
    file_list = zf.namelist()
    print(f"Files in archive: {file_list}")
    zf.extractall(path=extract_to2)

input("Extraction Complete. Press enter to continue...")