import os
import ctypes
from tkinter import messagebox

def disable_transparency():
    try:
        os.system('reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v EnableTransparency /t REG_DWORD /d 0 /f')
        ctypes.windll.user32.SendMessageW(0xFFFF, 0x112, 0xF170, -1)  # Send a WM_SYSCOMMAND message to the active window to disable the transparency effect
        messagebox.showinfo("Windows Talker", "Transparency Effects have been disabled.")
    except Exception as e:
        messagebox.showerror("Error", f"Error disabling Transparency Effects: {e}")