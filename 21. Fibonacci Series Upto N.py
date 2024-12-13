#19.	Write a python Program to Print Fibonacci Series up to N Term.

n=int(input())
f=0
l=1
fib=[0,1]
for i in range (2,n):
    c=fib[i-1]+fib[i-2]
    fib.append(c)
print(fib)
