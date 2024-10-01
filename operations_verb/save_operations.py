"""
     The saving process takes place here, functions for each method determine the format of the output. 
     
     The saving methods:

        -First Method: The verbs are divided in four categories (Imperfective, Perfective, Both and Unknown) 

        -Second Method: Performs the same action as the previous and adds verb conjugations.

        -Third Method: Provides a SCSV file with this format (verb;aspect;conjugation1;conjugation2) 
         perfect for flashcards or databases.
"""

import os


def write_verbs(file, verbs, header, conjugation_format=False, scsv_format=False, add_newline=True):
    if not scsv_format:  # Only write the header if it's not in SCSV format
        if add_newline:
            file.write(f"\n{header} Verbs:\n")
        else:
            file.write(f"{header} Verbs:\n")  # No newline for the first header
    
    for verb, data in verbs.items():
        conj1 = data["first_person_conjugation"]
        conj2 = data["third_person_conjugation"]

        # Write verb in the required SCSV format
        if scsv_format:
            file.write(f"{verb};{data['aspect']};{conj1};{conj2}\n")
        # Write in simple format with conjugations
        elif conjugation_format:
            file.write(f"{verb} - {conj1}, {conj2}\n")
        # Write only the verb name for the simple method 
        else:
            file.write(f"{verb}\n")


# First method: Saves the verbs classified by aspect.
def save_verb_simple(verb_list, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        write_verbs(file, {k: v for k, v in verb_list.items() if v["aspect"] == "imperfective"}, "Imperfective", add_newline=False) 
        write_verbs(file, {k: v for k, v in verb_list.items() if v["aspect"] == "perfective"}, "Perfective")  
        write_verbs(file, {k: v for k, v in verb_list.items() if v["aspect"] == "both"}, "Both")
        write_verbs(file, {k: v for k, v in verb_list.items() if v["aspect"] == "unknown"}, "Unknown")


# Second method: Saves the verbs classified by aspect with their conjugations.
def save_verb_conjugation(verb_list, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        write_verbs(file, {k: v for k, v in verb_list.items() if v["aspect"] == "imperfective"}, "Imperfective",conjugation_format=True, add_newline=False)
        write_verbs(file, {k: v for k, v in verb_list.items() if v["aspect"] == "perfective"}, "Perfective", conjugation_format=True)
        write_verbs(file, {k: v for k, v in verb_list.items() if v["aspect"] == "both"}, "Both", conjugation_format=True)


# Third method: Saves the verbs in a SCSV format.
def save_verb_SCSV(verb_list, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        # No headers needed, just write the verbs directly
        write_verbs(file, {k: v for k, v in verb_list.items() if v["aspect"] == "imperfective"}, "imperfective", scsv_format=True)
        write_verbs(file, {k: v for k, v in verb_list.items() if v["aspect"] == "perfective"}, "perfective", scsv_format=True)
        write_verbs(file, {k: v for k, v in verb_list.items() if v["aspect"] == "both"}, "both", scsv_format=True)


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
