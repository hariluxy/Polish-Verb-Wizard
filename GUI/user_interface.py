import tkinter as tk
from tkinter import filedialog
from operations_verb.processing_operations import process_verbs_and_save

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

    # Updates the text widget when necesarry
    def display_message(self, message):

        #Display a message in the message_display Text widget.
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

    def run_process(self):

        #Runs the verb processing and saves the results
        manual_verbs = self.verb_entry.get().strip()

        if not self.verb_file_path and not manual_verbs:
            self.display_message("Error: Please load a verb file or enter verbs manually.")
            return

        if not self.save_folder_path:
            self.display_message("Error: Please select a folder to save the results.")
            return

        # Process verbs from the manual input or file
        try:
            # Verbs manually introduced
            if manual_verbs:
                verbs = [verb.strip() for verb in manual_verbs.split(',')]
                process_verbs_and_save(verbs, self.save_folder_path, from_file=False)
                self.display_message("Results from manual input generated and saved successfully.")
            else: # Verbs from file
                process_verbs_and_save(self.verb_file_path, self.save_folder_path, from_file=True)
                self.display_message("Results generated and saved successfully.")

        except Exception as e:
            self.display_message(f"An error occurred: {e}")


# Running the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = PolishVerbWizard(root)
    root.mainloop()
