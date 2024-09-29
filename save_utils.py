def save_results(classified_verbs, conjugations, file_path, include_conjugations):
    """
    Saves the classified verbs and conjugations to the output file.
    If include_conjugations is True, conjugations will be added.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("Imperfective Verbs:\n")
        for verb in classified_verbs["imperfective"]:  
            if include_conjugations and verb in conjugations:
                conj1, conj2 = conjugations[verb]
                file.write(f"{verb};{conj1};{conj2}\n")
            else:
                file.write(f"{verb}\n")
        
        file.write("\nPerfective Verbs:\n")
        for verb in classified_verbs["perfective"]:  
            if include_conjugations and verb in conjugations:
                conj1, conj2 = conjugations[verb]
                file.write(f"{verb};{conj1};{conj2}\n")
            else:
                file.write(f"{verb}\n")
        
        file.write("\nBoth Verbs:\n")
        for verb in classified_verbs["both"]:  
            if include_conjugations and verb in conjugations:
                conj1, conj2 = conjugations[verb]
                file.write(f"{verb};{conj1};{conj2}\n")
            else:
                file.write(f"{verb}\n")
        
        file.write("\nUnknown Verbs:\n")
        for verb in classified_verbs["unknown"]:  
            file.write(f"{verb}\n")

def save_results_custom_format(classified_verbs, conjugations, file_path):
    """
    Saves the classified verbs in the custom format: verb;aspect;1st_singular;3rd_singular
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        for verb in classified_verbs["imperfective"]:
            if verb in conjugations:
                conj1, conj2 = conjugations[verb]
                file.write(f"{verb};imperfective;{conj1};{conj2}\n")
                
        
        for verb in classified_verbs["perfective"]:
            if verb in conjugations:
                conj1, conj2 = conjugations[verb]
                file.write(f"{verb};perfective;{conj1};{conj2}\n")
                

        for verb in classified_verbs["both"]:
            if verb in conjugations:
                conj1, conj2 = conjugations[verb]
                file.write(f"{verb};both;{conj1};{conj2}\n")

        for verb in classified_verbs["unknown"]:
            file.write(f"{verb};unknown\n")
