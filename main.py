import tkinter as tk
from tkinter import ttk, simpledialog
import platform
import sys
import sv_ttk
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
import open_msedge
import open_chrome
import open_msteams
import restart
import webbrowser
from PIL import Image
import os
import ctypes
import requests
import re
from tkinter import messagebox
import sv_ttk
import tldextract
import threading
import pystray
from datetime import datetime
from datetime import datetime as dt
import pyttsx3
import time
import winsound
import pygame
sys.path.append('commands')
sys.path.append('command_input')
sys.path.append('commands/open_app')


def load_command_map(language):
    command_map = {}
    file_paths = ["command_input/german.txt", "command_input/english.txt"]
    for file_path in file_paths:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:
                    keyword, function_name = line.split(":")
                    command_map[keyword.strip()] = eval(function_name.strip())
    return command_map

# Laden Sie die Befehlszuordnungen für die ausgewählte Sprache
language = "german"  # Oder "english" je nach Bedarf
command_map = load_command_map(language)


def start_timer(duration):
    try:
        duration = int(duration)
        if duration <= 0:
            print("Bitte geben Sie eine positive Zahl für die Dauer des Timers ein.")
            return
        duration *= 60  # Convert minutes to seconds
        print(f"Timer für {duration // 60} Minuten gestartet.")
        time.sleep(duration)
        print("Timer abgelaufen!")
        # Play background music for 5 seconds
        pygame.mixer.init()
        pygame.mixer.music.load("background-music-for-trailer-amp-shorts-184413.mp3")
        pygame.mixer.music.play()
        time.sleep(5)
        pygame.mixer.music.stop()
    except ValueError:
        print("Bitte geben Sie eine gültige Zahl für die Dauer des Timers ein.")


def execute_command(user_input):
    domain = get_domain(user_input)
    if user_input.lower() == "help":
        show_help()
        return

    if domain:
        search_url = f"https://{domain}"
        webbrowser.open(search_url)
    if "timer" in user_input.lower():
        duration = user_input.lower().replace("timer", "").strip()
        start_timer(duration)
    else:
        matched_commands = []
        for command_keyword, command_function in command_map.items():
            if all(word.lower() in user_input.lower() for word in command_keyword.split()):
                matched_commands.append(command_function)
        if len(matched_commands) > 0:
            for command_function in matched_commands:
                command_function()
        else:
            search_query = user_input.replace(' ', '+')
            search_url = f"https://www.google.com/search?q={search_query}"
            open_search_confirmation(search_url)

def get_domain(user_input):
    extracted = tldextract.extract(user_input)
    if extracted.domain and extracted.suffix:
        return f"{extracted.domain}.{extracted.suffix}"
    return None

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
        specific_url = "https://github.com/SchBenedikt/WinTalker/issues/new/choose"
        webbrowser.open(specific_url)
        confirmation_dialog.destroy()

    def cancel_search():
        confirmation_dialog.destroy()

    search_button = ttk.Button(confirmation_dialog, text="Search Online", command=perform_search, style='Modern.TButton')
    search_button.pack(side=tk.LEFT, padx=10, pady=10)

    specific_website_button = ttk.Button(confirmation_dialog, text="Open Github", command=open_specific_website, style='Modern.TButton')
    specific_website_button.pack(side=tk.LEFT, padx=10, pady=10)

    cancel_button = ttk.Button(confirmation_dialog, text="Cancel", command=cancel_search, style='Modern.TButton')
    cancel_button.pack(side=tk.RIGHT, padx=10, pady=10)

