# verbs.py

def read_verbs(file_path):
    """
    Reads verbs from a text file and returns a list of verbs.

    Args:
        file_path (str): The path to the verbs file.

    Returns:
        list: A list of verbs.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            verbs = [line.strip() for line in file if line.strip()]
        return verbs
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
