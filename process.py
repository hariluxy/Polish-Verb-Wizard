from classifier import classify_verbs
from conjugation import load_fast_conjugation_data, get_conjugation_from_fast_data
from save_utils import save_results

def process_verbs(input_file, output_file, include_conjugations):
    """
    Processes verbs from the input file, classifies them, and optionally adds conjugations.
    
    Saves the results to the output file.
    """
    # Load the fast conjugation dataset
    fast_conjugations = load_fast_conjugation_data()

    # Read verbs from input file
    with open(input_file, 'r', encoding='utf-8') as file:
        verb_list = [line.strip() for line in file.readlines()]

    # Classify the verbs using the classify_verbs function
    classified_verbs = classify_verbs(verb_list)

    conjugations = {}

    # Add conjugations for each verb if the box was checked
    if include_conjugations:
        for verb in verb_list:
            conj1, conj2 = get_conjugation_from_fast_data(verb, fast_conjugations)
            conjugations[verb] = (conj1, conj2)

    # Save the results
    save_results(classified_verbs, conjugations, output_file, include_conjugations)
