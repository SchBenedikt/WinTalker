import os
from tkinter import messagebox

def open_windows_taskmanager():
    try:
        os.system("start taskmgr")  # Command to open Microsoft Excel
    except Exception as e:
        messagebox.showerror("Error", f"Error opening Windows Task-Manager: {e}")