def update_window_size(event=None, width_percent=None, height_percent=None):
    root.update_idletasks()
    # Load settings from file
    settings = load_settings_from_file()

    # Get width and height from settings or use default values
    if "width" in settings:
        window_width_percent = int(settings["width"])
    else:
        window_width_percent = 30  # Default width percentage (adjust as needed)

    if "height" in settings:
        window_height_percent = int(settings["height"])
    else:
        window_height_percent = 25  # Default height percentage (adjust as needed)

    # Override with provided values if available
    if width_percent is not None:
        window_width_percent = width_percent

    if height_percent is not None:
        window_height_percent = height_percent

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Check if show_time is False in settings
    if "show_time" in settings and settings["show_time"] == "False":
        window_width_percent = 10  # Set width to 10 if show_time is False
        window_height_percent = 20  # Set height to 20 if show_time is False

    window_width = (screen_width * window_width_percent) // 100
    window_height = (screen_height * window_height_percent) // 100

    # Calculate window position so that the window is in the bottom right corner
    window_x = screen_width - window_width - 20
    window_y = screen_height - window_height - 90  # Adjust this value to change the vertical position

    # Set the window size and position
    root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
    root.resizable(True, True)  # Allow window resizing
    root.attributes("-topmost", True)  # Make the window always on top

def open_settings_window():
    settings_window = tk.Toplevel(root)
    settings_window.title("Settings")

    width_label = tk.Label(settings_window, text="Window Width (% of screen):")
    width_label.grid(row=0, column=0, padx=10, pady=5)
    width_entry = ttk.Entry(settings_window, font=("Segoe UI", 12), style='Modern.TEntry')
    width_entry.grid(row=0, column=1, padx=10, pady=5)

    height_label = tk.Label(settings_window, text="Window Height (% of screen):")
    height_label.grid(row=1, column=0, padx=10, pady=5)
    height_entry = ttk.Entry(settings_window, font=("Segoe UI", 12), style='Modern.TEntry')
    height_entry.grid(row=1, column=1, padx=10, pady=5)

    language_label = tk.Label(settings_window, text="Language:")
    language_label.grid(row=2, column=0, padx=10, pady=5)
    language_var = tk.StringVar(settings_window)
    language_var.set("English")  # Set default language
    language_menu = ttk.Combobox(settings_window, textvariable=language_var, values=["English", "German"])
    language_menu.grid(row=2, column=1, padx=10, pady=5)

    style_label = tk.Label(settings_window, text="Style Mode:")
    style_label.grid(row=3, column=0, padx=10, pady=5)
    style_var = tk.StringVar(settings_window)
    # Default value: system theme
    style_menu = ttk.Combobox(settings_window, textvariable=style_var, values=["dark", "light", "system"])
    style_menu.grid(row=3, column=1, padx=10, pady=5)

    show_time_label = tk.Label(settings_window, text="Show Time:")
    show_time_label.grid(row=4, column=0, padx=10, pady=5)
    show_time_var = tk.BooleanVar(settings_window)
    # Default value: True
    show_time_checkbox = ttk.Checkbutton(settings_window, variable=show_time_var)
    show_time_checkbox.grid(row=4, column=1, padx=10, pady=5)

    save_button = ttk.Button(settings_window, text="Save", command=lambda: save_settings(width_entry.get(), height_entry.get(), language_var.get(), style_var.get(), show_time_var.get()), style='Modern.TButton')
    save_button.grid(row=5, column=0, columnspan=2, pady=10)
    save_button.bind("<Enter>", lambda _: save_button.config(cursor="hand2"))
    save_button.bind("<Leave>", lambda _: save_button.config(cursor=""))

    reset_button = ttk.Button(settings_window, text="Reset", command=reset_settings, style='Modern.TButton')
    reset_button.grid(row=6, column=0, columnspan=2, pady=10)
    reset_button.bind("<Enter>", lambda _: reset_button.config(cursor="X_cursor"))
    reset_button.bind("<Leave>", lambda _: reset_button.config(cursor=""))

    # Load settings from file and populate the entry fields
    settings = load_settings_from_file()
    if "width" in settings:
        width_entry.insert(0, settings["width"])
    if "height" in settings:
        height_entry.insert(0, settings["height"])
    if "language" in settings:
        language_var.set(settings["language"])
    if "style_mode" in settings:
        style_var.set(settings["style_mode"])
    if "show_time" in settings:
        show_time_var.set(settings["show_time"])

