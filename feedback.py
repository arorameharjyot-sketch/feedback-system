class Feedback:
    feedback_list = []

    def __init__(self, student, course, rating, comments):
        self.student = student
        self.course = course
        self.rating = rating
        self.comments = comments

    def save_feedback(self):
        Feedback.feedback_list.append(self)
        print(f"✅ Feedback saved for {self.course.course_name}")

    @staticmethod
    def view_all_feedback():
        print("\n--- Feedback Records ---")
        for fb in Feedback.feedback_list:
            print(f"{fb.student.name} rated {fb.course.course_name}: {fb.rating}/5 - {fb.comments}")
