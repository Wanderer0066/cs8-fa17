import pet

class Cat(pet.Pet):

    def __init__(self, name, owner, color):
        super().__init__('Cat', name, color)
        self.__color = color

    def get_color(self):
        return self.__color

    def make_sound(self):
        print('Meow meow')

    def __str__(self):
        response = super().__str__()
        response += '. My fur is {}'.format(self.__color)
        return response
