# Note that we are importing the user module so we can use the User class
# defined there.
import user

class Student(user.User):
    """Notice the parentheses above with user.User inside of it. This is where
    we are telling Python that the Student class definition inherits from
    the User class definition defined in the user module. That means that
    a Student will have all of the methods and properties available to a
    User without us needing to define them explicitly."""

    def __init__(self, username, first_name, last_name, major, class_standing):
        """Subclass __init__ methods should accept all of the same parameters
        as their superclass. But, they can also accept additional parameters
        after those defined by the superclass. Here, we are adding major
        and class standing."""

        # The following line is going to call the superclass's constructor
        # __init__ method explicitly. Notice how we actually call __init__ and
        # pass the self argument. This is different from how we normally
        # instantiate objects. Python has another way to do this which we will
        # use in our Instructor class.
        user.User.__init__(self, username, first_name, last_name)
        self.__major = major
        self.__class_standing = class_standing

    def __str__(self):
        """Because a Student object has additional properties, we want to
        override the __str__ method from the superclass to include them in the
        response. We do this by first getting the superclass's __str__ method
        return value, then concating some extra information onto it before
        returning."""
        response = user.User.__str__(self)
        response += ' Major: {} Class Standing: {}'.format(self.__major,
            self.__class_standing)
        return response

    def set_username(self, username):
        user.User.set_username(self, 'S' + username)

    def get_major(self):
        return self.__major

    def get_class_standing(self):
        return self.__class_standing

    def set_major(self, major):
        self.__major = major

    def set_class_standing(self, class_standing):
        self.__class_standing = class_standing
