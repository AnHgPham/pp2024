from datetime import datetime


def input_number(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number < 0:
                print("Number cannot be negative. Try again.")
            else:
                return number
        except ValueError:
            print("Invalid input, please enter a number.")


def input_student_info(num_students):
    students = []
    for _ in range(num_students):
        student_id = input("Enter student ID: ").strip()
        student_name = input("Enter student name: ").strip()
        student_dob = input_date_of_birth()
        students.append({'id': student_id, 'name': student_name, 'dob': student_dob})
    return students


def input_date_of_birth():
    while True:
        dob = input("Enter student Date of Birth (DD/MM/YYYY): ").strip()
        try:
            datetime.strptime(dob, "%d/%m/%Y")
            return dob
        except ValueError:
            print("Invalid date format. Please enter the date in DD/MM/YYYY format.")


def input_course_info(num_courses):
    courses = []
    for _ in range(num_courses):
        course_id = input("Enter course ID: ").strip()
        course_name = input("Enter course name: ").strip()
        courses.append({'id': course_id, 'name': course_name})
    return courses


def input_marks_for_course(students, course_id):
    for student in students:
        while True:
            try:
                mark = float(input(f"Enter mark for student {student['name']} (ID: {student['id']}): "))
                if 0 <= mark <= 20:
                    student.setdefault('marks', {})[course_id] = mark
                    break
                else:
                    print("Mark must be between 0 and 20.")
            except ValueError:
                print("Invalid input, please enter a number.")


def list_items(items, item_name):
    if not items:
        print(f"No {item_name} available.")
    for item in items:
        details = ', '.join([f"{k.capitalize()}: {v}" for k, v in item.items()])
        print(details)


def show_student_marks_for_course(students, course_id):
    for student in students:
        marks = student.get('marks', {}).get(course_id, None)
        if marks is not None:
            print(f"{student['name']} (ID: {student['id']}) has marks: {marks}")
        else:
            print(f"No marks available for {student['name']} in course ID {course_id}.")


def main():
    num_students = input_number("Enter the number of students in the class: ")
    students = input_student_info(num_students)

    num_courses = input_number("Enter the number of courses: ") if num_students > 0 else 0
    courses = input_course_info(num_courses)

    for course in courses:
        print(f"Entering marks for course {course['name']} (ID: {course['id']}):")
        input_marks_for_course(students, course['id'])

    print("\nList of Students:")
    list_items(students, "students")

    print("\nList of Courses:")
    list_items(courses, "courses")

    if courses:
        course_id = input("\nEnter course ID to view student marks: ").strip()
        show_student_marks_for_course(students, course_id)


if __name__ == "__main__":
    main()
