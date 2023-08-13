import os

def rename_folders_with_number(directory):
    folders = [folder for folder in os.listdir(directory) if os.path.isdir(os.path.join(directory, folder))]
    folders.sort()  # Sort the folders to get consistent numbering
    
    for index, folder in enumerate(folders, start=1):
        old_folder_path = os.path.join(directory, folder)
        new_folder_name = f"{index}. {folder.capitalize()}"
        new_folder_path = os.path.join(directory, new_folder_name)
        os.rename(old_folder_path, new_folder_path)
        print(f"Renamed '{folder}' to '{new_folder_name}'")

if __name__ == "__main__":
    target_directory = "D:/My Github repositories/Python-Projects-Collection/2. Python Starter Projects"  # Replace this with the full path of the directory containing the folders to rename
    rename_folders_with_number(target_directory)