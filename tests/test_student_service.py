import unittest
import os
import tempfile

from src.services.student_service import StudentService


class TestStudentService(unittest.TestCase):

    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file.close()

        self.service = StudentService(self.temp_file.name)

    def tearDown(self):
        if os.path.exists(self.temp_file.name):
            os.remove(self.temp_file.name)

    def test_add_student(self):
        student = self.service.add_student(
            "Janrey Marquez",
            "janrey@example.com",
            "BSIT",
            "2",
            "1.75"
        )

        self.assertIsNotNone(student)
        self.assertEqual(student.name, "Janrey Marquez")

    def test_get_student(self):
        student = self.service.add_student(
            "Janrey Marquez",
            "janrey@example.com",
            "BSIT",
            "2",
            "1.75"
        )

        result = self.service.get_student(student.student_id)

        self.assertIsNotNone(result)
        self.assertEqual(result["name"], "Janrey Marquez")

    def test_update_student(self):
        student = self.service.add_student(
            "Janrey Marquez",
            "janrey@example.com",
            "BSIT",
            "2",
            "1.75"
        )

        result = self.service.update_student(
            student.student_id,
            "Janrey Luis Marquez",
            "new@example.com",
            "BSIT",
            "2",
            "1.50"
        )

        self.assertTrue(result)

    def test_delete_student(self):
        student = self.service.add_student(
            "Janrey Marquez",
            "janrey@example.com",
            "BSIT",
            "2",
            "1.75"
        )

        result = self.service.delete_student(student.student_id)

        self.assertTrue(result)
        self.assertIsNone(
            self.service.get_student(student.student_id)
        )


if __name__ == "__main__":
    unittest.main()