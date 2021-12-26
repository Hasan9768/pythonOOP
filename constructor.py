
class Student:
    id=" "
    gpa=" "

    def __init__(self,id,gpa):
        self.id=id
        self.gpa= gpa
    def display(self):
        print(f"ID:{self.id}, GPA:{self.gpa}")


akil=Student(101,3.6)
akil.display()
washi=Student(102,3.6)
washi.display()



'''
akil=Student()
#print(isinstance(akil,Student))

akil.id=101
akil.gpa=3.65
print(f"ID:{akil.id}, GPA:{akil.gpa}")

washi=Student()
#print(isinstance(akil,Student))

washi.id=102
washi.gpa=3.65
print(f"ID:{washi.id}, GPA:{washi.gpa}")



        self.id=id
        self.gpa=gpa

    def display(self):
        print(f"ID:{self.id}, GPA:{self.gpa}")

    akil=Student(101,3.6)
    akil.display()
    washi=Student(102,3.6)
    washi.display()
'''