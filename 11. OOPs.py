#Creating class
class Student:
    regno=30001
    name="Vishnavi"
    #indentation: In python it is an area which is used to represent begin and end inside any block
                # where blocks are functions, classes, for loop, while loop, etc....
#declaring the object of the class
ob=Student()
#printing the class variables
print("OB,")
print(" Registration number is",ob.regno)
print(" Name is",ob.name)

#Class Description (interveiw preparation),
    #All classes have a function called _init_(), which is always executed when the class is being intiated.
    #The _init_ method is like construction in C++ and Java. Construction are used to initialize the object's state.
    #Construction are used to initialize the data members of the class when an object of the class is created.
    #Whenever we defined
    #The first argument should be self, for every mehod in class.

#Creating _init_ method in class(unique method),
class Student1:
    def __init__(self, r, n):
        # n is formal parameter
        # r is register number
        self.regno = r
        self.name = n
ob1=Student1(31870,"V Uma Shankar")
ob2=Student1(31954,"S V S N S L P Khowshikk Sharma")
print("OB1,\n",ob1.regno," ",ob1.name)
print("OB2,\n",ob2.regno," ",ob2.name)

#Creating Methods in class,
class Student2:
    def __init__(self,regno,name):
        self.regno=regno
        self.name=name
    def displaydata(self):
        print(" Registration number :",self.regno)
        print(" Name :",self.name)
print("OB3,")
ob3=Student2(31955,"Tarun")
ob3.displaydata()
