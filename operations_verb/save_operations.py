"""
     The saving process takes place here, functions for each method determine the format of the output. 
     
     The saving methods:
        -First Method: The verbs are divided in four categories (Imperfective, Perfective, Both and Unknown) 

        -Second Method: Performs the same action as the previous and adds verb conjugations.

        -Third Method: Provides a SCSV file with this format (verb;aspect;conjugation1;conjugation2) 
         perfect for flashcards or databases.
"""

import os
        
# Write only the verb name for the first method 
def write_simple_method(file, verb_list, header, first_header=True):
    if first_header:
        file.write(f"\n{header} Verbs:\n")
    else:
        file.write(f"{header} Verbs:\n")  # No newline for the first header
    
    for verb in verb_list:
        file.write(f"{verb}\n")

# Write the verb name and conjugation for the second method
def write_conjugation_method(file, verb_list, header, first_header=True):
    if first_header:
        file.write(f"\n{header} Verbs:\n")
    else:
        file.write(f"{header} Verbs:\n")  # No newline for the first header
    
    for verb, data in verb_list.items():
        conj1 = data["first_person_conjugation"]
        conj2 = data["third_person_conjugation"]
        file.write(f"{verb} - {conj1}, {conj2}\n")

# Write the SCSV format for the third method
def write_SCSV_method(file, verb_list):
    for verb, data in verb_list.items():
        conj1 = data["first_person_conjugation"]
        conj2 = data["third_person_conjugation"]
        file.write(f"{verb};{data['aspect']};{conj1};{conj2}\n")

    
# First method: Saves the verbs classified by aspect.
def save_verb_simple(verb_list, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        write_simple_method(file, {k: v for k, v in verb_list.items() if v["aspect"] == "imperfective"}, "Imperfective", first_header=False) 
        write_simple_method(file, {k: v for k, v in verb_list.items() if v["aspect"] == "perfective"}, "Perfective")  
        write_simple_method(file, {k: v for k, v in verb_list.items() if v["aspect"] == "both"}, "Both")
        write_simple_method(file, {k: v for k, v in verb_list.items() if v["aspect"] == "unknown"}, "Unknown")


# Second method: Saves the verbs classified by aspect with their conjugations.
def save_verb_conjugation(verb_list, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        write_conjugation_method(file, {k: v for k, v in verb_list.items() if v["aspect"] == "imperfective"}, "Imperfective", first_header=False)
        write_conjugation_method(file, {k: v for k, v in verb_list.items() if v["aspect"] == "perfective"}, "Perfective")
        write_conjugation_method(file, {k: v for k, v in verb_list.items() if v["aspect"] == "both"}, "Both")


# Third method: Saves the verbs in a SCSV format.
def save_verb_SCSV(verb_list, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        write_SCSV_method(file, {k: v for k, v in verb_list.items() if v["aspect"] == "imperfective"})
        write_SCSV_method(file, {k: v for k, v in verb_list.items() if v["aspect"] == "perfective"})
        write_SCSV_method(file, {k: v for k, v in verb_list.items() if v["aspect"] == "both"})


# It saves each method in a different file
def save_all_methods(verb_list, destination_folder):
    # Define paths for each output file
    simple_path = os.path.join(destination_folder, '1_verb_simple.txt')
    conjugation_path = os.path.join(destination_folder, '2_verb_conjugation.txt')
    detailed_path = os.path.join(destination_folder, '3_verb_SCSV.txt')

    # Save First Method
    save_verb_simple(verb_list, simple_path)
    
    # Save Second Method
    save_verb_conjugation(verb_list, conjugation_path)

    # Save Third Method
    save_verb_SCSV(verb_list, detailed_path)
