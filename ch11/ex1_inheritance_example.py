#!/usr/bin/python3

# Import the modules where our classes are defined
import instructor
import student
import user

def do_user_stuff():
    print('\n---- Doing User stuff----\n')
    # Build some User objects
    u1 = user.User('sss1', 'Sally', 'Student')
    u2 = user.User('bbb1', 'Billy', 'Batts')

    print('Calling __str__ for User objects')
    print('u1=', u1)
    print('u2=', u2)

    print('Calling set_username for User objects')
    u1.set_username('sss0001')
    u2.set_username('bbb0001')

    print('Calling get_username for User objects')
    print('u1.get_username()=', u1.get_username())
    print('u2.get_username()=', u2.get_username())

    # Return User objects in a list
    return [u1, u2]


def do_student_stuff():
    print('\n---- Doing Student stuff----\n')
    # Build some Student objects
    s1 = student.Student('sss2', 'Samantha', 'Student', 'CS', 'Freshman')
    s2 = student.Student('raj1', 'Richard', 'Jones', 'Math', 'Junior')

    print('Calling __str__ for Student objects')
    print('s1=', s1)
    print('s2=', s2)

    print('Calling set_username for Student objects')
    s1.set_username('sss0002')
    s2.set_username('raj0001')

    print('Calling get_username for Student objects')
    print('s1.get_username()=', s1.get_username())
    print('s2.get_username()=', s2.get_username())

    print('Calling set_major and get_major for a Student object')
    s2.set_major('CS')
    print('s2.get_major()=', s2.get_major())

    # Return Student objects in a list
    return [s1, s2]


def do_instructor_stuff():
    print('\n---- Doing Instructor stuff----\n')
    # Build some Student objects
    i1 = instructor.Instructor('mts1', 'Mary', 'Smith', 'Psychology', True)
    i2 = instructor.Instructor('hsa1', 'Harold', 'Allen', 'Biology', False)

    print('Calling __str__ for Instructor objects')
    print('i1=', i1)
    print('i2=', i2)

    print('Calling set_username for Instructor objects')
    i1.set_username('mts0001')
    i2.set_username('hsa0001')

    print('Calling get_username for Instructor objects')
    print('i1.get_username()=', i1.get_username())
    print('i2.get_username()=', i2.get_username())

    print('Calling set_tenured and get_tenured for an Instructor object')
    i2.set_tenured(True)
    print('i2.get_tenure()=', i2.get_tenured())

    # Return Instructor objects in a list
    return [i1, i2]


def do_polymorphism(users):
    print('\n---- Doing Polymorphism stuff----\n')
    for u in users:
        # __str__ is a polymorphic method. Our subclasses overrode the default
        # implementation from User with their own custom output. But, we can use
        # them in a loop here and Python knows the right implementation to use.
        print('u=', u)

        # The isinstance function is a Python built-in that can tell us from
        # which class definition an object comes from. You supply it with two
        # arguments. The first is the object you want to check and the second
        # is a class definition (ie. users.User).

        # isinstance should always return True when checking an object against
        # its actual class or superclass
        print('is a User', isinstance(u, user.User))

        u.set_username(u.get_username() + '000')

        # isinstance will return False if the first argument is not an object
        # of the second argument's class (ie. an Instructor is a User, but not
        # a Student)
        print('is a Student', isinstance(u, student.Student))
        print('is an Instructor', isinstance(u, instructor.Instructor))
        print(u)



def main():
    """Our main function will create an empty list for Users. Each function
    will return a list containing objects that derive from the User class.
    We'll add those items to our users list and them demonstrate polymorphism.
    """
    users = []
    users += do_user_stuff()
    users += do_student_stuff()
    users += do_instructor_stuff()

    do_polymorphism(users)


main()
