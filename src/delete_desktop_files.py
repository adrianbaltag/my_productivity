""": This script deletes ALL specified files extensions from Desktop"""

import os


def delete_files_by_extension(path, extensions_to_delete):
    """
    Deletes all files from the Desktop based on the given file extensions.

    Args:
        path (str): Path to the Desktop folder.
        file_extensions (list): List of file extensions (e.g., ['.docx', '.txt']).
    """
    for item in os.listdir(path):  # List all items on the Desktop
        item_path = os.path.join(path, item)  # Full path to the item
        if os.path.isfile(item_path):  # Check if it's a file
            # Check if the file has a matching extension
            if any(item.lower().endswith(ext) for ext in extensions_to_delete):
                try:
                    os.remove(item_path)  # Remove the file
                    print(f"Deleted: {item_path}")  # Print what was deleted
                except (OSError, FileNotFoundError) as e:
                    print(f"Error deleting {item_path}: {e}")
            else:
                print(
                    "No matching file extensions found."
                )  # Print message if no matching file extensions


if __name__ == "__main__":
    base_path = os.path.expanduser("~/Desktop/")  # Path to the Desktop folder
    # List of file extensions to delete
    # Add or remove file extensions as needed
    file_extensions = [
	    ".docx",
        ".png",
        ".txt",
        ".xlsx",
        ".jpg",
        ".pdf",
        ".isa",
        ".pcap",
    ]
    delete_files_by_extension(base_path, file_extensions)
