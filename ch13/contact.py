class Contact:

    def __init__(self, first_name, last_name, email, phone):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone = phone

    def __str__(self):
        return '{} {} {} {}'.format(self.__first_name, self.__last_name,
            self.__email, self.__phone)

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_email(self, email):
        self.__email = email

    def set_phone(self, phone):
        self.__phone = phone
