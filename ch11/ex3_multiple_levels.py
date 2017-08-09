#!/usr/bin/python3

# Import the modules where our classes are defined
import cat
import dog


def main():
    """We'll create some Dog and Cat objects, each of which inherits from Pet,
    which in turn inherits from Animal. That means we can use any of the
    methods from the superclasses of Dog and Cat.
    """
    d1 = dog.Dog('Duke', 'Jason', 'Labrador Retriever')
    d2 = dog.Dog('Molly', 'Sally', 'German Shepherd')
    c1 = cat.Cat('Mittens', 'Susie', 'Calico')
    c2 = cat.Cat('Tabby', 'Sally', 'Orange')
    pets = [d1, d2, c1, c2]

    print('Print each Pet...')
    for p in pets:
      print(p)

    print('Making animal sounds...')
    for p in pets:
      p.make_sound()

    print('Change everyone\'s owner...')
    for p in pets:
        p.set_owner('Jill')
        print(p)


main()
