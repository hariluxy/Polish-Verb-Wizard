import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
from classifier import classify_verbs  # Assuming the classifier function is in classifier.py
from conjugation import find_present_conjugations  # Import the conjugation function from open.py

class VerbClassifierGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Polish Verb Wizard 2.0")
        
        # Variable to store the conjugation checkbox value
        self.include_conjugations = tk.BooleanVar()
        
        self.load_button = tk.Button(self.root, text="Load Verbs", command=self.load_verbs)
        self.load_button.pack()

        self.classify_button = tk.Button(self.root, text="Classify Verbs", command=self.classify_verbs)
        self.classify_button.pack()

        self.save_button = tk.Button(self.root, text="Save Results", command=self.save_results)
        self.save_button.pack()
        
        # Checkbox for conjugation analysis
        self.conjugation_checkbox = tk.Checkbutton(self.root, text="Include Conjugations", variable=self.include_conjugations)
        self.conjugation_checkbox.pack()

        self.verb_list = None
        self.classification_results = None
        self.conjugation_results = {}
        
        # Path to the PoliMorf conjugation file (assumes it's in the program's directory)
        self.conjugation_file_path = os.path.join(os.path.dirname(__file__), "PoliMorf-0.6.7.tab")

    def load_verbs(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.verb_list = file.read().splitlines()
            messagebox.showinfo("Info", "Verbs have been loaded successfully.")

    def classify_verbs(self):
        if self.verb_list is None:
            messagebox.showwarning("Warning", "Please load verbs before classifying.")
            return

        self.classification_results = classify_verbs(self.verb_list)

        # If the conjugation checkbox is checked, perform conjugation analysis
        if self.include_conjugations.get():
            if os.path.exists(self.conjugation_file_path):
                for verb in self.verb_list:
                    first_person, third_person = find_present_conjugations(verb, self.conjugation_file_path)
                    if first_person and third_person:
                        self.conjugation_results[verb] = (first_person, third_person)
                    else:
                        self.conjugation_results[verb] = ("N/A", "N/A")
            else:
                messagebox.showwarning("Warning", f"Conjugation data file not found: {self.conjugation_file_path}")
                return

        messagebox.showinfo("Info", "Verbs have been classified successfully.")

    def save_results(self):
        if self.classification_results is None:
            messagebox.showwarning("Warning", "Please classify verbs before saving.")
            return

        save_path = filedialog.askdirectory()
        if save_path:
            result_file_path = os.path.join(save_path, "results.txt")
            with open(result_file_path, 'w', encoding='utf-8') as result_file:
                for aspect, verbs in self.classification_results.items():
                    result_file.write(f"{aspect.capitalize()} Verbs:\n")
                    for verb in verbs:
                        result_file.write(f"{verb}")
                        
                        # Provide conjugation data only for non-unknown aspects
                        if aspect != "unknown" and self.include_conjugations.get() and verb in self.conjugation_results:
                            first_person, third_person = self.conjugation_results[verb]
                            # Only write conjugation if it's available
                            if first_person != "N/A" and third_person != "N/A":
                                result_file.write(f" - {first_person}, {third_person}\n")
                            else:
                                result_file.write("\n")  # No conjugation available
                        else:
                            result_file.write("\n")  # If the verb is in "Unknown" or no conjugation needed
                        
                    result_file.write("\n")

        messagebox.showinfo("Info", f"Results have been saved to {result_file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VerbClassifierGUI(root)
    root.mainloop()
