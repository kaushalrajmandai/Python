class Student:
    def _init_(self, name, roll):
        self.name = name
        self.roll = roll
        print("Name", name)
        print("Roll no", roll)

s1 = Student("Student", 123)