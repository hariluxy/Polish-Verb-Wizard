import csv

def find_present_conjugations(verb_infinitive, file_path):
    first_person = None
    third_person = None
    
    # Open the CSV file (assuming your data is in a similar CSV format)
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')  # Assuming the file is tab-delimited
        
        # Iterate over each row in the dataset
        for row in reader:
            # Check if the row has at least 4 elements
            if len(row) >= 4:
                conjugated_form = row[0]
                base_form = row[1]
                morphological_info = row[2]
                part_of_speech = row[3]
                
                # We are only interested in present tense, first and third person, singular
                if base_form == verb_infinitive and 'fin' in morphological_info and 'sg' in morphological_info:
                    # Check for 1st person singular (pri) and 3rd person singular (ter)
                    if 'pri' in morphological_info:
                        first_person = conjugated_form
                    elif 'ter' in morphological_info:
                        third_person = conjugated_form
    
    return first_person, third_person

# Example usage
verb_infinitive = "przekraczać"  # Provide the infinitive verb
file_path = "PoliMorf-0.6.7.tab"  # Path to the file containing your verb data

first_person, third_person = find_present_conjugations(verb_infinitive, file_path)

# Display the conjugations in the requested format
if first_person and third_person:
    print(f"{verb_infinitive.capitalize()} - {first_person.capitalize()}, {third_person.capitalize()}")
else:
    print("No conjugations found for the given criteria.")
