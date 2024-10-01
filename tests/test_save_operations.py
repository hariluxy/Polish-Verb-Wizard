import unittest
import os
import tempfile
from operations_verb.save_operations import save_verb_simple, save_verb_conjugation, save_verb_SCSV


class TestSaveOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n3-Starting the verb save operations test.")

    @classmethod
    def tearDownClass(cls):
        print("\nSuccessful.\n")

    def setUp(self):
        # Verbs already classified using the new structure (verb_list)
        self.verbs_aspect = {
            "istnieć": {"aspect": "imperfective", "first_person_conjugation": "istnieję", "third_person_conjugation": "istnieje"},
            "różnić": {"aspect": "imperfective", "first_person_conjugation": "różnię", "third_person_conjugation": "różni"},
            "nużyć": {"aspect": "imperfective", "first_person_conjugation": "nużę", "third_person_conjugation": "nuży"},
            "wspierać": {"aspect": "imperfective", "first_person_conjugation": "wspieram", "third_person_conjugation": "wspiera"},
            "przyzwyczaić": {"aspect": "perfective", "first_person_conjugation": "przyzwyczaję", "third_person_conjugation": "przyzwyczai"},
            "sporządzić": {"aspect": "perfective", "first_person_conjugation": "sporządzę", "third_person_conjugation": "sporządzi"},
            "ruszyć": {"aspect": "perfective", "first_person_conjugation": "ruszę", "third_person_conjugation": "ruszy"},
            "oszczędzić": {"aspect": "perfective", "first_person_conjugation": "oszczędzę", "third_person_conjugation": "oszczędzi"},
            "przeczuwać": {"aspect": "both", "first_person_conjugation": "przeczuwam", "third_person_conjugation": "przeczuwa"},
            "należeć": {"aspect": "both", "first_person_conjugation": "należę", "third_person_conjugation": "należy"},
            "powodzić": {"aspect": "unknown", "first_person_conjugation": None, "third_person_conjugation": None},
            "pasować": {"aspect": "unknown", "first_person_conjugation": None, "third_person_conjugation": None}
        }

        # Expected result for the first saving method
        self.expected_result = (
            "Imperfective Verbs:\n"
            "istnieć\n"
            "różnić\n"
            "nużyć\n"
            "wspierać\n\n"
            "Perfective Verbs:\n"
            "przyzwyczaić\n"
            "sporządzić\n"
            "ruszyć\n"
            "oszczędzić\n\n"
            "Both Verbs:\n"
            "przeczuwać\n"
            "należeć\n\n"
            "Unknown Verbs:\n"
            "powodzić\n"
            "pasować\n"
        )

        # Expected result for the second method (with conjugations)
        self.expected_conjugation_result = (
            "Imperfective Verbs:\n"
            "istnieć - istnieję, istnieje\n"
            "różnić - różnię, różni\n"
            "nużyć - nużę, nuży\n"
            "wspierać - wspieram, wspiera\n\n"
            "Perfective Verbs:\n"
            "przyzwyczaić - przyzwyczaję, przyzwyczai\n"
            "sporządzić - sporządzę, sporządzi\n"
            "ruszyć - ruszę, ruszy\n"
            "oszczędzić - oszczędzę, oszczędzi\n\n"
            "Both Verbs:\n"
            "przeczuwać - przeczuwam, przeczuwa\n"
            "należeć - należę, należy\n"
        )

        # Expected result for the third method (SCSV format)
        self.expected_scsv_result = (
            "istnieć;imperfective;istnieję;istnieje\n"
            "różnić;imperfective;różnię;różni\n"
            "nużyć;imperfective;nużę;nuży\n"
            "wspierać;imperfective;wspieram;wspiera\n"
            "przyzwyczaić;perfective;przyzwyczaję;przyzwyczai\n"
            "sporządzić;perfective;sporządzę;sporządzi\n"
            "ruszyć;perfective;ruszę;ruszy\n"
            "oszczędzić;perfective;oszczędzę;oszczędzi\n"
            "przeczuwać;both;przeczuwam;przeczuwa\n"
            "należeć;both;należę;należy\n"
        )

    # Test the first method (Only aspects)
    def test_save_verb_simple(self):

        # Create a temporary file to test saving
        with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8') as temp_file:
            temp_file_path = temp_file.name

        try:
            # Save the classified verbs using the first method
            save_verb_simple(self.verbs_aspect, temp_file_path)

            # Read the saved content
            with open(temp_file_path, 'r', encoding='utf-8') as file:
                saved_content = file.read()

            # Compare the saved content with the expected result
            self.assertEqual(saved_content, self.expected_result, 
                             msg="The saved content does not match the expected output.")

        finally:
            # Clean up: remove the temporary file
            os.remove(temp_file_path)


    # Test the second method (with conjugations)
    def test_save_verb_conjugation(self):
        
        # Create a temporary file to test saving
        with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8') as temp_file:
            temp_file_path = temp_file.name

        try:
            # Save the classified verbs with conjugations using the second method
            save_verb_conjugation(self.verbs_aspect, temp_file_path)

            # Read the saved content
            with open(temp_file_path, 'r', encoding='utf-8') as file:
                saved_content = file.read()

            # Compare the saved content with the expected result
            self.assertEqual(saved_content, self.expected_conjugation_result, 
                             msg="The saved content does not match the expected output for the second method.")

        finally:
            # Clean up: remove the temporary file
            os.remove(temp_file_path)

    # Test the third method (SCSV format)
    def test_save_verb_scsv(self):
        
        # Create a temporary file to test saving
        with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8') as temp_file:
            temp_file_path = temp_file.name

        try:
            # Save the classified verbs in SCSV format
            save_verb_SCSV(self.verbs_aspect, temp_file_path)

            # Read the saved content
            with open(temp_file_path, 'r', encoding='utf-8') as file:
                saved_content = file.read()

            # Compare the saved content with the expected result
            self.assertEqual(saved_content, self.expected_scsv_result, 
                             msg="The saved content does not match the expected output for the third method (SCSV).")

        finally:
            # Clean up: remove the temporary file
            os.remove(temp_file_path)


if __name__ == '__main__':
    unittest.main()
