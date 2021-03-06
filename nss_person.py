

class NSSPerson:
    
    def __init__(self, first_name, last_name, slack_handle, cohort):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__slack_handle = slack_handle
        self.__cohort = cohort

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def slack_handle(self):
        return self.__slack_handle

    @property
    def cohort(self):
        return self.__cohort