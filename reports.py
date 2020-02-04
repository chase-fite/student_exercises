import sqlite3
from student import Student
from cohort import Cohort
from exercise import Exercise

class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/Chase/workspace/python/student_exercises/studentexercises.db"

    def all_cohorts(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Cohort(row[1])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select c.Id,
            c.Name
            from Cohort c
            """)

            all_cohorts = db_cursor.fetchall()

            [print(s) for s in all_cohorts]

    def all_exercises(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.Id,
            e.Name,
            e.ExLanguage
            from Exercise e
            """)

            all_exercises = db_cursor.fetchall()

            [print(s) for s in all_exercises]

    def all_javascript_exercises(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.Id,
            e.Name,
            e.ExLanguage
            from Exercise e
            """)

            all_javascript_exercises = db_cursor.fetchall()

            [print(e) for e in all_javascript_exercises if e.language == 'Javascript']

    def all_python_exercises(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.Id,
            e.Name,
            e.ExLanguage
            from Exercise e
            """)

            all_python_exercises = db_cursor.fetchall()

            [print(e) for e in all_python_exercises if e.language == 'Python']

    def all_java_exercises(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.Id,
            e.Name,
            e.ExLanguage
            from Exercise e
            """)

            all_java_exercises = db_cursor.fetchall()

            [print(e) for e in all_java_exercises if e.language == 'Java']

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(
                row[1], row[2], row[3], row[5]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.Id,
                s.FirstName,
                s.LastName,
                s.SlackHandle,
                s.CohortId,
                c.Name
            from Student s
            join Cohort c on s.CohortId = c.Id
            order by s.CohortId
            """)

            all_students = db_cursor.fetchall()

            [print(s) for s in all_students]

    def all_instructors(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(
                row[1], row[2], row[3], row[5]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select i.Id,
                i.FirstName,
                i.LastName,
                i.SlackHandle,
                i.CohortId,
                c.Name
            from Instructor i
            join Cohort c on i.CohortId = c.Id
            order by i.CohortId
            """)

            all_instructors = db_cursor.fetchall()

            [print(i) for i in all_instructors]

reports = StudentExerciseReports()
print()
reports.all_cohorts()
print()
reports.all_exercises()
print()
reports.all_javascript_exercises()
print()
reports.all_python_exercises()
print()
reports.all_java_exercises()
print()
reports.all_students()
print()
reports.all_instructors()
