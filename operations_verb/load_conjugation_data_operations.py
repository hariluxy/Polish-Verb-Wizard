"""
    Loads the conjugation dataset.

    The Fast-Conjugation-Dataset contains three rows: Infinitive, First conjugation, Second Conjugation
"""

import os
import csv
import warnings
from pathlib import Path


# Obtain the dataset from any computer. It gets the current directory of the script and navigate to the 'conjugation_dataset' folder
CURRENT_DIR = Path(__file__).parent
CONJUGATION_DATA_PATH = CURRENT_DIR.parent / 'conjugation_dataset' / 'fast_conjugation_data.tab'


# Loads the whole data set into the conjugation dictionary
def load_conjugation_data():
    
    loaded_conjugations = {}

  # Check if the file exists
    if not os.path.exists(CONJUGATION_DATA_PATH):
        warnings.warn(f"Warning: The dataset file '{CONJUGATION_DATA_PATH}' cannot be located.")
        return loaded_conjugations

    try:
        with open(CONJUGATION_DATA_PATH, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter='\t')
            
            for row in reader:
                if len(row) == 3:
                    infinitive, conj1, conj2 = row
                    loaded_conjugations[infinitive] = (conj1, conj2)
    except Exception as e:
        warnings.warn(f"Warning: Failed to load the dataset. Error: {e}")

    return loaded_conjugations


# Retrieves the conjugation for a verb from the conjugation dictionary. (If the verb is not found, return (None, None))
def get_conjugation(verb, loaded_conjugations):
   
    return loaded_conjugations.get(verb, (None, None))
