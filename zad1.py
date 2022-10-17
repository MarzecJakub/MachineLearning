class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        if (sum(self.marks) / len(self.marks) > 50):
            return True
        else:
            return False


kuba = Student("Jakub", [90, 40, 50, 50, 40, 50, 50, 50, 50])
print(kuba.is_passed())

michal = Student("Michal", [30, 20, 20, 30, 20, 70, 30, 10, 10])
print(michal.is_passed())
