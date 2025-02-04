from datetime import datetime
from typing import List, Dict, Optional

class InputHandler:  # Utility class for handling input
    def __init__(self) -> None:
        # InputHandler không cần khởi tạo state, nhưng thêm __init__ để tuân thủ chuẩn
        pass
    @staticmethod
    def input_number(prompt):
        while True:  # Loop for validating numeric input
            try:
                number = int(input(prompt))
                if number < 0:
                    print("Number cannot be negative. Try again.")
                else:
                    return number
            except ValueError:
                print("Invalid input, please enter a number.")

    @staticmethod
    def input_date(prompt: str) -> str:
        while True:
            date_input = input(prompt).strip()
            try:
                datetime.strptime(date_input, "%d/%m/%Y")
                return date_input
            except ValueError:
                print("Invalid date format. Please enter the date in DD/MM/YYYY format.")


class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

    def __str__(self) -> str:
        return f"ID: {self.student_id}, Name: {self.name}, DoB: {self.dob}"

    def add_mark(self, course_id: str, mark: float) -> None:
        if 0 <= mark <= 20:
            self.marks[course_id] = mark
        else:
            print("Mark must be between 0 and 20.")


class Course:
    def __init__(self, course_id: str, name: str) -> None:
        self.course_id = course_id
        self.name = name

    def __str__(self) -> str:
        return f"ID: {self.course_id}, Name: {self.name}"


class SchoolSystem(InputHandler):
    def __init__(self) -> None:

        super().__init__()  # Gọi __init__ của InputHandler
        self.students: List[Student] = []
        self.courses: List[Course] = []

    def input_students(self) -> None:
        num_students = self.input_number("Enter the number of students in the class: ")
        for _ in range(num_students):
            student_id = input("Enter student ID: ").strip()
            name = input("Enter student name: ").strip()
            dob = self.input_date("Enter student Date of Birth (DD/MM/YYYY): ")
            self.students.append(Student(student_id, name, dob))

    def input_courses(self) -> None:
        if self.students:
            num_courses = self.input_number("Enter the number of courses: ")
            for _ in range(num_courses):
                course_id = input("Enter course ID: ").strip()
                name = input("Enter course name: ").strip()
                self.courses.append(Course(course_id, name))
        else:
            print("No students to enroll in courses.")

    def input_marks(self) -> None:
        for course in self.courses:
            print(f"\nEntering marks for course {course.name} (ID: {course.course_id}):")
            for student in self.students:
                while True:
                    try:
                        mark = float(input(f"Enter mark for student {student.name} (ID: {student.student_id}): "))
                        student.add_mark(course.course_id, mark)
                        break
                    except ValueError:
                        print("Invalid input, please enter a number.")

    def list_students(self) -> None:
        if not self.students:
            print("No students available.")
        else:
            for student in self.students:
                print(student)

    def list_courses(self) -> None:
        if not self.courses:
            print("No courses available.")
        else:
            for course in self.courses:
                print(course)

    def show_marks_for_course(self) -> None:
        if self.courses:
            course_id = input("\nEnter course ID to view student marks: ").strip()
            found = False
            for student in self.students:
                mark = student.marks.get(course_id, None)
                if mark is not None:
                    print(f"{student.name} (ID: {student.student_id}) has marks: {mark}")
                    found = True
            if not found:  # If no marks found for a course, notify
                print(f"No marks available for course ID {course_id}.")
        else:
            print("No courses to show marks for.")


def main() -> None:
    system = SchoolSystem()
    system.input_students()
    system.input_courses()
    system.input_marks()
    # Display data
    print("\nList of Students:")
    system.list_students()

    print("\nList of Courses:")
    print("\nList of Courses:")  # Display courses

    system.show_marks_for_course()


if __name__ == "__main__":
    main()
