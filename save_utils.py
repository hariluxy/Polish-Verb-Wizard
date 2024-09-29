import os

def save_simple_classification(classified_verbs, file_path):
    """
    First method: Saves the verbs classified by aspect without conjugations.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("Imperfective Verbs:\n")
        for verb in classified_verbs["imperfective"]:
            file.write(f"{verb}\n")
        
        file.write("\nPerfective Verbs:\n")
        for verb in classified_verbs["perfective"]:
            file.write(f"{verb}\n")
        
        file.write("\nBoth Verbs:\n")
        for verb in classified_verbs["both"]:
            file.write(f"{verb}\n")
        
        file.write("\nUnknown Verbs:\n")
        for verb in classified_verbs["unknown"]:
            file.write(f"{verb}\n")


def save_conjugation_classification(classified_verbs, conjugations, file_path):
    """
    Second method: Saves the verbs classified by aspect with their conjugations.
    Format: verb - 1st_person_singular, 3rd_person_singular
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("Imperfective Verbs:\n")
        for verb in classified_verbs["imperfective"]:
            if verb in conjugations:
                conj1, conj2 = conjugations[verb]
                file.write(f"{verb} - {conj1}, {conj2}\n")
            else:
                file.write(f"{verb}\n")
        
        file.write("\nPerfective Verbs:\n")
        for verb in classified_verbs["perfective"]:
            if verb in conjugations:
                conj1, conj2 = conjugations[verb]
                file.write(f"{verb} - {conj1}, {conj2}\n")
            else:
                file.write(f"{verb}\n")
        
        file.write("\nBoth Verbs:\n")
        for verb in classified_verbs["both"]:
            if verb in conjugations:
                conj1, conj2 = conjugations[verb]
                file.write(f"{verb} - {conj1}, {conj2}\n")
            else:
                file.write(f"{verb}\n")
        
        file.write("\nUnknown Verbs:\n")
        for verb in classified_verbs["unknown"]:
            file.write(f"{verb}\n")


def save_detailed_classification(classified_verbs, conjugations, file_path):
    """
    Third method: Saves the verbs in the format:
    verb;aspect;1st_person_singular;3rd_person_singular
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        # Imperfective Verbs
        for verb in classified_verbs["imperfective"]:
            if verb in conjugations:
                conj1, conj2 = conjugations[verb]
                file.write(f"{verb};imperfective;{conj1};{conj2}\n")
            else:
                file.write(f"{verb};imperfective\n")
        
        # Perfective Verbs
        for verb in classified_verbs["perfective"]:
            if verb in conjugations:
                conj1, conj2 = conjugations[verb]
                file.write(f"{verb};perfective;{conj1};{conj2}\n")
            else:
                file.write(f"{verb};perfective\n")
        
        # Both
        for verb in classified_verbs["both"]:
            if verb in conjugations:
                conj1, conj2 = conjugations[verb]
                file.write(f"{verb};both;{conj1};{conj2}\n")
            else:
                file.write(f"{verb};both\n")



def save_all_classifications(classified_verbs, conjugations, destination_folder):
    """
    Saves three types of files:
    1. Simple classification (First Method)
    2. Conjugation classification (Second Method)
    3. Detailed classification with aspect (Third Method)
    """
    # Define paths for each output file
    simple_path = os.path.join(destination_folder, 'simple_classification.txt')
    conjugation_path = os.path.join(destination_folder, 'conjugation_classification.txt')
    detailed_path = os.path.join(destination_folder, 'detailed_classification.txt')

    # Save simple classification (First Method)
    save_simple_classification(classified_verbs, simple_path)
    
    # Save conjugation classification (Second Method)
    save_conjugation_classification(classified_verbs, conjugations, conjugation_path)

    # Save detailed classification with aspect (Third Method)
    save_detailed_classification(classified_verbs, conjugations, detailed_path)

