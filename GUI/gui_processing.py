import tkinter as tk
from tkinter import filedialog

def display_message(self, message):
    """Display a message in the message_display Text widget."""
    self.message_display.config(state='normal')  # Enable editing
    self.message_display.delete(1.0, tk.END)  # Clear previous messages
    self.message_display.insert(tk.END, message)  # Insert the new message
    self.message_display.tag_add("center", 1.0, "end-1c")  # Apply the "center" tag to the text
    self.message_display.config(state='disabled')  # Disable editing

def load_verb_file(self):
    """Allows the user to load a verb .txt file"""
    self.verb_file_path = filedialog.askopenfilename(
        title="Select Verb File",
        filetypes=(("Text Files", "*.txt"),)
    )
    if self.verb_file_path:
        self.display_message("File loaded successfully.\n\nNow choose a folder to save the results")
    else:
        self.display_message("Please select a file.")

def select_save_folder(self):
    """Allows the user to select a folder where results will be saved"""
    self.save_folder_path = filedialog.askdirectory(title="Select Save Folder")
    if self.save_folder_path:
        self.display_message("Folder selected successfully.\n\nYou may generate the results now.")
    else:
        self.display_message("Please select a folder.")
