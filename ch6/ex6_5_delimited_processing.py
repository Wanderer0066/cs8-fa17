#!/usr/bin/python3
import random

FILE_NAME = 'grades.txt'

username_dict = {}

def sort_by_grade(student_grade):
    return student_grade['grade']

f = open(FILE_NAME)
o = open(FILE_NAME + '_completed.txt', 'w')
for line in f:
    line = line.rstrip()    
    parts = line.split('\t')
    student_grade = {}
    student_grade['name'] = parts[1] + ' ' + parts[0]   
    student_grade['username'] = parts[2]        
    student_grade['grade'] = random.randint(90, 100)
    
    if student_grade['username'] not in username_dict:
        username_dict[student_grade['username']] = []
        
    username_dict[student_grade['username']].append(student_grade)
    
    print(student_grade)
    
    #o.write('{},{}\n'.format(username, grade))
    
while True:
    student_id = input('Lookup a student by ID: ')
    if student_id in username_dict:
        username_dict[student_id].sort(key=sort_by_grade)            
        for g in username_dict[student_id]:
            print(g)
    else:
        print(student_id, 'is not found')
    
f.close()
#o.close()

    
