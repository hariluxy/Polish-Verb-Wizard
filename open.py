import csv

def find_present_conjugations(verb_infinitive, file_path):
    first_person = None
    third_person = None
    
    # Open the PoliMorf CSV file
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')  # Assuming tab-delimited format
        
        # Iterate over each row in the dataset
        for row in reader:
            if len(row) >= 4:
                conjugated_form = row[0]
                base_form = row[1]
                morphological_info = row[2]
                part_of_speech = row[3]

                # Present tense, first and third person, singular (pri = 1st person, ter = 3rd person)
                if base_form == verb_infinitive and 'fin' in morphological_info and 'sg' in morphological_info:
                    if 'pri' in morphological_info:
                        first_person = conjugated_form
                    elif 'ter' in morphological_info:
                        third_person = conjugated_form
    
    return first_person, third_person
