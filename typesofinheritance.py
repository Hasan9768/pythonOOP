
class A:
    def diplay1(self):
        print("I am in A class")

class B:
    def diplay2(self):
        print("I am in B class")

class C(A,B):

    pass

obj=C()
obj.diplay1()
obj.diplay2()
