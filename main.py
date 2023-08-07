import tkinter as tk
from tkinter import ttk, simpledialog
import sys
sys.path.append('commands')
sys.path.append('commands/open_app')
import dark_mode
import light_mode
import screenshot
import open_word
import open_powerpoint
import open_excel
import open_explorer
import enable_transparency
import disable_transparency 
import open_taskmanager
import system_info
import shutdown
import restart
import webbrowser
import os
import ctypes
from tkinter import messagebox
import threading
import pystray
from PIL import Image


def show_help():
    help_url = "https://github.com/SchBenedikt/WinTalker/wiki/Commands"  # Hier die URL deiner Hilfe-Webseite einfügen
    webbrowser.open(help_url)

# Map command keywords to the corresponding functions
command_map = {
    'dark mode': dark_mode.enable_dark_mode,
    'heller modus': light_mode.enable_light_mode,
    'light mode': light_mode.enable_light_mode,
    'screenshot': screenshot.take_screenshot,
    'system info': system_info.show_system_info,
    'shutdown': shutdown.shutdown_computer,
    'restart': restart.restart_computer,
    'word': open_word.open_microsoft_word,
    'powerpoint': open_powerpoint.open_microsoft_powerpoint,
    'excel': open_excel.open_microsoft_excel,
    'explorer': open_explorer.open_explorer,
    'taskmanager': open_taskmanager.open_windows_taskmanager,
    'transparency on': enable_transparency.enable_transparency,
    'transparency off': disable_transparency.disable_transparency,
    'help': show_help,
}

def execute_command(user_input):
    matched_commands = []
    for command_keyword, command_function in command_map.items():
        # Check if all words in the command_keyword are present in the user input
        if all(word.lower() in user_input.lower() for word in command_keyword.split()):
            matched_commands.append(command_function)
    if len(matched_commands) > 0:
        # If multiple matching commands are found, execute them all
        for command_function in matched_commands:
            command_function()
    else:
        search_query = user_input.replace(' ', '+')
        search_url = f"https://www.google.com/search?q={search_query}"
        open_search_confirmation(search_url)

def open_search_confirmation(search_url):
    # Create a new dialog window to ask for confirmation
    confirmation_dialog = tk.Toplevel(root)
    confirmation_dialog.title("Command Not Found")

    message_label = tk.Label(confirmation_dialog, text="Command not found. Would you like to search online or report this bug on Github?")
    message_label.pack(padx=20, pady=10)

    def perform_search():
        webbrowser.open(search_url)
        confirmation_dialog.destroy()

    def open_specific_website():
        specific_url = "https://github.com/SchBenedikt/WinTalker/issues/new/choose"  # Replace with the URL of the specific website
        webbrowser.open(specific_url)
        confirmation_dialog.destroy()

    def cancel_search():
        confirmation_dialog.destroy()

    search_button = tk.Button(confirmation_dialog, text="Search Online", command=perform_search)
    search_button.pack(side=tk.LEFT, padx=10, pady=10)

    specific_website_button = tk.Button(confirmation_dialog, text="Open Github", command=open_specific_website)
    specific_website_button.pack(side=tk.LEFT, padx=10, pady=10)

    cancel_button = tk.Button(confirmation_dialog, text="Cancel", command=cancel_search)
    cancel_button.pack(side=tk.RIGHT, padx=10, pady=10)

def update_window_size(event=None):
    root.update_idletasks()
    # Calculate window size in percentage of screen size
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width_percent = 30  # Set the width percentage (adjust as needed)
    window_height_percent = 25  # Set the height percentage (adjust as needed)
    window_width = (screen_width * window_width_percent) // 100
    window_height = (screen_height * window_height_percent) // 100
    # Calculate window position so that the window is in the bottom right corner
    window_x = screen_width - window_width -20
    window_y = screen_height - window_height - 90  # Adjust this value to change the vertical position
    # Set the window size and position
    root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
    root.resizable(False, False)  # Disable window resizing
    root.attributes("-topmost", True)  # Make the window always on top

def minimize_to_tray():
    root.withdraw()  # Verstecke das Hauptfenster

def restore_from_tray(icon, item):
    root.deiconify()  # Zeige das Hauptfenster wieder an

def close_application(icon, item):
    tray_icon.stop()  # Stoppe das Tray-Icon
    root.destroy()  # Schließe die Hauptanwendung

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Windows Talker")
    # Call the update_window_size function to set initial window size and make the window immovable and always on top
    update_window_size()
    # Use 'clam' built-in theme
    style = ttk.Style()

    def on_command_entry(event=None):
        user_input = command_entry.get()
        execute_command(user_input)
        command_entry.delete(0, tk.END) 

    welcome_label = tk.Label(root, text="Welcome to the Windows Talker!", font=("Segoe UI", 16, "bold"))
    welcome_label.pack(pady=20)
    welcome_label.bind("<Button-1>", lambda e: webbrowser.open("github.com/SchBenedikt/WinTalker"))
    welcome_label.bind("<Enter>", lambda e: welcome_label.config(cursor="hand2"))
    welcome_label.bind("<Leave>", lambda e: welcome_label.config(cursor=""))
    

    command_label = tk.Label(root, text="Type a command or 'help' for available commands:", font=("Segoe UI", 12))
    command_label.pack()

    command_entry = tk.Entry(root, font=("Segoe UI", 12))
    command_entry.bind("<Return>", on_command_entry)
    command_entry.pack(pady=10)
    command_entry.focus_set()  # Set the focus on the input field


    # Erstelle das Tray-Icon
    icon_image = Image.open("icon.ico")
    tray_icon = pystray.Icon("My App", icon_image, "My App")
    tray_icon.menu = (
        pystray.MenuItem("Restore", restore_from_tray),
        pystray.MenuItem("Minimize", minimize_to_tray),
        pystray.MenuItem("Quit", close_application)
    )

    # Starte das Tray-Icon in einem Thread
    tray_icon_thread = threading.Thread(target=tray_icon.run)
    tray_icon_thread.daemon = True
    tray_icon_thread.start()

    root.protocol("WM_DELETE_WINDOW", minimize_to_tray)

    root.mainloop()
