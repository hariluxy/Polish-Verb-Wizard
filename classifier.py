import morfeusz2

def classify_verbs(verbs):
    """
    Classifies verbs into Imperfective, Perfective, Both or Unknown.

    Args:
        verbs (list): A list of verbs to classify.

    Returns:
        dict: A dictionary with aspects as keys and lists of verbs as values. ????
    """
    morfeusz = morfeusz2.Morfeusz()
    classifications = {
        'imperfective': [], 
        'perfective': [],
        'both': [],
        'unknown': []
    }

    for verb in verbs:
        analyses = morfeusz.analyse(verb)
        aspects = set()
        for ana in analyses:
            interp = ana[2]
            tags = interp[2].split(':')
            
            # Check for aspect tags
            if 'imperf' in tags:
                aspects.add('imperfective')
            if 'perf' in tags:
                aspects.add('perfective')
        if aspects == {'imperfective'}:
            classifications['imperfective'].append(verb)
        elif aspects == {'perfective'}:
            classifications['perfective'].append(verb)
        elif aspects == {'imperfective', 'perfective'}:
            classifications['both'].append(verb)
        else:
            classifications['unknown'].append(verb)
    return classifications
