import tkinter as tk
from tkinter import simpledialog
import sys
import os
from tkinter import messagebox

def shutdown_computer():
    confirmation = messagebox.askyesno("Shutdown Confirmation", "Are you sure you want to shutdown your computer?")
    if confirmation:
        try:
            os.system("shutdown /s /t 0")  # Shutdown command for Windows
        except Exception as e:
            messagebox.showerror("Error", f"Error shutting down the computer: {e}")