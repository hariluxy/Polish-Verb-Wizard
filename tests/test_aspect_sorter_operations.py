import unittest
from operations_verb.aspect_sorter_operations import verbs_by_aspect

class TestVerbAspectSorting(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("\n1-Starting the verb aspect classification test.")

    @classmethod
    def tearDownClass(cls):
        print("\nSuccessful.\n")


    def setUp(self):
        # Sample verbs for testing
        self.verbs = [
            "istnieć",      # Imperfective
            "różnić",       # Imperfective
            "nużyć",        # Imperfective
            "wspierać",     # Imperfective
            "przyzwyczaić", # Perfective
            "sporządzić",   # Perfective
            "ruszyć",       # Perfective
            "oszczędzić",   # Perfective
            "przeczuwać",   # Both
            "należeć",      # Both
            "powodzić",     # Unknown
            "pasować"       # Unknown
        ]

        # Expected result
        self.expected_result = {
            'imperfective': ['istnieć', 'różnić', 'nużyć', 'wspierać'],
            'perfective': ['przyzwyczaić', 'sporządzić', 'ruszyć', 'oszczędzić'],
            'both': ['przeczuwać', 'należeć'],
            'unknown': ['powodzić', 'pasować']
        }

    def test_verb_aspect_classification(self):
        result = verbs_by_aspect(self.verbs)
        
        # Create lists for the aspects based on the new structure
        imperfective_verbs = [verb for verb, data in result.items() if data['aspect'] == 'imperfective']
        perfective_verbs = [verb for verb, data in result.items() if data['aspect'] == 'perfective']
        both_verbs = [verb for verb, data in result.items() if data['aspect'] == 'both']
        unknown_verbs = [verb for verb, data in result.items() if data['aspect'] == 'unknown']

        # Assert that the results match the expected outcome
        self.assertEqual(imperfective_verbs, self.expected_result['imperfective'], 
                         f"Expected {self.expected_result['imperfective']}, but got {imperfective_verbs}")
        self.assertEqual(perfective_verbs, self.expected_result['perfective'], 
                         f"Expected {self.expected_result['perfective']}, but got {perfective_verbs}")
        self.assertEqual(both_verbs, self.expected_result['both'], 
                         f"Expected {self.expected_result['both']}, but got {both_verbs}")
        self.assertEqual(unknown_verbs, self.expected_result['unknown'], 
                         f"Expected {self.expected_result['unknown']}, but got {unknown_verbs}")

if __name__ == '__main__':
    unittest.main()
