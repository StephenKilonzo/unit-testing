from src.employee import Employee
from src.student import Student

E1 = Employee('Steve', 'Kilo', '12', 2000)
def test_full_name():
    assert E1.full_name() == 'Steve Kilo'

def test_salary():
    assert E1.get_salary() == '2000'

def test_get_id():
    S1 = Student('Steve', 'Kilo', '12')
    assert S1.get_student_id() == '12'