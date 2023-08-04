import os
from tkinter import messagebox

def enable_dark_mode():
    try:
        # Modify the Windows registry to enable dark mode
        os.system('reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v AppsUseLightTheme /t REG_DWORD /d 0 /f')
        os.system('reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v SystemUsesLightTheme /t REG_DWORD /d 0 /f')
        
        # Restart the explorer process to apply the changes
        os.system('taskkill /f /im explorer.exe')
        os.system('start explorer.exe')
        
        messagebox.showinfo("Windows Talker", "The default Windows mode has been changed to Dark Mode.")
    except Exception as e:
        messagebox.showerror("Error", f"Error enabling Dark Mode: {e}")
