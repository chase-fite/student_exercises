

class Cohort:

    def __init__(self, name):
        self.__name = name
        self.__students = []
        self.__instructors = []

    def __repr__(self):
        return f'{self.__name}'