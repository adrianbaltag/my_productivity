"""This script cleans the contents of specified folders on your Desktop."""

import os

# Define the base path to the Desktop
base_path = os.path.expanduser("~/Desktop/")  # Path to the Desktop folder

# todo: Replace the folder names in the list below with the actual names of the folders you want to clean.
# List of folders to clean directly on the Desktop
target_folders_list = ["delete1", "delete2", "delete3", "del6", "IMGS"]


def clean_folders(desktop_path, folders_to_clean):
    """Cleans the contents of the specified folders directly on your Desktop, including files in subfolders."""
    for folder in folders_to_clean:
        folder_path = os.path.join(
            desktop_path, folder
        )  # Full path to the folder on Desktop
        if os.path.exists(folder_path):  # Check if the folder exists
            files_deleted = False  # Flag to track if any files were deleted
            for item in os.listdir(
                folder_path
            ):  # List of files and subfolders in the folder
                item_path = os.path.join(folder_path, item)  # Full path to the item
                if os.path.isdir(item_path):  # If it's a subfolder, clean its contents
                    # Check for files inside the subfolder
                    for sub_item in os.listdir(item_path):
                        sub_item_path = os.path.join(item_path, sub_item)
                        if os.path.isfile(
                            sub_item_path
                        ):  # If it's a file inside the subfolder
                            try:
                                os.remove(sub_item_path)  # Remove the file
                                print(
                                    f"Deleted: {sub_item_path}"
                                )  # Print what was deleted
                                files_deleted = True  # Mark that a file was deleted
                            except (OSError, FileNotFoundError) as e:
                                print(f"Error deleting {sub_item_path}: {e}")
                elif os.path.isfile(item_path):  # If it's a file inside the main folder
                    try:
                        os.remove(item_path)  # Remove the file
                        print(f"Deleted: {item_path}")  # Print what was deleted
                        files_deleted = True  # Mark that a file was deleted
                    except (OSError, FileNotFoundError) as e:
                        print(f"Error deleting {item_path}: {e}")

            if not files_deleted:  # If no files were deleted
                print(
                    f"No files to delete in the {folder} folder."
                )  # Print message if no files to delete
        else:
            print(
                f"Folder {folder_path} does not exist."
            )  # Print error message if the folder doesn't exist


# Call the function to clean the folders
if __name__ == "__main__":
    clean_folders(desktop_path=base_path, folders_to_clean=target_folders_list)
