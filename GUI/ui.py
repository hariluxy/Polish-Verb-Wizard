import tkinter as tk
from .gui_processing import display_message, load_verb_file, select_save_folder
from .ui_main import run_process

class PolishVerbWizard:
    def __init__(self, root):
        self.root = root
        self.root.title("Polish Verb Wizard by Hariluxy")
        
        '''
        # Instructions configured for maximum clarity
        '''
        # Label to highlight "Follow these instructions:"
        self.instructions_title = tk.Label(root, text="Follow these instructions:", font=("Helvetica", 12, "bold"))
        self.instructions_title.grid(row=0, column=0, padx=10, pady=5, columnspan=2, sticky="n")

        # Label for the detailed instructions
        self.load_file_label = tk.Label(root, text="1. Load a file with verbs or enter them manually.\n"
                                                   "2. Choose a folder to save the results.\n"
                                                   "3. Click on 'Generate Results'.",
                                        justify="left")
        self.load_file_label.grid(row=1, column=0, padx=10, pady=5, columnspan=2, sticky="n")

        # Button to load the verb file
        self.load_file_button = tk.Button(root, text="Load file", command=self.load_verb_file)
        self.load_file_button.grid(row=2, column=0, padx=10, pady=10)

        # Entry for manual verb input
        self.verb_entry_label = tk.Label(root, text="You may also enter verbs manually (separated by commas):")
        self.verb_entry_label.grid(row=3, column=0, padx=10, pady=5)
        self.verb_entry = tk.Entry(root, width=50)
        self.verb_entry.grid(row=4, column=0, padx=10, pady=5)

        # Button to select the save folder
        self.save_folder_button = tk.Button(root, text="Select a folder to save", command=self.select_save_folder)
        self.save_folder_button.grid(row=5, column=0, padx=10, pady=10)

        # Button to run the process
        self.run_button = tk.Button(root, text="Generate Results", command=self.run_process)
        self.run_button.grid(row=6, column=0, columnspan=2, pady=20)

        # Text widget for displaying status messages 
        self.message_display = tk.Text(root, height=2, width=40, state='normal', wrap='word')
        self.message_display.grid(row=7, column=0, padx=10, pady=10, columnspan=2, sticky="ew")
        self.message_display.tag_configure("center", justify='center')
        self.display_message("Status Report Screen")

        # Variables to hold file path and save directory
        self.verb_file_path = None
        self.save_folder_path = None

    # Bind methods from processing_operations.py
    def display_message(self, message):
        display_message(self, message)

    def load_verb_file(self):
        load_verb_file(self)

    def select_save_folder(self):
        select_save_folder(self)

    # Bind method from ui_main.py
    def run_process(self):
        run_process(self)

if __name__ == "__main__":
    root = tk.Tk()
    app = PolishVerbWizard(root)
    root.mainloop()
