

class Student:

    def __init__(self, first_name, last_name, slack_handle, cohort):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__slack_handle = slack_handle
        self.__cohort = cohort
        self.__current_exercises = []

    def full_name(self):
        return f'{self.__first_name} {self.__last_name}'

    def add_exercise(self, exercise):
        self.__current_exercises.append(exercise)

    def list_current_exercises(self):
        exercise_list = []
        for exercise in self.__current_exercises:
            exercise_list.append(f'{exercise.name} - {exercise.language}')
        return exercise_list