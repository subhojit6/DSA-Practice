class Student():

    school = "Sri chaitanya college"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old.")

student1 = Student("Subhojit", 24)
student2 = Student("Rahul", 19)

student1.introduce()
student2.introduce()

student1.school = "XYZ college"

print(student1.school)
print(student2.school)
print(Student.school)