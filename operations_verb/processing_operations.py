
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


def load_verbs_list(verb_input, from_file=True):

    # Load verbs from file file
    if from_file:
        with open(verb_input, 'r', encoding='utf-8') as file:
            verbs = [line.strip() for line in file.readlines() if line.strip()]
    # Load verbs from manual input
    else:
        verbs = verb_input
    
    return verbs


def add_data_verbs(verb_input, destination_folder):

    # Classify the verbs by aspect
    verb_list = verbs_by_aspect(verb_input)

    # Load conjugation data
    loaded_conjugations = load_conjugation_data()

    # Loop over the verbs in the verb_list to update conjugations
    for verb in verb_list:
        # Retrieve conjugation for each verb
        first_conj, third_conj = get_conjugation(verb, loaded_conjugations)

        # Update the verb_list with the conjugations
        verb_list[verb]['first_person_conjugation'] = first_conj
        verb_list[verb]['third_person_conjugation'] = third_conj

     # Save all three classifications
    save_all_methods(verb_list, destination_folder)

   

