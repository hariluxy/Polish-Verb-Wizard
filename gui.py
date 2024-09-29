from tkinter import *
from tkinter import filedialog
from process import process_verbs  # Import process_verbs from process.py
import os

class PolishVerbWizard:
    def __init__(self, window):
        self.window = window
        self.window.title("Polish Verb Wizard")

        # Variables
        self.input_file = None
        self.output_file = None
        self.include_conjugations = BooleanVar()

        # GUI Elements
        Label(window, text="Polish Verb Wizard").pack()

        # Load file button
        Button(window, text="Load Verbs (.txt)", command=self.load_file).pack()

        # Save file button
        Button(window, text="Destination Folder", command=self.save_file).pack()

        # Checkbox for conjugations
        self.conjugation_checkbox = Checkbutton(window, text="Include Conjugations", variable=self.include_conjugations)
        self.conjugation_checkbox.pack()

        # Run button
        Button(window, text="Run", command=self.run_classification).pack()

    def load_file(self):
        """
        Opens a dialog to load a file containing the list of verbs.
        """
        self.input_file = filedialog.askopenfilename(title="Select Verbs File", filetypes=[("Text Files", "*.txt")])
        if self.input_file:
            print(f"Loaded file: {self.input_file}")

    def save_file(self):
        """
        Opens a dialog to choose where to save the result file.
        """
        self.output_file = filedialog.asksaveasfilename(title="Select Location to Save Results", defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if self.output_file:
            print(f"Saving results to: {self.output_file}")

    def run_classification(self):
        """
        Runs the verb classification process, using morfeusz2 for classification and 
        adding conjugations if the checkbox is selected.
        """
        if not self.input_file or not self.output_file:
            print("Please select both input and output files.")
            return
        
        include_conjugations = self.include_conjugations.get()
        process_verbs(self.input_file, self.output_file, include_conjugations)
        print("Classification completed and results saved.")
