import os
from tkinter import messagebox

def open_microsoft_powerpoint():
    try:
        os.system("start powerpnt")  # Command to open Microsoft Powerpoint
    except Exception as e:
        messagebox.showerror("Error", f"Error opening Microsoft PowerPoint: {e}")
