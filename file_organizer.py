import os
import shutil
import sys
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

EXTENSION_MAP = {
    "Pictures": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".odt", ".xls", ".xlsx", ".csv", ".ppt", ".pptx", ".xopp"],
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
        return "Podana ścieżka nie jest folderem.\n"

    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    if not files:
        return "Brak plików do posortowania.\n"

    stats = {cat: 0 for cat in EXTENSION_MAP}
    logs = ""
    for filename in files:
        ext = os.path.splitext(filename)[1]
        dest_folder = get_folder_for_extension(ext)
        dest_path = os.path.join(folder_path, dest_folder)
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)
        src = os.path.join(folder_path, filename)
        dst = os.path.join(dest_path, filename)
        shutil.move(src, dst)
        stats[dest_folder] += 1
        logs += f"Przeniesiono: {filename} → {dest_folder}/\n"

    summary = "\nPodsumowanie:\n"
    for cat, count in stats.items():
        if count:
            summary += f"{cat}: {count} plików\n"

    logs += summary + "\nSortowanie zakończone.\n"
    with open(os.path.join(folder_path, "organizer_log.txt"), "w", encoding="utf-8") as f:
        f.write(logs)
    return logs

def start_gui():
    def browse_folder():
        folder_selected = filedialog.askdirectory()
        entry_folder.delete(0, tk.END)
        entry_folder.insert(0, folder_selected)

    def run_organize():
        folder_path = entry_folder.get()
        output.delete(1.0, tk.END)
        logs = organize_folder(folder_path)
        output.insert(tk.END, logs)
        messagebox.showinfo("Organizer", "Sortowanie zakończone!\nZobacz log w organizer_log.txt w wybranym folderze.")

    root = tk.Tk()
    root.title("Organizer Plików")
    root.geometry("600x400")
    root.resizable(False, False)

    label = tk.Label(root, text="Wybierz folder do posortowania:", font=("Arial", 12))
    label.pack(pady=10)

    frame = tk.Frame(root)
    frame.pack(pady=5)
    entry_folder = tk.Entry(frame, width=50)
    entry_folder.pack(side=tk.LEFT, padx=5)
    btn_browse = tk.Button(frame, text="Przeglądaj...", command=browse_folder)
    btn_browse.pack(side=tk.LEFT)

    btn_sort = tk.Button(root, text="Sortuj pliki!", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=run_organize)
    btn_sort.pack(pady=15)

    output = scrolledtext.ScrolledText(root, width=70, height=14, font=("Consolas", 10))
    output.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(organize_folder(sys.argv[1]))
    else:
        start_gui()
