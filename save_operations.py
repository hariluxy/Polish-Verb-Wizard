"""
     The saving process takes place here, functions for each method determine the format of the output. 
     
     The saving methods:

        -First Method: The verbs are divided in four categories (Imperfective, Perfective, Both and Unknown) 

        -Second Method: Performs the same action as the previous and adds verb conjugations.

        -Third Method: Provides a SCSV file with this format (verb;aspect;conjugation1;conjugation2) 
         perfect for flashcards or databases.
"""

import os


    
# First method: Saves the verbs classified by aspect.

def save_verb_simple(verbs_aspect, file_path):
  
    with open(file_path, 'w', encoding='utf-8') as file:

        # Imperfective list
        file.write("Imperfective Verbs:\n")
        for verb in verbs_aspect["imperfective"]:
            file.write(f"{verb}\n")

        # Perfective list
        file.write("\nPerfective Verbs:\n")
        for verb in verbs_aspect["perfective"]:
            file.write(f"{verb}\n")

        # Both imperfective and perfective list
        file.write("\nBoth Verbs:\n")
        for verb in verbs_aspect["both"]:
            file.write(f"{verb}\n")
        
        # Unknown or not recognized list
        file.write("\nUnknown Verbs:\n")
        for verb in verbs_aspect["unknown"]:
            file.write(f"{verb}\n")


# Second method: Saves the verbs classified by aspect with their conjugations.
    #Format: verb - 1st_person_singular, 3rd_person_singular

def save_verb_conjugation(verbs_aspect, loaded_conjugations, file_path):
    
    with open(file_path, 'w', encoding='utf-8') as file:

        # Imperfective list
        file.write("Imperfective Verbs:\n")
        for verb in verbs_aspect["imperfective"]:
            if verb in loaded_conjugations:
                conj1, conj2 = loaded_conjugations[verb]
                file.write(f"{verb} - {conj1}, {conj2}\n")
            else:
                file.write(f"{verb}\n")
        
        # Perfective list
        file.write("\nPerfective Verbs:\n")
        for verb in verbs_aspect["perfective"]:
            if verb in loaded_conjugations:
                conj1, conj2 = loaded_conjugations[verb]
                file.write(f"{verb} - {conj1}, {conj2}\n")
            else:
                file.write(f"{verb}\n")
        
        # Both imperfective and perfective list
        file.write("\nBoth Verbs:\n")
        for verb in verbs_aspect["both"]:
            if verb in loaded_conjugations:
                conj1, conj2 = loaded_conjugations[verb]
                file.write(f"{verb} - {conj1}, {conj2}\n")
            else:
                file.write(f"{verb}\n")
        
         # Unknown or not recognized list (No conjugations included in this list)
        file.write("\nUnknown Verbs:\n")
        for verb in verbs_aspect["unknown"]:
            file.write(f"{verb}\n")

 #Third method: Saves the verbs in a SCSV format:
    #Format: verb;aspect;1st_person_singular;3rd_person_singular

def save_verb_SCSV(verbs_aspect, loaded_conjugations, file_path):
    
    with open(file_path, 'w', encoding='utf-8') as file:

        # Imperfective list
        for verb in verbs_aspect["imperfective"]:
            if verb in loaded_conjugations:
                conj1, conj2 = loaded_conjugations[verb]
                file.write(f"{verb};imperfective;{conj1};{conj2}\n")
            else:
                file.write(f"{verb};imperfective\n")
        
        # Perfective list
        for verb in verbs_aspect["perfective"]:
            if verb in loaded_conjugations:
                conj1, conj2 = loaded_conjugations[verb]
                file.write(f"{verb};perfective;{conj1};{conj2}\n")
            else:
                file.write(f"{verb};perfective\n")
        
        ## Both imperfective and perfective list
        for verb in verbs_aspect["both"]:
            if verb in loaded_conjugations:
                conj1, conj2 = loaded_conjugations[verb]
                file.write(f"{verb};both;{conj1};{conj2}\n")
            else:
                file.write(f"{verb};both\n")

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

