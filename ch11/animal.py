class Animal:

    def __init__(self, species):
        self.__species = species

    def get_species(self):
        return self.__species

    def __str__(self):
        return 'I am a {}'.format(self.__species)
