#7.	Write a python Program to check whether a number is PERFECT NUMBER or not.

num=int(input("enter the number : "))
sum=0
for i in range(1,num):
    if(num%i==0):
        sum=sum+i
if(sum==num):
    print("given number is perfect  number")
else:
     print("given number is not a perfect number")