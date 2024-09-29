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
            if include_conjugations and verb in conjugations:
                conj1, conj2 = conjugations[verb]
                file.write(f"{verb};{conj1};{conj2}\n")
            else:
                file.write(f"{verb}\n")
