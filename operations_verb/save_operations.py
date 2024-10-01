"""
     The saving process takes place here, functions for each method determine the format of the output. 
     
     The saving methods:

        -First Method: The verbs are divided in four categories (Imperfective, Perfective, Both and Unknown) 

        -Second Method: Performs the same action as the previous and adds verb conjugations.

        -Third Method: Provides a SCSV file with this format (verb;aspect;conjugation1;conjugation2) 
         perfect for flashcards or databases.
"""

import os

# Helper function to write verbs to file
def write_verbs(file, verbs, header, loaded_conjugations=None, scsv_format=False, add_newline=True):
    if not scsv_format:  # Only write the header if it's not in SCSV format
        if add_newline:
            file.write(f"\n{header} Verbs:\n")
        else:
            file.write(f"{header} Verbs:\n")  # No newline for the first header
    
    for verb in verbs:
        if loaded_conjugations and verb in loaded_conjugations:
            conj1, conj2 = loaded_conjugations[verb]
            if scsv_format:
                # Write verb in the required SCSV format without any headers
                file.write(f"{verb};{header.lower()};{conj1};{conj2}\n")
            else:
                file.write(f"{verb} - {conj1}, {conj2}\n")
        else:
            if scsv_format:
                # Write verb in SCSV format without conjugations if not found
                file.write(f"{verb};{header.lower()}\n")
            else:
                file.write(f"{verb}\n")


# First method: Saves the verbs classified by aspect.
def save_verb_simple(verbs_aspect, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        write_verbs(file, verbs_aspect["imperfective"], "Imperfective", add_newline=False)  # First section, no newline
        write_verbs(file, verbs_aspect["perfective"], "Perfective")  # Subsequent sections with newline
        write_verbs(file, verbs_aspect["both"], "Both")
        write_verbs(file, verbs_aspect["unknown"], "Unknown")

# Second method: Saves the verbs classified by aspect with their conjugations.
def save_verb_conjugation(verbs_aspect, loaded_conjugations, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        write_verbs(file, verbs_aspect["imperfective"], "Imperfective", loaded_conjugations, add_newline=False)
        write_verbs(file, verbs_aspect["perfective"], "Perfective", loaded_conjugations)
        write_verbs(file, verbs_aspect["both"], "Both", loaded_conjugations)
        write_verbs(file, verbs_aspect["unknown"], "Unknown")

# Third method: Saves the verbs in a SCSV format.
def save_verb_SCSV(verbs_aspect, loaded_conjugations, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        # No headers needed, just write the verbs directly
        write_verbs(file, verbs_aspect["imperfective"], "imperfective", loaded_conjugations, scsv_format=True)
        write_verbs(file, verbs_aspect["perfective"], "perfective", loaded_conjugations, scsv_format=True)
        write_verbs(file, verbs_aspect["both"], "both", loaded_conjugations, scsv_format=True)

# It saves each method in a different file
def save_all_methods(verbs_aspect, loaded_conjugations, destination_folder):
    # Define paths for each output file
    simple_path = os.path.join(destination_folder, '1_verb_simple.txt')
    conjugation_path = os.path.join(destination_folder, '2_verb_conjugation.txt')
    detailed_path = os.path.join(destination_folder, '3_verb_SCSV.txt')

    # Save First Method
    save_verb_simple(verbs_aspect, simple_path)
    
    # Save Second Method
    save_verb_conjugation(verbs_aspect, loaded_conjugations, conjugation_path)

    # Save Third Method
    save_verb_SCSV(verbs_aspect, loaded_conjugations, detailed_path)