# If else conditional statements
x=int(input("Enter the value = "))
y=int(input("Enter the value = "))
if(x>y):
    print("x = ",x,"is greater than y = ",y)
else:
    print("x = ",x,"is lesser than y = ",y)


#For loop,
#1. for(i=0;i<10;i++)
for i in range(10):
    print(i)
print()
#2. for(i=5;i<10;i++)
for i in range(5,10):
    print(i)
print()
#3. for(i=1;i<10;i=i+2)
for i in range(1,10,2):
    print(i)
print()
#4. for(i=20;i>10;i=i-2)
for i in range(20,10,-2):
    print(i)
print()

#knowing data types of given data by hard core values
regno=1
name="sai"
course="PFSD"
secno=16
time=1.06730
print("Type of Registration = ",type(regno))
print("Type of Name = ",type(name))
print("Type of Course = ",type(course))
print("Type of Section = ",type(secno))
print("Type of Time = ",type(time))

#knowing data types of reading data from keyboard
branch=input("Enter the Branch you belog to is ")
print("Branch you belong to is ",branch)
x=input("Enter values of x = ")
print("Value of x is ",type(x))
#"TYPE CAST" is doing because by default reading is in datatype of string so, we need to convet it to required datatype.
x=int(input("Enter values of x = "))
print("Value of x is ",type(x))
x=float(input("Enter values of x = "))
print("Value of x is ",type(x))
x=bool(input("Enter values of x = "))
print("Value of x is ",type(x))
