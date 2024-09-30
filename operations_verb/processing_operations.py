
"""
    Loads the verbs from the input file, It performs the operations with the verbs and saves the results in three formats.

"""

from operations_verb.aspect_sorter_operations import verbs_by_aspect
from operations_verb.load_conjugation_data_operations import load_conjugation_data, get_conjugation
from operations_verb.save_operations import save_all_methods

"""
Process verbs either from a file or a manually provided list.
    
Parameters:
    - verb_input: Either a file path (if from_file=True) or a list of verbs.
    - destination_folder: The folder where results will be saved.
    - from_file: Whether the input is a file or a list of verbs.
"""
def process_verbs_and_save(verb_input, destination_folder, from_file=True):
  
    # Read verbs from the input file or use the provided list
    if from_file:
        with open(verb_input, 'r', encoding='utf-8') as file:
            verbs = [line.strip() for line in file.readlines() if line.strip()]
    else:
        verbs = verb_input

    # Classify the verbs by aspect
    verbs_aspect = verbs_by_aspect(verbs)

    # Load conjugation data
    loaded_conjugations = load_conjugation_data()

    # Obtain the matching conjugation
    verb_conjugation = {verb: get_conjugation(verb, loaded_conjugations) for verb in verbs}

    # Save all three classifications
    save_all_methods(verbs_aspect, verb_conjugation, destination_folder)