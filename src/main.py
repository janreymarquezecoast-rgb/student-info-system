import logging

from src.services.student_service import StudentService
from src.utils.config import load_config

config = load_config()

logging.basicConfig(
    filename=config["log_file"],
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

service = StudentService(config["data_file"])

def show_menu():
    print("\n=== Student Information System ===")
    print("1. Add Student")
    print("2. View All Students")
    print("3. View Student by ID")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

def main():
    while True:
        show_menu()

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            view_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Thank you for using the Student Information System.")
            break
        else:
            print("Invalid choice. Please try again.")

def add_student():
    print("\n--- Add Student ---")

    name = input("Enter name: ")
    email = input("Enter email: ")
    course = input("Enter course: ")
    year_level = input("Enter year level: ")
    gpa = input("Enter GPA: ")

    student = service.add_student(
        name,
        email,
        course,
        year_level,
        gpa
    )

    logging.info("Student added: %s", student.student_id)

    print("Student added successfully!")
    print("Student ID:", student.student_id)

def view_students():
    print("\n--- Student Records ---")

    students = service.get_all_students()

    if not students:
        print("No student records found.")
        return

    for student in students:
        print("------------------------")
        print("Student ID:", student["student_id"])
        print("Name:", student["name"])
        print("Email:", student["email"])
        print("Course:", student["course"])
        print("Year Level:", student["year_level"])
        print("GPA:", student["gpa"])

def view_student():
    print("\n--- View Student ---")

    student_id = input("Enter student ID: ")

    student = service.get_student(student_id)

    if student is None:
        print("Student not found.")
        return

    print("------------------------")
    print("Student ID:", student["student_id"])
    print("Name:", student["name"])
    print("Email:", student["email"])
    print("Course:", student["course"])
    print("Year Level:", student["year_level"])
    print("GPA:", student["gpa"])

def update_student():
    print("\n--- Update Student ---")

    student_id = input("Enter student ID: ")

    student = service.get_student(student_id)

    if student is None:
        print("Student not found.")
        return

    name = input("Enter new name: ")
    email = input("Enter new email: ")
    course = input("Enter new course: ")
    year_level = input("Enter new year level: ")
    gpa = input("Enter new GPA: ")

    success = service.update_student(
        student_id,
        name,
        email,
        course,
        year_level,
        gpa
    )

    if success:
        logging.info("Student updated: %s", student_id)
        print("Student updated successfully!")
    else:
        print("Unable to update student.")

def delete_student():
    print("\n--- Delete Student ---")

    student_id = input("Enter student ID: ")

    success = service.delete_student(student_id)

    if success:
        logging.info("Student deleted: %s", student_id)
        print("Student deleted successfully!")
    else:
        print("Student not found.")

if __name__ == "__main__":
    main()