from .person import Person
class Student(Person):
    def __init__(self, first_name, last_name, student_id):
        super().__init__(first_name, last_name)
        self.student_id = student_id

    def get_student_id(self):
        return f'{self.student_id}'