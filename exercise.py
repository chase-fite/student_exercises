

class Exercise:

    def __init__(self, name, language):
        self.__name = name
        self.__language = language

    @property
    def name(self):
        return self.__name

    @property
    def language(self):
        return self.__language