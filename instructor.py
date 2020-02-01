from student import Student

class Instructor:

    def __init__(self, first_name, last_name, slack_handle, cohort, specialty):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__slack_handle = slack_handle
        self.__cohort = cohort
        self.__specialty = specialty
    
    def assign_exercise(self, student, exercise):
        student.add_exercise(exercise)
    