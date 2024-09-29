import csv

# Path to your conjugation dataset (make sure this path is correct)
FAST_CONJUGATION_DATA_PATH = 'C:/Users/Raque/Desktop/PGW/Polish-Verb-Wizard/fast_conjugation_data.tab'

def load_fast_conjugation_data():
    """
    Loads the fast conjugation data from the smaller dataset.
    """
    conjugations = {}
    with open(FAST_CONJUGATION_DATA_PATH, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            if len(row) == 3:
                infinitive, conj1, conj2 = row
                conjugations[infinitive] = (conj1, conj2)
    return conjugations

def get_conjugation_from_fast_data(verb, conjugations):
    """
    Retrieves the conjugation for a verb from the fast conjugation dataset.
    If the verb is not found, return (None, None).
    """
    return conjugations.get(verb, (None, None))
