import os
import shutil

# Replace 'path/to/your/directory' with the actual path to your directory
DIRECTORY = 'C:\VINAY\vinay pen drive'

# Define the mapping of file extensions to their respective folders
FILE_TYPES = {
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Videos': ['.mp4', '.mkv', '.flv', '.avi', '.mov'],
    'Music': ['.mp3', '.wav', '.aac', '.flac'],
    'Archives': ['.zip', '.tar', '.gz', '.rar'],
    'Scripts': ['.py', '.sh', '.bat', '.js', '.html', '.css']
}

def create_folders():
    for folder in FILE_TYPES.keys():
        folder_path = os.path.join(DIRECTORY, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def move_files():
    for item in os.listdir(DIRECTORY):
        item_path = os.path.join(DIRECTORY, item)
        if os.path.isfile(item_path):
            file_extension = os.path.splitext(item)[1].lower()
            moved = False
            for folder, extensions in FILE_TYPES.items():
                if file_extension in extensions:
                    shutil.move(item_path, os.path.join(DIRECTORY, folder, item))
                    print(f"Moved {item} to {folder}")
                    moved = True
                    break
            if not moved:
                print(f"No matching folder for {item}")

if __name__ == "__main__":
    create_folders()
    move_files()
    print("File organization complete.")
