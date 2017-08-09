# Note that we are importing the user module so we can use the User class
# defined there.
import user

class Instructor(user.User):
    """Notice the parentheses above with user.User inside of it. This is where
    we are telling Python that the Instructor class definition inherits from
    the User class definition defined in the user module. That means that
    a Instructor will have all of the methods and properties available to a
    User without us needing to define them explicitly."""

    def __init__(self, username, first_name, last_name, department, tenured):
        """Subclass __init__ methods should accept all of the same parameters
        as their superclass. But, they can also accept additional parameters
        after those defined by the superclass. Here, we are adding major
        and class standing."""

        # There's a cleaner way to call a superclass's method that's familiar
        # if you've used a language like Java. You can use the super() function
        # followed by the name of the method you want to call (__init__) in
        # our case and it will refer to the superclass's method. There are some
        # pitfalls to be mindful of but none that we will encounter in the scope
        # of this class.
        super().__init__(username, first_name, last_name)
        self.__department = department
        self.__tenured = tenured
        self.__can_edit_grades = True

    def __str__(self):
        """Because an Instructor object has additional properties, we want to
        override the __str__ method from the superclass to include them in the
        response. We do this by first getting the superclass's __str__ method
        return value, then concating some extra information onto it before
        returning."""
        response = super().__str__()
        response += ' Department: {} Tenured?: {}'.format(self.__department,
            self.__tenured)
        return response

    def get_department(self):
        return self.__department

    def get_tenured(self):
        return self.__tenured

    def set_department(self, department):
        self.__department = department

    def set_tenured(self, tenured):
        self.__tenured = tenured
        
    def can_edit_grades(self):
        return self.__can_edit_grades
        
    def set_can_edit_grades(self, can_edit_grades):
        self.__can_edit_grades = can_edit_grades
