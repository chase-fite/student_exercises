from nss_person import NSSPerson

class Instructor(NSSPerson):

    def __init__(self, first_name, last_name, slack_handle, cohort, specialty):
        super().__init__(first_name, last_name, slack_handle, cohort)
        self.__specialty = specialty
    
    def assign_exercise(self, student, exercise):
        student.add_exercise(exercise)
    