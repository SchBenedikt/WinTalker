import os
from tkinter import messagebox

def enable_light_mode():
    try:
        # Modify the Windows registry to enable light mode
        os.system('reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v AppsUseLightTheme /t REG_DWORD /d 1 /f')
        os.system('reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v SystemUsesLightTheme /t REG_DWORD /d 1 /f')
        
        # Restart the explorer process to apply the changes
        os.system('taskkill /f /im explorer.exe')
        os.system('start explorer.exe')
        
        messagebox.showinfo("Windows Talker", "The default Windows mode has been changed to Light Mode.")
    except Exception as e:
        messagebox.showerror("Error", f"Error enabling Light Mode: {e}")
