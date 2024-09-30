import unittest
from operations_verb.aspect_sorter_operations import verbs_by_aspect



class TestVerbAspectSorting(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("\nStarting the verb aspect classification test.")

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
    

    # Check that the result matches the expected classification
    def test_verb_aspect_classification(self):
        result = verbs_by_aspect(self.verbs)
        
        # Test each aspect separately for better failure reporting
        self.assertEqual(result['imperfective'], self.expected_result['imperfective'],
                         msg="Failed to classify some imperfective verbs correctly.")
        self.assertEqual(result['perfective'], self.expected_result['perfective'],
                         msg="Failed to classify some perfective verbs correctly.")
        self.assertEqual(result['both'], self.expected_result['both'],
                         msg="Failed to classify some 'both' aspect verbs correctly.")
        self.assertEqual(result['unknown'], self.expected_result['unknown'],
                         msg="Failed to classify some unknown aspect verbs correctly.")
        
    @classmethod
    def tearDownClass(cls):
        print("\nThe verb aspect classification test has been successful")

if __name__ == '__main__':
    unittest.main()