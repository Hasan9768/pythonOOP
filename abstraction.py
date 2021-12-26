From abc import ABC,abstractmethod

class Shape(ABC):
    def __init__(self,d1,d2):
        self.d1=d1
        self.d2=d2
    @abstractmethod
    def area(self):
        print("I am in method of shape class ")

class Triangle(Shape):
    def area(self):
        area=0.5*self.d1*self.d2
        print("Area of Triangle: ",area)

class Rectangle(Shape):
    def area(self):
        area=self.d1*self.d2
        print("Area of Rectangle: ",area)

t1=Triangle(10,20)
t1.area()
r1=Rectangle(20,30)
r1.area()