#!/usr/bin/python3
sentence = input('Type something: ')
for i in range(len(sentence)):
    print('The {} letter of your sentence is {}'.format(
        i, sentence[i]))

for i in range(1, 101):
    print(i, '*' * i)

#You can even make range count backwards
for c in range(10, -1, -1):
    print('Countdown to liftoff in...', c)
