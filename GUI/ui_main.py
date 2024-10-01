import sys
import os

# Adjust sys.path to include the parent directory where operations_verb is located
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))  # Go up one directory
sys.path.insert(0, parent_dir)

from operations_verb.processing_operations import load_verbs_list, add_data_verbs
from operations_verb.save_operations import save_all_methods

def run_process(self):
    """Runs the verb processing and saves the results."""
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
            verb_list = load_verbs_list(verbs, from_file=False)
            verbs_To_Save = add_data_verbs(verb_list)
            save_all_methods(verbs_To_Save, self.save_folder_path)
            self.display_message("Results from manual input generated and saved successfully.")
        else:  # Verbs from file
            verb_list = load_verbs_list(self.verb_file_path, from_file=True)
            verbs_To_Save = add_data_verbs(verb_list)
            save_all_methods(verbs_To_Save, self.save_folder_path)
            self.display_message("Results generated and saved successfully.")

    except Exception as e:
        self.display_message(f"An error occurred: {e}")
