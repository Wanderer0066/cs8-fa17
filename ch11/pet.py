import animal

class Pet(animal.Animal):

    def __init__(self, species, name, owner):
        super().__init__(species)
        self.__name = name
        self.__owner = owner

    def set_name(self, name):
        self.__name = name

    def set_owner(self, owner):
        self.__owner = owner

    def get_name(self):
        return self.__name

    def get_owner(self):
        return self.__owner

    def __str__(self):
        response = 'My name is {}. '.format(self.__name)
        response += super().__str__()
        response += '. My owner is {}'.format(self.__owner)
        return response
