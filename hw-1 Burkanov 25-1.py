class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
            print(f"{self.fullname}\n{self.age}\n{self.is_married}\n")

    def __str__(self):
            return f"Name:{self.fullname}\n" \
                   f"Age:{self.age}\n" \
                   f"Marriage:{self.is_married}\n"

person1 = Person("Dosya", "19", "no")
print(person1)
person2 = Person("Kuba", "20", True)
print(person2.introduce_myself())

class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def average(self):
        print(sum(self.marks) // len(self.marks))


class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience=3):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.salary = 10000

    def teacher_cash(self):
        if self.experience > 3:
            new_salary = self.salary + ((self.salary / 100 * 5)*(self.experience - 3))
            return new_salary

k = Teacher("pasha", "yes", True, 10)
print(f"{k.fullname}, {k.salary},{k.age},{k.is_married}")
print(k.teacher_cash())

def create_students():
    student1 = Student("Beka",20,False, marks={
        "История":5,
        "Алгебра":3,
        "Физ-ра":4,
        "Физика":3,
        "Химия":2
    })
    student2 = Student("Akyl", 19, False, marks={
        "История": 5,
        "Алгебра": 5,
        "Физ-ра": 5,
        "Физика": 4,
        "Химия": 4
    })
    student3 = Student("Bek", 23, True, marks={
        "История": 3,
        "Алгебра": 3,
        "Физ-ра": 3,
        "Физика": 3,
        "Химия": 3
    })

    result = [student1, student2, student3]
    return result

student = create_students()
for i in student:
    list = []

    for marks in i.marks.values():
        list.append(marks)
    print(f"Name:{i.fullname}\n"
          f"Age:{i.age}\n"
          f"Marriage:{i.is_married}\n"
          f"Average:{sum(list) / len(list)}\n")