def save_settings(width_percent, height_percent, language, style_mode, show_time):
    try:
        if width_percent:
            width_percent = int(width_percent)
            if 0 < width_percent <= 100:
                update_window_size(width_percent=width_percent)
                save_setting_to_file("width", width_percent)
            else:
                messagebox.showerror("Error", "Invalid percentage value for width. Please enter a value between 1 and 100.")

        if height_percent:
            height_percent = int(height_percent)
            if 0 < height_percent <= 100:
                update_window_size(height_percent=height_percent)
                save_setting_to_file("height", height_percent)
            else:
                messagebox.showerror("Error", "Invalid percentage value for height. Please enter a value between 1 and 100.")

        if language:
            save_setting_to_file("language", language)

        save_setting_to_file("style_mode", style_mode)
        save_setting_to_file("show_time", show_time)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

def save_setting_to_file(setting_name, setting_value):
    settings_file_path = "settings.txt"

    try:
        with open(settings_file_path, "r") as file:
            settings = file.readlines()
    except FileNotFoundError:
        settings = []

    with open(settings_file_path, "w") as file:
        setting_found = False
        for line in settings:
            if line.startswith(f"{setting_name}:"):
                file.write(f"{setting_name}: {setting_value}\n")
                setting_found = True
            else:
                file.write(line)

        if not setting_found:
            file.write(f"{setting_name}: {setting_value}\n")

def reset_settings():
    settings_file_path = "settings.txt"
    try:
        os.remove(settings_file_path)
        messagebox.showinfo("Reset", "Settings reset successfully.")
    except FileNotFoundError:
        messagebox.showinfo("Reset", "No settings file found.")

def load_settings_from_file():
    settings_file_path = "settings.txt"
    settings = {}

    try:
        with open(settings_file_path, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    key, value = line.split(":")
                    settings[key.strip()] = value.strip()
    except FileNotFoundError:
        # Wenn die Datei nicht gefunden wird, füge die Standardwerte hinzu
        settings["show_time"] = "True"
        settings["style_mode"] = "system"  # Hier setzen wir den Standardwert für style_mode

    # Falls die Einstellung show_time nicht vorhanden ist, füge sie hinzu und speichere sie
    if "show_time" not in settings:
        settings["show_time"] = "True"
        save_setting_to_file("show_time", "True")

    # Falls die Einstellung style_mode nicht vorhanden ist, füge sie hinzu und speichere sie
    if "style_mode" not in settings:
        settings["style_mode"] = "system"  # Hier setzen wir den Standardwert für style_mode
        save_setting_to_file("style_mode", "system")

    return settings


def update_time_label():
    current_time = datetime.now()
    settings = load_settings_from_file()
    if "language" in settings and settings["language"] == "German":
        formatted_time = current_time.strftime("%d.%m.%Y %H:%M:%S")
    else:
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    if "show_time" in settings and settings["show_time"] == "False":
        formatted_time = ""
    time_label.config(text=formatted_time)
    root.after(1000, update_time_label)  # Update the time label every 1000 ms (1 second)

def minimize_to_tray():
    root.withdraw()  # Verstecke das Hauptfenster

def restore_from_tray(icon, item):
    root.deiconify()  # Zeige das Hauptfenster wieder an

def close_application(icon, item):
    tray_icon.stop()  # Stoppe das Tray-Icon
    root.destroy()  # Schließe die Hauptanwendung

def help():
    help_url = "https://github.com/SchBenedikt/WinTalker"
    webbrowser.open(help_url)
def detect_system_theme():
    if platform.system() == "Windows":
        registry_key = r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"
        try:
            import winreg
            reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, registry_key)
            value, _ = winreg.QueryValueEx(reg_key, "AppsUseLightTheme")
            return "light" if value == 1 else "dark"
        except FileNotFoundError:
            # Falls der Registrierungsschlüssel nicht gefunden wird, nehme den dunklen Modus als Standard
            return "dark"
        except Exception as e:
            print("Fehler beim Zugriff auf die Registrierung:", e)
            return "dark"
    elif platform.system() == "Darwin":
        try:
            result = os.popen('defaults read -g AppleInterfaceStyle').read()
            if "Dark" in result:
                return "dark"
            else:
                return "light"
        except Exception as e:
            print("Fehler beim Zugriff auf die macOS-Einstellungen:", e)
            return "dark"
    else:
        # Fallback: Verwende den dunklen Modus für andere Betriebssysteme
        return "dark"
