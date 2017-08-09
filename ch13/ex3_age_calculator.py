class AgeCalculator:
    """This is a trivially simple class, but will demonstrate how we can write
       a backend module that our GUI interacts with."""

    def __init__(self):
        self.__age_in_years = 0
        self.__age_in_days = 0
        self.__age_in_hours = 0
        self.__age_in_seconds = 0

    def calculate(self, age_in_years):
        self.__age_in_years = age_in_years
        self.__age_in_days = self.__age_in_years * 365.25
        self.__age_in_hours = self.__age_in_days * 24
        self.__age_in_seconds = self.__age_in_hours * 60

    def get_age_in_days(self):
        return self.__age_in_days

    def get_age_in_hours(self):
        return self.__age_in_hours

    def get_age_in_seconds(self):
        return self.__age_in_seconds
