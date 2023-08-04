import os
from tkinter import messagebox

def open_microsoft_excel():
    try:
        os.system("start excel")  # Command to open Microsoft Excel
    except Exception as e:
        messagebox.showerror("Error", f"Error opening Microsoft Excel: {e}")
