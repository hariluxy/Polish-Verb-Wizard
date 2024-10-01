"""
    Classifies verbs into Imperfective, Perfective, Both or Unknown.

    It also sets up the verb_list dict that will be used throughout the code

    It uses morfeusz2 to perform the morphological analysis for Polish.

"""

import morfeusz2

def verbs_by_aspect(verbs):

    morfeusz = morfeusz2.Morfeusz()  # Init morfeusz2

    # Prepare the dictionary that will be returned
    verb_list = {}

    # Loop over the verbs
    for verb in verbs:
        analyses = morfeusz.analyse(verb)
        aspects = set()
        # Loop over the morfeusz2 analysis to save tags
        for ana in analyses:
            interp = ana[2]
            tags = interp[2].split(':')

            # Check for aspect tags
            if 'imperf' in tags:
                aspects.add('imperfective')
            if 'perf' in tags:
                aspects.add('perfective')

        # Determine the aspect classification
        if aspects == {'imperfective'}:
            aspect = 'imperfective'
        elif aspects == {'perfective'}:
            aspect = 'perfective'
        elif aspects == {'imperfective', 'perfective'}:
            aspect = 'both'
        else:
            aspect = 'unknown'

        # Add the verb to the verb_list dictionary with aspect and empty placeholders for later conjugations
        verb_list[verb] = {
            "aspect": aspect,
            "first_person_conjugation": None,  # Placeholder, can be updated later
            "third_person_conjugation": None   # Placeholder, can be updated later
        }

    return verb_list
