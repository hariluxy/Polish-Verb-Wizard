import unittest
from operations_verb.aspect_sorter_operations import verbs_by_aspect



class TestAspectSorterOperationsEdgeCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\nStarting the general case tests.")

    @classmethod
    def tearDownClass(cls):
        print("\nThe general case tests have been successful.")

    """
    Test that an empty list of verbs is handled accordingly.
    The expected result is that all categories remain empty.
    """
    def test_empty_verb_list(self):
       
        # Empty list of verbs
        verbs = []  
        expected_result = {
            'imperfective': [],
            'perfective': [],
            'both': [],
            'unknown': []
        }
        
        result = verbs_by_aspect(verbs)
        
        self.assertEqual(result, expected_result, "Empty verb list should result in empty categorized aspects.")

    """
    Test that a list of invalid or non-existent verbs is classified as 'unknown'.
    The expected result is that the invalid verbs appear only in the 'unknown' category.
    """
    def test_invalid_verbs(self):

        # Invalid verbs
        verbs = ['abcd', 'xyz', 'notaverb']  
        expected_result = {
            'imperfective': [],
            'perfective': [],
            'both': [],
            'unknown': ['abcd', 'xyz', 'notaverb']
        }
        
        result = verbs_by_aspect(verbs)
        
        self.assertEqual(result['unknown'], expected_result['unknown'], "Invalid verbs should be classified as unknown.")
        self.assertEqual(len(result['imperfective']), 0, "There should be no imperfective verbs.")
        self.assertEqual(len(result['perfective']), 0, "There should be no perfective verbs.")
        self.assertEqual(len(result['both']), 0, "There should be no verbs classified as both.")

if __name__ == '__main__':
    unittest.main()
