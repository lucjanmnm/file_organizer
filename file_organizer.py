import os
import shutil
import sys

EXTENSION_MAP = {
    "Pictures": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".odt", ".xls", ".xlsx", ".csv", ".ppt", ".pptx"],
    "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", ".m4a"],
    "Videos": [".mp4", ".avi", ".mov", ".wmv", ".flv", ".mkv"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".c", ".java", ".php", ".rb", ".go", ".sh", ".ipynb", ".dart", ".ts", ".json"],
    "Other": []
}

def get_folder_for_extension(ext):
    for folder, extensions in EXTENSION_MAP.items():
        if ext.lower() in extensions:
            return folder
    return "Other"

def organize_folder(folder_path):
    if not os.path.isdir(folder_path):
        print(f"Podana ścieżka '{folder_path}' nie jest folderem.")
        return

    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    if not files:
        print("Brak plików do posortowania.")
        return

    for filename in files:
        ext = os.path.splitext(filename)[1]
        dest_folder = get_folder_for_extension(ext)
        dest_path = os.path.join(folder_path, dest_folder)

        if not os.path.exists(dest_path):
            os.makedirs(dest_path)

        src = os.path.join(folder_path, filename)
        dst = os.path.join(dest_path, filename)
        shutil.move(src, dst)
        print(f"Przeniesiono: {filename} → {dest_folder}/")

    print("Sortowanie zakończone.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Użycie: python file_organizer.py /ścieżka/do/folderu")
    else:
        organize_folder(sys.argv[1])
