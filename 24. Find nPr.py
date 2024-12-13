#21.	Write a python Program to Find nPr (Permutation) of a number.

print("For permutations (nPr)")
n=int(input("Enter n value: "))
r=int(input("Enter r value: "))

def fact(n):
    s=1
    for i in range (1,n+1,1):
        s=s*i
    return s

numerator=(fact(n))
denominator=fact(n-r)
print(numerator/denominator)
