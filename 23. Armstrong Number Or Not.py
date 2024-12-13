#20.	Write a python Program to Check whether a number is Armstrong Number or not.

n=int(input("Enter a number"))
count=0
a=n
b=n
while a>0:
    count=count+1
    a=int(a/10)
sum=0
x=1
while b>0:
    temp=b%10
    x=1
    i = count
    while i>0:
        x=x*temp
        i=i-1
    sum=sum+x
    print(x)
    b=int(b/10)
if sum==n:
    print("The given number is amstrong")
else:
    print("The given number is not amstrong")