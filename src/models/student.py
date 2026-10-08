import uuid
from datetime import datetime


class Student:
    def __init__(self, name, email, course, year_level, gpa):
        self.student_id = str(uuid.uuid4())[:8]
        self.name = name
        self.email = email
        self.course = course
        self.year_level = year_level
        self.gpa = gpa
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "email": self.email,
            "course": self.course,
            "year_level": self.year_level,
            "gpa": self.gpa,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }