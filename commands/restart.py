import tkinter as tk
from tkinter import simpledialog
import sys
import os
from tkinter import messagebox

def restart_computer():
    confirmation = messagebox.askyesno("Restart Confirmation", "Are you sure you want to restart your computer?")
    if confirmation:
        try:
            os.system("shutdown /r /t 0")  # Restart command for Windows
        except Exception as e:
            messagebox.showerror("Error", f"Error restarting the computer: {e}")