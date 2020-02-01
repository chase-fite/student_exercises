from exercise import Exercise
from cohort import Cohort
from student import Student
from instructor import Instructor
from random import randint

exercise_1 = Exercise("e1", "python")
exercise_2 = Exercise("e2", "python")
exercise_3 = Exercise("e3", "javascript")
exercise_4 = Exercise("e4", "javascript")

cohort_1 = Cohort("cohort 1")
cohort_2 = Cohort("cohort 2")
cohort_3 = Cohort("cohort 3")

chase = Student("chase", "f", "chase_slack", "cohort 1")
corri = Student("corri", "g", "corri_slack", "cohort 3")
matt = Student("matt", "b", "matt_slack", "cohort 3")
ryan = Student("ryan", "b", "ryan_slack", "cohort 3")

brad = Instructor("brad", "s", "brad_slack", "cohort 1", "nerd jokes")
josh = Instructor("josh", "d", "josh_slack", "cohort 2", "embarassing people")
kayla = Instructor("kayla", "s", "kayla_slack", "cohort 3", "explanations")

exercise_list = [exercise_1, exercise_2, exercise_3, exercise_4]
student_list = [chase, corri, matt, ryan]
instructor_list = [brad, josh, kayla]

for instructor in instructor_list:
    for student in student_list:
        for i in range(2):
            rand_num = randint(0, 3)
            instructor.assign_exercise(student, exercise_list[rand_num])

for student in student_list:
    for exercise in student.list_current_exercises():
        print(f'{student.full_name()}: {exercise}')