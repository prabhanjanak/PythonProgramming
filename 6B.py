import shutil

source_folder = input("Enter the path or folder name to be Zipped: ")
output_folder = input("Set the Zip folder name: ")

try:
    archived = shutil.make_archive(output_folder, "zip", source_folder)
    print(f"Zip file created as {output_folder}.zip")
except FileNotFoundError:
    print("Source folder not found")
