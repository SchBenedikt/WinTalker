import tkinter as tk
import sys
from tkinter import simpledialog
sys.path.append('commands')
sys.path.append('commands/open_app')
import dark_mode
import light_mode
import screenshot
import open_word
import open_powerpoint
import open_excel

def show_help():
    help_message = "Available commands:\n\n"
    help_message += "'dark mode': Change the default Windows mode to Dark Mode.\n"
    help_message += "'light mode': Change the default Windows mode to Light Mode.\n"
    help_message += "'screenshot': Take a screenshot of the desktop.\n"
    help_message += "'word': Open Microsoft Word.\n"
    help_message += "'help': Show this help message."
    tk.messagebox.showinfo("Windows Talker Help", help_message)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Windows Talker")
    root.geometry("400x300")

    def on_command_entry(event=None):
        user_input = command_entry.get()
        if user_input.lower() == "dark mode":
            dark_mode.enable_dark_mode()
        elif user_input.lower() in ["heller modus", "light mode"]:
            light_mode.enable_light_mode()
        elif user_input.lower() == "screenshot":
            screenshot.take_screenshot()
        elif user_input.lower() == "word":
            open_word.open_microsoft_word()
        elif user_input.lower() == "powerpoint":
            open_powerpoint.open_microsoft_powerpoint()
        elif user_input.lower() == "excel":
            open_excel.open_microsoft_excel()
        elif user_input.lower() == "help":
            show_help()
        else:
            tk.messagebox.showinfo("Invalid Command", "Invalid command. Type 'help' for available commands.")
        command_entry.delete(0, tk.END)

    welcome_label = tk.Label(root, text="Welcome to the Windows Talker!", font=("Arial", 16))
    welcome_label.pack(pady=20)

    command_label = tk.Label(root, text="Type a command or 'help' for available commands:", font=("Arial", 12))
    command_label.pack()

    command_entry = tk.Entry(root, font=("Arial", 12))
    command_entry.bind("<Return>", on_command_entry)
    command_entry.pack(pady=10)

    command_entry.focus_set()  # Setze den Fokus auf das Eingabefeld

    root.mainloop()
