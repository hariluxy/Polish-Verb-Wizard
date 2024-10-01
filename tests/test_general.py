import unittest
from operations_verb.aspect_sorter_operations import verbs_by_aspect


class TestAspectSorterOperationsEdgeCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n2-Starting the general case tests.")

    @classmethod
    def tearDownClass(cls):
        print("\nSuccessful.\n")

 
    # Test that an empty list of verbs returns only empty categories
    def test_empty_verb_list(self):
        # Empty list of verbs
        verbs = []  
        expected_result = {}

        # Call the function
        result = verbs_by_aspect(verbs)

        # Check if the result matches the expected structure with empty lists
        self.assertEqual(result, expected_result, "Empty verb list should result in empty categorized aspects.")

    """
    Test that a list of invalid or non-existent verbs is classified as 'unknown'.
    """
    def test_invalid_verbs(self):
        # List of invalid verbs
        verbs = ['xyz', 'abc', 'invalidverb']
        expected_result = ['xyz', 'abc', 'invalidverb']

        # Classify the verbs
        result = verbs_by_aspect(verbs)

        # Collect verbs classified as 'unknown'
        unknown_verbs = [verb for verb, data in result.items() if data['aspect'] == 'unknown']

        # Check if the invalid verbs are classified as 'unknown'
        self.assertEqual(unknown_verbs, expected_result, "Invalid verbs should be classified as unknown.")



if __name__ == '__main__':
    unittest.main()
