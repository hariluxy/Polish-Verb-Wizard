import unittest
import os
import tempfile
from operations_verb.save_operations import save_verb_simple, save_verb_conjugation, save_verb_SCSV


class TestSaveOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\nStarting the verb save operations test.")

    @classmethod
    def tearDownClass(cls):
        print("\nThe verb save operations test has been successful.\n")

    def setUp(self):

        # Verbs already classified using the new structure
        self.verbs_aspect = {
            "istnieć": {"aspect": "imperfective", "first_person_conjugation": "istnieję", "third_person_conjugation": "istnieje"},
            "różnić": {"aspect": "imperfective", "first_person_conjugation": "różnię", "third_person_conjugation": "różni"},
            "nużyć": {"aspect": "imperfective", "first_person_conjugation": "nużę", "third_person_conjugation": "nuży"},
            "wspierać": {"aspect": "imperfective", "first_person_conjugation": "wspieram", "third_person_conjugation": "wspiera"},
            "przyzwyczaić": {"aspect": "perfective", "first_person_conjugation": "przyzwyczajam", "third_person_conjugation": "przyzwyczaja"},
            "sporządzić": {"aspect": "perfective", "first_person_conjugation": "sporządzam", "third_person_conjugation": "sporządza"},
            "ruszyć": {"aspect": "perfective", "first_person_conjugation": "ruszam", "third_person_conjugation": "rusza"},
            "oszczędzić": {"aspect": "perfective", "first_person_conjugation": "oszczędzam", "third_person_conjugation": "oszczędza"},
            "przeczuwać": {"aspect": "both", "first_person_conjugation": "przeczuwam", "third_person_conjugation": "przeczuwa"},
            "należeć": {"aspect": "both", "first_person_conjugation": "należę", "third_person_conjugation": "należy"},
            "powodzić": {"aspect": "unknown", "first_person_conjugation": None, "third_person_conjugation": None},
            "pasować": {"aspect": "unknown", "first_person_conjugation": None, "third_person_conjugation": None}
        }

    # First test: Save verbs classified by aspect
    def test_save_verb_simple(self):
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file_path = temp_file.name
        save_verb_simple(self.verbs_aspect, temp_file_path)
        os.remove(temp_file_path)

    # Second test: Save verbs classified by aspect with conjugations
    def test_save_verb_conjugation(self):
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file_path = temp_file.name
        save_verb_conjugation(self.verbs_aspect, temp_file_path)
        os.remove(temp_file_path)

    # Third test: Save verbs in SCSV format 
    def test_save_verb_scsv(self):
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file_path = temp_file.name
        save_verb_SCSV(self.verbs_aspect, temp_file_path)
        os.remove(temp_file_path)


if __name__ == '__main__':
    unittest.main()
