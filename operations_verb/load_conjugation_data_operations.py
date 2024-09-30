"""
    Loads the conjugation dataset.

    The Fast-Conjugation-Dataset contains three rows: Infinitive, First conjugation, Second Conjugation
"""

import csv


# Path to conjugation dataset 
CONJUGATION_DATA_PATH = 'C:/Users/Raque/Desktop/PGW/Polish-Verb-Wizard/conjugation_dataset/fast_conjugation_data.tab'


# Loads the whole data set into the conjugation dictionary

def load_conjugation_data():
    
    loaded_conjugations = {}

    with open(CONJUGATION_DATA_PATH, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        
        for row in reader:
            if len(row) == 3:
                infinitive, conj1, conj2 = row
                loaded_conjugations[infinitive] = (conj1, conj2)

    return loaded_conjugations

# Retrieves the conjugation for a verb from the conjugation dictionary. (If the verb is not found, return (None, None))

def get_conjugation(verb, loaded_conjugations):
   
    return loaded_conjugations.get(verb, (None, None))
