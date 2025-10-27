import unittest
from feedback import Feedback
from report import Report

class TestFeedback(unittest.TestCase):

    def setUp(self):
        self.feedback = Feedback()

    def test_add_feedback(self):
        result = self.feedback.add_feedback("Meharjyot", "Python Programming", 5, "Excellent course!")
        self.assertEqual(result, "Feedback submitted successfully")

    def test_view_feedback(self):
        self.feedback.add_feedback("John", "Data Structures", 4, "Good teaching")
        feedback_list = self.feedback.view_feedback()
        self.assertEqual(len(feedback_list), 1)
        self.assertIn("John", feedback_list[0]['student_name'])


class TestReport(unittest.TestCase):

    def setUp(self):
        self.feedback = Feedback()
        self.feedback.add_feedback("Anita", "OOP", 3, "Average course")
        self.feedback.add_feedback("Rohit", "OOP", 5, "Very informative")
        self.report = Report(self.feedback.get_all_feedback())

    def test_average_rating(self):
        avg = self.report.calculate_average_rating("OOP")
        self.assertEqual(avg, 4)

    def test_feedback_count(self):
        count = self.report.count_feedback("OOP")
        self.assertEqual(count, 2)


if __name__ == '__main__':
    unittest.main()
