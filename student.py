from nss_person import NSSPerson

class Student(NSSPerson):

    def __init__(self, first_name, last_name, slack_handle, cohort):
        super().__init__(first_name, last_name, slack_handle, cohort)
        self.__current_exercises = []

    def add_exercise(self, exercise):
        self.__current_exercises.append(exercise)

    @property
    def current_exercises(self):
        exercise_list = []
        for exercise in self.__current_exercises:
            exercise_list.append(f'{exercise.name} in {exercise.language}')
        return exercise_list

    def __repr__(self):
        return f'{self.first_name} {self.last_name} is in {self.cohort}'