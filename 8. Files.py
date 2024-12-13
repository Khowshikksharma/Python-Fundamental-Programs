# Files,
#Files is used to store data permanently.

# Modes in file,
#   r -> to read data from file
#   w -> to write new data in file, while previous data will be erased
#   a -> to write the data at last in file

#Write data in file
a=3
b=5
c=str(a+b)

file=open("test.txt","w")
file.write("Siva Sankara Vara Prasad.\n")
file.write("Name of this file is 'test'.\n")
file.write("sum of a=3 and b=5 is ")
file.write(c)

#Read data from file
file1=open("test.txt","r")
for i in file1:
    print(i,end=" ")

#copy data from one file to other file
file1=open("test.txt","r")
file2=open("result.txt","w")
for i in file1:
    file2.write(i)

#Appending data in file
file1=open("test.txt","r")
file2=open("result.txt","a")
for i in file1:
    file2.write(i)
