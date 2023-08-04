import os
from tkinter import messagebox

def open_microsoft_word():
    try:
        os.system("start winword")  # Command to open Microsoft Word
    except Exception as e:
        messagebox.showerror("Error", f"Error opening Microsoft Word: {e}")