def apply_theme():
    # Load settings from file
    settings = load_settings_from_file()
    
    if "style_mode" in settings:
        if settings["style_mode"] == "system":
            # Überprüfe das Systemthema und wähle entsprechend den Dunkel- oder Hellmodus aus
            system_theme = detect_system_theme()
            if system_theme == "dark":
                sv_ttk.set_theme("dark")
            else:
                sv_ttk.set_theme("light")
        elif settings["style_mode"] == "dark":
            sv_ttk.set_theme("dark")
        else:
            sv_ttk.set_theme("light")
    else:
        # Fallback: Verwende das Dunkelmodus-Theme
        sv_ttk.set_theme("dark")

    # Refresh the GUI to apply the theme changes
    root.update_idletasks()


def watch_settings():
    while True:
        apply_theme()
        time.sleep(1)  # Überprüfe die Einstellungen alle 5 Sekunden

if __name__ == "__main__":
    root = tk.Tk()

    root.title("Windows Talker")
    # Call the update_window_size function to set initial window size and make the window immovable and always on top
    update_window_size()
    
    # Apply theme based on settings
    apply_theme()

    # Set window transparency
    root.attributes("-alpha", 1)  # Set transparency level (0.0 - fully transparent, 1.0 - fully opaque)
    
    # Start the settings watcher thread
    settings_watcher_thread = threading.Thread(target=watch_settings)
    settings_watcher_thread.daemon = True
    settings_watcher_thread.start()

    # Load settings from file
    settings = load_settings_from_file()
    if "show_time" in settings and settings["show_time"] == "True":
        new_label = tk.Label(root, text="")
        new_label.pack()
        time_label = tk.Label(root, text="", font=("Segoe UI", 20))
        time_label.pack()

    # Add a new line here
    new_label = tk.Label(root, text="")
    new_label.pack()

    update_time_label_thread = threading.Thread(target=update_time_label)
    update_time_label_thread.daemon = True
    update_time_label_thread.start()

    # command_label = tk.Label(root, text="Type a command or 'help' for available commands:", font=("Segoe UI", 12))
    # command_label.pack()

    command_entry = ttk.Entry(root, font=("Segoe UI", 12), style='Modern.TEntry')
    command_entry.bind("<Return>", lambda event: execute_command(command_entry.get()))
    command_entry.pack(pady=10)
    command_entry.focus_set()  # Set the focus on the input field

    execute_button = ttk.Button(root, text="Execute", command=lambda: execute_command(command_entry.get()), style='Modern.TButton')
    execute_button.pack(pady=10)
    execute_button.bind("<Enter>", lambda _: execute_button.config(cursor="hand2"))
    execute_button.bind("<Leave>", lambda _: execute_button.config(cursor=""))
    execute_button.config(width=15, style='Modern.TButton')
    settings_button = ttk.Button(root, text="Settings", command=open_settings_window, style='Modern.TButton')
    settings_button.pack(pady=10)

    icon_image = Image.open("icon.ico")
    tray_icon = pystray.Icon("Windows Talker", icon_image, "Windows Talker")
    tray_icon.menu = (
        pystray.MenuItem("Restore", restore_from_tray),
        pystray.MenuItem("Minimize", minimize_to_tray),
        pystray.MenuItem("Quit", close_application),
        pystray.MenuItem("Help", help)

    )

    tray_icon_thread = threading.Thread(target=tray_icon.run)
    tray_icon_thread.daemon = True
    tray_icon_thread.start()

    root.protocol("WM_DELETE_WINDOW", minimize_to_tray)

    root.mainloop()
