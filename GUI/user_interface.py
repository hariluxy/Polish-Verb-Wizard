import tkinter as tk
from tkinter import filedialog, messagebox
from operations.processing_operations import process_verbs_and_save

class PolishVerbWizard:
    def __init__(self, root):
        self.root = root
        self.root.title("Polish Verb Wizard")

        # Instructions label
        self.load_file_label = tk.Label(root, text="Follow these instructions:\n1-Load a file with verbs.\n2-Choose a folder to save the results.\n3-Click on generate results.")
        self.load_file_label.grid(row=0, column=0, padx=10, pady=10, sticky="n")

        # Button to load the verb file
        self.load_file_button = tk.Button(root, text="Load file", command=self.load_verb_file)
        self.load_file_button.grid(row=1, column=0, padx=10, pady=10)

        # Button to select the save folder
        self.save_folder_button = tk.Button(root, text="Select a folder to save", command=self.select_save_folder)
        self.save_folder_button.grid(row=3, column=0, padx=10, pady=10)

        # Button to run the process
        self.run_button = tk.Button(root, text="Generate Results", command=self.run_process)
        self.run_button.grid(row=4, column=0, columnspan=2, pady=20)

        # Text widget for displaying messages
        self.message_display = tk.Text(root, height=5, width=50, state='disabled')
        self.message_display.grid(row=5, column=0, padx=10, pady=10)

        # Variables to hold file path and save directory
        self.verb_file_path = None
        self.save_folder_path = None

    # Updates the text widget when necesarry
    def display_message(self, message):
        """Display a message in the message_display Text widget."""
        self.message_display.config(state='normal')  # Enable editing the text widget
        self.message_display.delete(1.0, tk.END)  # Clear previous messages
        self.message_display.insert(tk.END, message)  # Insert the new message
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

    def run_process(self):
        """Runs the verb processing and saves the results"""
        if not self.verb_file_path:
            self.display_message("Error: Please load a verb .txt file first.")
            return
        if not self.save_folder_path:
            self.display_message("Error: Please select a folder to save the results.")
            return

        # Call the processing function with the verb file and save folder
        try:
            process_verbs_and_save(self.verb_file_path, self.save_folder_path)
            self.display_message("Results generated and saved successfully.")
        except Exception as e:
            self.display_message(f"An error occurred: {e}")

# Running the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = PolishVerbWizard(root)
    root.mainloop()
