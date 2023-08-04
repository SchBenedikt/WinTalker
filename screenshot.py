import pyautogui
import time
from tkinter import messagebox

def take_screenshot():
    try:
        print("Screenshot will be taken in 5 seconds")
        time.sleep(5)  # Wait for 5 seconds before taking the screenshot
        pyautogui.press('printscreen')  # Simulate pressing the "Print Screen" key
        time.sleep(2) 
        messagebox.showinfo("Windows Talker", "Screenshot has been taken.")
    except Exception as e:
        messagebox.showerror("Error", f"Error taking screenshot: {e}")
