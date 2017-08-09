import pet

class Dog(pet.Pet):

    def __init__(self, name, owner, breed):
        super().__init__('Dog', name, owner)
        self.__breed = breed

    def get_breed(self):
        return self.__breed

    def make_sound(self):
        print('Woof woof')

    def __str__(self):
        response = super().__str__()
        response += '. I am a {}'.format(self.__breed)
        return response
