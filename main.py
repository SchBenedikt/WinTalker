import tkinter as tk
from tkinter import simpledialog
import dark_mode
import light_mode
import screenshot
import open_word

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Windows Tuner")
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

    root.mainloop()
