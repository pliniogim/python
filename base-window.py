import tkinter as tk
from tkinter import filedialog
import os

def choose_folder():
    folder_path = filedialog.askdirectory()
    folder_var.set(folder_path)

def print_files_in_folder():
    folder_path = folder_var.get()
    if not folder_path:
        print("Please choose a folder first.")
        return

    files = os.listdir(folder_path)
    files = sorted(files)
    print("Files in the chosen folder:")
    for filename in files:
        print(filename)

def create_window():
    window = tk.Tk()
    window.title("Folder Chooser")
    window.minsize(300,300)

    # Title label
    title_label = tk.Label(window, text="Choose a Folder", font=("Helvetica", 16))
    title_label.pack(pady=20)

    global folder_var  # Make folder_var a global variable
    folder_var = tk.StringVar()

    # Text field to display selected folder path
    folder_label = tk.Label(window, textvariable=folder_var)
    folder_label.pack(pady=10)

    # Button to choose folder
    choose_button = tk.Button(window, height=2, width=10, text="Browse", command=choose_folder)
    choose_button.pack(pady=10)

    # Button to print files in folder
    print_button = tk.Button(window, height=2, width=10, text="Execute", command=print_files_in_folder)
    print_button.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    create_window()
