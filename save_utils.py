def save_results(classifications, output_file):
    """
    Saves the classification results to a text file.

    Args:
        classifications (dict): The classification results.
        output_file (str): The path to the output file.
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            for aspect, verbs in classifications.items():
                file.write(f"{aspect.capitalize()} verbs:\n")
                for verb in verbs:
                    file.write(f"{verb}\n")
                file.write("\n")
        print(f"Results have been saved to '{output_file}'.")
    except Exception as e:
        print(f"Error while writing to file: {e}")
