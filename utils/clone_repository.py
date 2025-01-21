import os
import git

def clone_repository(github_url: str, folder_path: str):
    """Clone the GitHub repository to a local folder, removing the folder if it already exists."""
    print(f"Cloning repository from {github_url}...")

    # Check if the folder already exists
    if os.path.exists(folder_path):
        # Remove the existing folder and its contents
        print(f"Folder {folder_path} already exists. Removing it...")
        remove_folder(folder_path)

    # Create the folder if it doesn't exist
    os.makedirs(folder_path)

    # Clone the repository into the folder
    git.Repo.clone_from(github_url, folder_path)

# Function to generate the prompt using code2prompt
def remove_folder(folder_path: str):
    """Remove a folder and its contents recursively."""
    for root, dirs, files in os.walk(folder_path, topdown=False):
        # Remove all files first
        for name in files:
            os.remove(os.path.join(root, name))
        # Then remove all directories
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(folder_path)  # Remove the empty folder itself
