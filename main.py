from student import Student
from feedback import Feedback
from course import Course

def main():
    courses = [Course("CS101", "Software Engineering")]
    student = Student("S001", "Aarav Singh")

    print("1. Submit Feedback\n2. View Feedback")
    choice = int(input("Enter choice: "))

    if choice == 1:
        rating = int(input("Enter rating (1–5): "))
        comments = input("Enter comments: ")
        fb = Feedback(student, courses[0], rating, comments)
        fb.save_feedback()
    elif choice == 2:
        Feedback.view_all_feedback()

if __name__ == "__main__":
    main()
