import os
import pyautogui
import time
import tkinter as tk
from tkinter import simpledialog, messagebox

def enable_dark_mode():
    try:
        # Modify the Windows registry to enable dark mode
        os.system('reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v AppsUseLightTheme /t REG_DWORD /d 0 /f')
        os.system('reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v SystemUsesLightTheme /t REG_DWORD /d 0 /f')
        
        # Restart the explorer process to apply the changes
        os.system('taskkill /f /im explorer.exe')
        os.system('start explorer.exe')
        
        messagebox.showinfo("Windows Tuner", "The default Windows mode has been changed to Dark Mode.")
    except Exception as e:
        messagebox.showerror("Error", f"Error enabling Dark Mode: {e}")

def enable_light_mode():
    try:
        # Modify the Windows registry to enable light mode
        os.system('reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v AppsUseLightTheme /t REG_DWORD /d 1 /f')
        os.system('reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v SystemUsesLightTheme /t REG_DWORD /d 1 /f')
        
        # Restart the explorer process to apply the changes
        os.system('taskkill /f /im explorer.exe')
        os.system('start explorer.exe')
        
        messagebox.showinfo("Windows Tuner", "The default Windows mode has been changed to Light Mode.")
    except Exception as e:
        messagebox.showerror("Error", f"Error enabling Light Mode: {e}")

def take_screenshot():
    try:
        print("Screenshot will be taken in 5 seconds")
        time.sleep(5)  # Wait for 5 seconds before taking the screenshot
        pyautogui.press('printscreen')  # Simulate pressing the "Print Screen" key
        time.sleep(2) 
        messagebox.showinfo("Windows Tuner", "Screenshot has been taken.")
    except Exception as e:
        messagebox.showerror("Error", f"Error taking screenshot: {e}")

def show_help():
    help_message = "Available commands:\n\n"
    help_message += "'dark mode': Change the default Windows mode to Dark Mode.\n"
    help_message += "'light mode': Change the default Windows mode to Light Mode.\n"
    help_message += "'screenshot': Take a screenshot of the desktop.\n"
    help_message += "'help': Show this help message."
    messagebox.showinfo("Windows Tuner Help", help_message)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Windows Tuner")
    root.geometry("400x300")

    def on_command_entry(event=None):
        user_input = command_entry.get()
        if user_input.lower() == "dark mode":
            enable_dark_mode()
        elif user_input.lower() in ["heller modus", "light mode"]:
            enable_light_mode()
        elif user_input.lower() == "screenshot":
            take_screenshot()
        elif user_input.lower() == "help":
            show_help()
        else:
            messagebox.showinfo("Invalid Command", "Invalid command. Type 'help' for available commands.")
        command_entry.delete(0, tk.END)

    welcome_label = tk.Label(root, text="Welcome to the Windows Tuner!", font=("Arial", 16))
    welcome_label.pack(pady=20)

    command_label = tk.Label(root, text="Type a command or 'help' for available commands:", font=("Arial", 12))
    command_label.pack()

    command_entry = tk.Entry(root, font=("Arial", 12))
    command_entry.bind("<Return>", on_command_entry)
    command_entry.pack(pady=10)

    root.mainloop()
