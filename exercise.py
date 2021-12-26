# base,height(10,20)(20,30).... Calculate area

class Triangle:
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def Calculate_area(self):
        area=0.5*self.base*self.height
        print("Area :",area)

T1= Triangle(10,20)
T1.Calculate_area()
T2= Triangle(20,30)
T2.Calculate_area()