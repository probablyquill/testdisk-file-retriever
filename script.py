import os, shutil
from pathlib import Path

filepath = os.getcwd()
list_of_filetypes = ["*.jpg", "*.png", "*.pdf", "*.doc", "*.docx", "*.txt", "*.xls", "*.mp4"]
i = 0
list_of_files = []

for item in list_of_filetypes:
    print("Searching for: " + filepath + "\\" + item)
    files_found = Path(filepath).rglob(item)
    for element in files_found: list_of_files.append(element)

try: os.makedirs("PulledFiles")
except: pass

for item in list_of_files:
    extension = str(item).split(".")[len(str(item).split(".")) - 1]
    print("Copying and Renaming " + str(item) + " to PulledFiles\\" + str(i) + "." + str(extension))
    shutil.copy(item, "PulledFiles\\" + str(i) + "." + str(extension))
    i += 1