

class Student:
    id=" "
    gpa=" "

  def set_value(self,id,gpa):
   self.id=id
   self.gpa=gpa

def display(self):
    print(f"ID:{self.id}, GPA:{self.gpa}")

akil=Student()
#print(isinstance(akil,Student))
akil.set_value(101,3.65)
#akil.id=101
#akil.gpa=3.65
#print(f"ID:{akil.id}, GPA:{akil.gpa}")
akil.display()
washi=Student()
#print(isinstance(akil,Student))
washi.set_value(102,3.65)
#washi.id=102
#washi.gpa=3.65
#print(f"ID:{washi.id}, GPA:{washi.gpa}")
washi.display()

