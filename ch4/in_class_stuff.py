#!/usr/bin/python3
sentence = input('Type something: ')
print(len(sentence), 'characters in sentence')
for i in range(len(sentence)):
    print('The {} letter of your sentence is {}'.format(
        i, sentence[i]))
        
for i in sentence:
    print('The letter of your sentence is {}'.format(i))

start = int(input('Where to start? '))
stop = int(input('Where to stop? '))
step = int(input('How many? '))

for i in range(start, stop, step):
    print(i, '*' * i)

