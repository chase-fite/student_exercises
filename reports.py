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

    def students_with_exercises(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            # conn.row_factory here
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                e.Id ExerciseId,
                e.Name,
                e.ExLanguage,
                s.Id,
                s.FirstName,
                s.LastName,
                s.SlackHandle,
                c.Name
            from Exercise e
            join StudentExercise se on se.ExerciseId = e.Id
            join Student s on s.Id = se.StudentId
            join Cohort c on s.CohortId = c.Id
            """)

            students_with_exercises = db_cursor.fetchall()

            students = dict()

            for row in students_with_exercises:

                if row[3] not in students:
                    students[row[3]] = Student(row[4], row[5], row[6], row[7])
                    students[row[3]].add_exercise(Exercise(row[1], row[2]))
                else:
                    students[row[3]].add_exercise(Exercise(row[1], row[2]))

            for key in students:
                print(f'{students[key].first_name} {students[key].last_name} is working on:')
                for exercise in students[key].current_exercises:
                    print(f'\t* {exercise}')       

            # for row in students_with_exercises:
            #     exercise_id = row[0]
            #     exercise_name = row[1]
            #     student_id = row[2]
            #     student_name = f'{row[3]} {row[4]}'

            #     if student_name not in exercises:
            #         exercises[student_name] = [exercise_name]
            #     else:
            #         exercises[student_name].append(exercise_name)

            # for key, value in exercises.items():
            #     print(f'{key} is working on:')
            #     for exercise in value:
            #         print(f'\t* {exercise}')

    def exercises_with_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            # conn.row_factory here
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                e.Id ExerciseId,
                e.Name,
                s.Id,
                s.FirstName,
                s.LastName
            from Exercise e
            join StudentExercise se on se.ExerciseId = e.Id
            join Student s on s.Id = se.StudentId
            """)

            exercises_with_students = db_cursor.fetchall()

            exercises = dict()

            for row in exercises_with_students:
                exercise_id = row[0]
                exercise_name = row[1]
                student_id = row[2]
                student_name = f'{row[3]} {row[4]}'

                if exercise_name not in exercises:
                    exercises[exercise_name] = [student_name]
                else:
                    exercises[exercise_name].append(student_name)

            for key, value in exercises.items():
                print(f'{key} is being worked on by:')
                for student in value:
                    print(f'\t* {student}')

    def assigned_exercises(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            # conn.row_factory here
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
            e.Name,
            i.FirstName,
            i.LastName
            from Exercise e
            join StudentExercise se on se.ExerciseId = e.Id
            join Student s on se.StudentId = s.Id
            join Instructor i on se.InstructorId = i.Id
            """)

            assigned_exercises = db_cursor.fetchall()

            # print(assigned_exercises)

            assignments = dict()

            for row in assigned_exercises:
                exercise_name = row[0]
                instructor_name = f'{row[1]} {row[2]}'

                if instructor_name not in assignments:
                    assignments[instructor_name] = [exercise_name]
                else:
                    assignments[instructor_name].append(exercise_name)

            for key, value in assignments.items():
                print(f'{key} has assigned:')
                for exercise in value:
                    print(f'\t* {exercise}')

reports = StudentExerciseReports()

# part four of student exercises
# print()
# reports.all_cohorts()
# print()
# reports.all_exercises()
# print()
# reports.all_javascript_exercises()
# print()
# reports.all_python_exercises()
# print()
# reports.all_java_exercises()
# print()
# reports.all_students()
# print()
# reports.all_instructors()

# student workload / part five

print()
reports.students_with_exercises()
print()
reports.exercises_with_students()
print()
reports.assigned_exercises()