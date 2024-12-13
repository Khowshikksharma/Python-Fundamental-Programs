#Multiple inhertience

#subclass --> div, add, sub and mul
class ADD:
    def addition(sel,x,y):
        return x+y
class SUB:
    def subtraaction(self,x,y):
        return x-y
class MUL:
    def multiplication(self,x,y):
        return x*y
class DIV:
    def division(self,x,y):
        return x/y
class Subclass (ADD,SUB,MUL,DIV):
    pass
ob=Subclass()
x=12
y=6
print("Addition:",ob.addition(x,y))
print("Subtraction:",ob.subtraaction(x,y))
print("Multiplication:",ob.multiplication(x,y))
print("Divsion:",ob.division(x,y))


#Multilevel Inheritance
class A:
    def funA(self):
        print("class a")
class B(A):
    def funB(self):
        print("class b")
class C(B):
    def funC(self):
        print("class c")
print()
oba=A()
obb=B()
obc=C()
print("class A -->")
oba.funA()
print("class B-->")
obb.funA()
obb.funB()
print("class C-->")
obc.funA()
obc.funB()
obc.funC()

print()
#Method Overridding
class AA:
    def func(self):
        print("Class A function")
class BB(AA):
    def func(self):
        print("Class B function")
obA=AA()
obB=BB()
obA.func()
obB.func()

#Method Overloading: Class containing same function with differnt signature
class AAA:
    def func(self):
        print("Fuction with no arguments")
    def func(self,x):
        self.x=x
        print("Fuction with 1 arguments")
    def func(self,x,y):
        self.x = x
        self.y = y
        print("Fuction with 2 arguments")
ob1=AAA()




