import os
from tkinter import messagebox

def open_explorer():
    try:
        os.system("start explorer")
    except Exception as e:
        messagebox.showerror("Error", f"Error opening Microsoft Windows Explorer: {e}")
