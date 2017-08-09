class User:
    """User will be our superclass. It will contain the general properties
       and methods that will be available to our more specialized types of
       Users."""

    def __init__(self, username, first_name, last_name):
        self.__username = username
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = username + '@pitt.edu'

    def __str__(self):
        return '{} {} Username: {}'.format(self.__first_name, self.__last_name,
            self.__username)

    def get_username(self):
        return self.__username

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name
        
    def get_email(self):
        return self.__email    

    def set_username(self, username):
        self.__username = username

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name
        
    def can_edit_grades(self):
        return False
        
    
