#22.	Write a python Program to Find nCr (Combination) of a number.

print("For combination (nPr)")
n=int(input("Enter n value: "))
r=int(input("Enter r value: "))

def fact(n):
    s=1
    for i in range (1,n+1,1):
        s=s*i
    return s

numerator=fact(n)
denominator1=fact(n-r)
denominator2=fact(r)
denominator=denominator2*denominator1
print(numerator/denominator)
