class Student:

    def __init__(self, name, major, class_standing):
        self.__name = name
        self.__major = major
        self.__class_standing = class_standing
        
    def __str__(self):
        return 'Name: {}, Major: {}, Class: {}'.format(
            self.__name, self.__major, self.__class_standing
        )
        
    def set_class_standing(self, new_standing):
        if new_standing in ('Freshman', 'Sophomore', 'Junior', 'Senior'):
            self.__class_standing = new_standing            


def main():        
    s1 = Student('Jason', 'CS', 'Junior')
    s2 = Student('Sally', 'Bio', 'Freshman')
    s3 = Student('Billy', 'Chemistry', 'Senior')


if __name__ == '__main__':
    main()
