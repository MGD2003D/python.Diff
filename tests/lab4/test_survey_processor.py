import unittest
from src.lab4.survey_sorter.survey_processor import SurveyProcessor


class TestSurveyProcessor(unittest.TestCase):
    def setUp(self):
        self.age_bounds = [18, 35, 50]
        self.processor = SurveyProcessor(self.age_bounds)

    def test_initialization(self):
        self.assertEqual(len(self.processor.age_groups), 4)
        self.assertEqual(self.processor.age_groups[0].lower_bound, 0)
        self.assertEqual(self.processor.age_groups[0].upper_bound, 18)
        self.assertEqual(self.processor.age_groups[1].lower_bound, 19)
        self.assertEqual(self.processor.age_groups[1].upper_bound, 35)
        self.assertEqual(self.processor.age_groups[2].lower_bound, 36)
        self.assertEqual(self.processor.age_groups[2].upper_bound, 50)
        self.assertEqual(self.processor.age_groups[3].lower_bound, 51)
        self.assertEqual(self.processor.age_groups[3].upper_bound, 123)

    def test_process_respondents(self):
        input_lines = [
            "John Doe,25",
            "Jane Smith,40",
            "Alice Johnson,17",
            "Bob Brown,51"
        ]
        self.processor.process_respondents(input_lines)

        self.assertEqual(len(self.processor.age_groups[0].respondents), 1)
        self.assertEqual(len(self.processor.age_groups[1].respondents), 1)
        self.assertEqual(len(self.processor.age_groups[2].respondents), 1)
        self.assertEqual(len(self.processor.age_groups[3].respondents), 1)

        self.assertEqual(str(self.processor.age_groups[0].respondents[0]), "Alice Johnson (17)")
        self.assertEqual(str(self.processor.age_groups[1].respondents[0]), "John Doe (25)")
        self.assertEqual(str(self.processor.age_groups[2].respondents[0]), "Jane Smith (40)")
        self.assertEqual(str(self.processor.age_groups[3].respondents[0]), "Bob Brown (51)")

    def test_get_results(self):
        input_lines = [
            "John Doe,25",
            "Jane Smith,40",
            "Alice Johnson,17",
            "Bob Brown,51"
        ]
        self.processor.process_respondents(input_lines)
        expected_result = (
            "0-18+: Alice Johnson (17)\n"
            "19-35+: John Doe (25)\n"
            "36-50+: Jane Smith (40)\n"
            "51-123+: Bob Brown (51)"
        )
        self.assertEqual(self.processor.get_results(), expected_result)


if __name__ == '__main__':
    unittest.main()