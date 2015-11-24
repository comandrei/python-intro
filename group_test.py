import unittest
from cStringIO import StringIO
from grouped_by_year import group_students


class GroupStudentsTest(unittest.TestCase):

    def setUp(self):
        rows = ["Ionescu Andrei,Facultatea de Automatica,Anul I",
                "Popescu Ion,Facultatea de Automatica,Anul II",
                "Danescu Andrei,Facultatea de Automatica,Anul I",
                "Altescu Andreea,Facultatea de Arhitectura,Anul V"]
        self.file = StringIO('\n'.join(rows))
        self.file.seek(0)
        self.students = group_students(self.file)

    def tearDown(self):
        self.file.close()

    def test_all_years_matched(self):
        self.assertItemsEqual(self.students.keys(),
                              ["Anul I", "Anul II", "Anul V"])

    def test_only_one_student(self):
        self.assertEqual(len(self.students["Anul II"]), 1)

    def test_multiple_students_grouped(self):
        self.assertEqual(len(self.students["Anul I"]), 2)

    def test_right_students_get_matched(self):
        student = self.students["Anul V"][0]
        nume, facultate, an = student["NUME"], student["FACULTATE"], student["AN"]
        self.assertEqual("Altescu Andreea", nume)
        self.assertEqual("Facultatea de Arhitectura", facultate)
        self.assertEqual("Anul V", an)

if __name__ == "__main__":
    unittest.main()
