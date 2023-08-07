import platform
import tkinter as tk
from tkinter import messagebox
import psutil
import threading
import os
import time

def show_system_info():
    memory = psutil.virtual_memory()
    system_info = f"Operating System: {platform.system()}\n"
    system_info += f"Release Version: {platform.release()}\n"
    system_info += f"Processor: {platform.processor()}\n"

    memory_info = f"Total RAM: {round(memory.total / (1024. ** 3), 2)} GB\n"
    memory_info += f"Percentage Used: {memory.percent}%\n"
    memory_info += f"Used RAM: {round(memory.used / (1024. ** 3), 2)} GB\n"
    memory_info += f"Available RAM: {round(memory.available / (1024. ** 3), 2)} GB\n\n"

    memory_info += f"Total Storage: {round(psutil.disk_usage('/').total / (1024. ** 3), 2)} GB\n"
    memory_info += f"Percentage Used: {psutil.disk_usage('/').percent}%\n"
    memory_info += f"Used Storage: {round(psutil.disk_usage('/').used / (1024. ** 3), 2)} GB\n"
    memory_info += f"Available Storage: {round(psutil.disk_usage('/').free / (1024. ** 3), 2)} GB\n"

    info_text = f"{system_info}\n{memory_info}"
    messagebox.showinfo("System and Memory Information", info_text)