#Exception Handling

#Exceptions are 2 types,
#    1. Defined by the user Exception
#    2. Bulitin Exception

# Theory: Program stopped for one error at any line while in exception,program stopped when error is occured.

#Userdefined Exception,
student=[1,"smith","cSe",4.5]
x=len(student)
print("lenght of student list is",x)
for i in range(x+1):
    try:
        print(student[i])
    except:
        print("Index out of range")
#Raising an Exception
x=int(input("Enter the x value:"))
y=int(input("Enter the y value:"))
if (y==0):
    raise Exception("Denominator cannot be zero")
else:
    print("Division of two numbers is:",x/y)