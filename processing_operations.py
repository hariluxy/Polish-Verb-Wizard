
"""
    Loads the verbs from the input file, It performs the operations with the verbs and saves the results in three formats.

"""

from aspect_sorter_operations import verbs_by_aspect
from load_conjugation_data_operations import load_conjugation_data, get_conjugation
from save_operations import save_all_methods

def process_verbs_and_save(verb_file_path, destination_folder):
  
    # Read verbs from the input file
    with open(verb_file_path, 'r', encoding='utf-8') as file:
        verbs = [line.strip() for line in file.readlines() if line.strip()]

    # Classify the verbs by aspect
    verbs_aspect = verbs_by_aspect(verbs)

    # Load conjugation data
    loaded_conjugations = load_conjugation_data()

    # Obtain the matching conjugation
    verb_conjugation = {verb: get_conjugation(verb, loaded_conjugations) for verb in verbs}

    # Save all three classifications
    save_all_methods(verbs_aspect, verb_conjugation, destination_folder)