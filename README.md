# tryps
https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh

r"C:\Users\YourName\Downloads"

# Куда сортировать
FOLDERS = {
    "images": [".png", ".jpg", ".jpeg", ".gif"],
    "docs": [".pdf", ".docx", ".txt"],
    "videos": [".mp4", ".mkv", ".avi"],
}

def get_folder(file):
    for folder, extensions in FOLDERS.items():
        for ext in extensions:
            if file.lower().endswith(ext):
                return folder
    return "other"

def organize_files():
    for file in os.listdir(SOURCE_DIR):
        file_path = os.path.join(SOURCE_DIR, file)

        if os.path.isfile(file_path):
            folder_name = get_folder(file)
            target_dir = os.path.join(SOURCE_DIR, folder_name)

            if not os.path.exists(target_dir):
                os.makedirs(target_dir)

            shutil.move(file_path, os.path.join(target_dir, file))
            print(f"Moved: {file} → {folder_name}")

if name == "main":
    organize_files()
