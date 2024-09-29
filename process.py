from classifier import classify_verbs
from conjugation import get_conjugation, load_fast_conjugation_data
from save_utils import save_all_classifications

def process_verbs_and_save(verb_file_path, destination_folder):
    """
    Processes the verbs from the input file and saves the results in three formats.
    :param verb_file_path: Path to the file containing the list of verbs.
    :param destination_folder: Folder where the result files will be saved.
    """
    # Read verbs from the input file
    with open(verb_file_path, 'r', encoding='utf-8') as file:
        verbs = [line.strip() for line in file.readlines() if line.strip()]

    # Classify the verbs
    classified_verbs = classify_verbs(verbs)

    # Load conjugation data
    conjugations = load_fast_conjugation_data()

    # Conjugate the verbs
    verb_conjugations = {verb: get_conjugation(verb, conjugations) for verb in verbs}

    # Save all three classifications
    save_all_classifications(classified_verbs, verb_conjugations, destination_folder)