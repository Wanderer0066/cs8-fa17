import student

class GraduateStudent(student.Student):

    def __init__(self, name, graduation_year, major, thesis_title, advisor):
        super().__init__(name, graduation_year, major)
        self.__thesis_title = thesis_title
        self.__advisor = advisor

    def get_thesis_title(self):
        return self.__thesis_title

    def get_advisor(self):
        return self.__advisor

    def __str__(self):
        from_super = super().__str__()
        from_super += 'is advised by {} and is researching {}'.format(
            self.__advisor, self.__thesis_title)
        return from_super

