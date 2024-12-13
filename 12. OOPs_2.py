#Inheritance
#Inheritance allows us to define class that inherits all the methods and properties from another class.
#Parent class is the class being inherited from, also called base class.
#Child class is the class that inherits from another class, also called derived class.

#Using pass key word
#Method 1,
class Person:
    def __init__(self,i,n):
        self.id=i
        self.name=n
    def displaydata(self):
        print(self.id," ",self.name)
class Staff(Person):
    #pass: Use this "pass" keyword when you don't want to add any other properties or methods to the class.
    pass
ob=Staff(20,"SKKS")
ob1=Person(30,"SSNBR")
ob.displaydata()
ob1.displaydata()

#Method 2,
class Person1:
    def __init__(self,i,n):
        self.id=i
        self.name=n
class Staff(Person1):
    def displaydata(self):
        print(self.id," ",self.name)
ob2=Staff(23,"SKK SHARMA")
ob3=Staff(34,"SRIPADA SNBR")
ob2.displaydata()
ob3.displaydata()
print()
#Use of "super" key word,
#super: It is used to called the methods in parent class from child class.
#Method 1,
class Person2:
    def __init__(self,i,n):
        self.id=i
        self.name=n
    def displaydata(self):
        print(self.id," ",self.name)
class Staff(Person2):
    def __init__(self,i,n):
        super().__init__(i,n)
    def displaydata(self):
        super().displaydata()
ob4=Staff(45,"Sripada KK SHARMA")
ob5=Staff(32,"SRIPADA S NagaBR")
ob4.displaydata()
ob5.displaydata()

#Method 2,
class Parent:
    def function1(self):
        print("Parent class")
class Child(Parent):
    def function1(self):
        super().function1()
        print("Child class")
ob6=Child()
ob6.function1()
ob7=Parent()
ob7.function1()

