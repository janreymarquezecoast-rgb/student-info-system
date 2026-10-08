import json
import os
from datetime import datetime

from src.models.student import Student


class StudentService:
    def __init__(self, data_file="data/students.json"):
        self.data_file = data_file
        self._ensure_data_file()

    def _ensure_data_file(self):
        directory = os.path.dirname(self.data_file)

        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        if not os.path.exists(self.data_file):
            with open(self.data_file, "w") as file:
                json.dump([], file, indent=4)

    def _load_students(self):
        try:
            with open(self.data_file, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def _save_students(self, students):
        with open(self.data_file, "w") as file:
            json.dump(students, file, indent=4)

    def add_student(self, name, email, course, year_level, gpa):
        student = Student(name, email, course, year_level, gpa)

        students = self._load_students()
        students.append(student.to_dict())

        self._save_students(students)

        return student

    def get_all_students(self):
        return self._load_students()

    def get_student(self, student_id):
        students = self._load_students()

        for student in students:
            if student["student_id"] == student_id:
                return student

        return None

    def update_student(self, student_id, name, email, course, year_level, gpa):
        students = self._load_students()

        for student in students:
            if student["student_id"] == student_id:
                student["name"] = name
                student["email"] = email
                student["course"] = course
                student["year_level"] = year_level
                student["gpa"] = gpa
                student["updated_at"] = datetime.now().isoformat()

                self._save_students(students)
                return True

        return False

    def delete_student(self, student_id):
        students = self._load_students()

        for student in students:
            if student["student_id"] == student_id:
                students.remove(student)
                self._save_students(students)
                return True

        return False