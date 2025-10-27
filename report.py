# report.py
# ---------------------------------
# Class: Report
# Purpose: Generate and display summarized feedback reports for faculty
# ---------------------------------

class Report:
    def __init__(self, feedback_list):
        """
        Initializes the Report class with a list of feedback entries.
        Each feedback entry is expected to be a dictionary containing:
        student_name, course_name, rating, and comments.
        """
        self.feedback_list = feedback_list

    def calculate_average_rating(self, course_name):
        """
        Calculates the average rating for a given course.
        Returns 0 if no feedback exists for that course.
        """
        course_feedbacks = [f for f in self.feedback_list if f['course_name'] == course_name]
        if not course_feedbacks:
            return 0
        total = sum(f['rating'] for f in course_feedbacks)
        return total / len(course_feedbacks)

    def count_feedback(self, course_name):
        """
        Counts how many feedback entries exist for a given course.
        """
        return len([f for f in self.feedback_list if f['course_name'] == course_name])

    def display_report(self):
        """
        Displays a formatted report of feedback for all courses.
        """
        if not self.feedback_list:
            print("No feedback available to display.")
            return

        print("\n===== FEEDBACK REPORT =====\n")
        courses = set([f['course_name'] for f in self.feedback_list])

        for course in courses:
            avg = self.calculate_average_rating(course)
            count = self.count_feedback(course)
            print(f"Course: {course}")
            print(f"  Total Feedbacks: {count}")
            print(f"  Average Rating: {avg:.2f}")
            print("---------------------------")
