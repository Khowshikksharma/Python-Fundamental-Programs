#5.	Write a python Program to check whether a number is PALINDROME NUMBER or not.

n=int(input())
s=0
t=n
while (n>0):
    r=n%10
    s=s*10+r
    n=int(n/10)
print(s)
if(t==s):
    print("yes")
else:
    print("no")