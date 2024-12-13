#18.	Write a python Program to Find Reverse a String.

s=input("Enter any string: ")
c=0
ns=""
ns1=""
#Finding lenght of string without function
for i in s:
    c=c+1
print(c)
#Finding lenght of string using function
count=len(s)
print(count)

#Reversing string without default function (for loop)
for i in s:
    ns=i+ns
print(s)
print(ns)
#Reversing string without default function (while loop)
while count>0:
    ns1=ns1+s[count-1]
    count=count-1
#Reversing string using default function
print(s[::-1])