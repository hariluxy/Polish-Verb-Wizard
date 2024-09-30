import tkinter as tk
from tkinter import filedialog, messagebox
from processing_operations import process_verbs_and_save

class PolishVerbWizard:
    def __init__(self, root):
        self.root = root
        self.root.title("Polish Verb Wizard")

        # Label to load verb file
        self.load_file_label = tk.Label(root, text="First, you must load a .txt file with verbs")
        self.load_file_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Button to load the verb file
        self.load_file_button = tk.Button(root, text="Load file", command=self.load_verb_file)
        self.load_file_button.grid(row=0, column=1, padx=10, pady=10)

        # Label to select the save folder
        self.save_folder_label = tk.Label(root, text="Second, you must select a directory to save the results")
        self.save_folder_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        # Button to select the save folder
        self.save_folder_button = tk.Button(root, text="Select a saving folder", command=self.select_save_folder)
        self.save_folder_button.grid(row=1, column=1, padx=10, pady=10)

        # Button to run the process
        self.run_button = tk.Button(root, text="Generate Results", command=self.run_process)
        self.run_button.grid(row=2, column=0, columnspan=2, pady=20)

        # Variables to hold file path and save directory
        self.verb_file_path = None
        self.save_folder_path = None

    def load_verb_file(self):

        """Allows the user to load a verb .txt file"""
        self.verb_file_path = filedialog.askopenfilename(
            title="Select Verb File",
            filetypes=(("Text Files", "*.txt"),)
        )
        if self.verb_file_path:
            messagebox.showinfo("Success", f"File Loaded Succesfully")
        else:
            messagebox.showwarning("No File", "Please select a file.")

    def select_save_folder(self):

        """Allows the user to select a folder where results will be saved"""
        self.save_folder_path = filedialog.askdirectory(title="Select Save Folder")
        if self.save_folder_path:
            messagebox.showinfo("Success", f"Folder Selected Sucesfully\nYou may generate the results now")
        else:
            messagebox.showwarning("No Folder", "Please select a folder.")

    def run_process(self):
        """Runs the verb processing and saves the results"""
        if not self.verb_file_path:
            messagebox.showerror("Error", "Please load a verb .txt file first.")
            return
        if not self.save_folder_path:
            messagebox.showerror("Error", "Please select a folder to save the results.")
            return

        # Call the processing function with the verb file and save folder
        try:
            process_verbs_and_save(self.verb_file_path, self.save_folder_path)
            messagebox.showinfo("Success", "Results generated and saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Running the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = PolishVerbWizard(root)
    root.mainloop()
