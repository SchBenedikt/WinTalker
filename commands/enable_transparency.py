import os
import ctypes
from tkinter import messagebox

def enable_transparency():
    try:
        os.system('reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v EnableTransparency /t REG_DWORD /d 1 /f')
        ctypes.windll.user32.SendMessageW(0xFFFF, 0x112, 0xF170, -1) 
        messagebox.showinfo("Windows Talker", "Transparency Effects have been enabled.")
    except Exception as e:
        messagebox.showerror("Error", f"Error enabling Transparency Effects: {e}")
