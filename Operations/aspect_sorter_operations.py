"""
    Classifies verbs into Imperfective, Perfective, Both or Unknown.

    It uses morfeusz2 to perform the morphological analysis for Polish.

"""


import morfeusz2

def verbs_by_aspect(verbs):

    morfeusz = morfeusz2.Morfeusz() # Init morfeusz2

    # Prepare a dictionary
    verb_aspect = {
        'imperfective': [], 
        'perfective': [],
        'both': [],
        'unknown': []
    }

    # Loop over the verbs
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

        # Classify the verbs based on aspects
        if aspects == {'imperfective'}:
            verb_aspect['imperfective'].append(verb)
        elif aspects == {'perfective'}:
            verb_aspect['perfective'].append(verb)
        elif aspects == {'imperfective', 'perfective'}:
            verb_aspect['both'].append(verb)
        else:
            verb_aspect['unknown'].append(verb)

    return verb_aspect
