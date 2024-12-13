#dictionary is a key-value pair
#no indexing
#key is used to retrive the data

#Printing the type of data
Student={"Reg.no":31954,"name":"Venkat","Branch":"Cse","cgpa":9.47}
print(type(Student))
#print only keys in dictionary
print("Keys in dictionary : ",Student.keys())

#print ony values in dictionary
print("Values in Dictionary :",Student.values())

#print the whole data in sequence
print(Student)

#Print individuals key-values
print("Registration number is ",Student["Reg.no"])
print("Student name is ",Student["name"])
print("Student branch is ",Student["Branch"])
print("Student CGPA is ",Student["cgpa"])

#Print using for loop,
#Type 1
print("\nPrinting using for loop,\n")
for x in Student.keys():
    print(x," = ",Student[x])
#Type 2
for x,y in Student.items():
  print(x,y)

#print type of keys using for loop
for i in Student.keys():
    print(i,"Type is ",type(i))

#print type of values using for loop
for i in Student.values():
    print(i,"Type is ",type(i))

#print type of both keys and values using for loop
for i in Student:
    print(i,"its type is ",type(i)," : ",Student[i],"its type is ",type(Student[i]))

#copy the values from dictionary to list
S1=[]
Student={"Reg.no":31954,"name":"Venkat","Branch":"Cse","cgpa":9.47}
for i in Student:
    S1.append(Student[i])
for i in S1:
    print(i)

#copy the keys from dictionary to list
S2=[]
Student={"Reg.no":31954,"name":"Venkat","Branch":"Cse","cgpa":9.47}
for i in Student:
    S2.append(Student[i])
for i in S2:
    print(i)