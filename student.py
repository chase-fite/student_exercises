from nss_person import NSSPerson

class Student(NSSPerson):

    def __init__(self, first_name, last_name, slack_handle, cohort):
        super().__init__(first_name, last_name, slack_handle, cohort)
        self.__current_exercises = []

    def add_exercise(self, exercise):
        self.__current_exercises.append(exercise)

    @property
    def current_exercises(self):
        return self.__current_exercises

    # def __repr__(self):
    #     return f'{self.first_name} {self.last_name} is in {self.cohort}'