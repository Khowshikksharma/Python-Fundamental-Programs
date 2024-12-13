# TUPEL

t = (1, 2, 3, 4, 6, 7, 8, 9)
print(t)
y = list(t)
y[3] = 10
t = tuple(y)
print(t)

#Reading tuple using for loop
student=(16,"PFSD",2200031954,16,2.30,"Hero")
for i in student:
    # this area id=s called indentation in for loop
    print (i, "type is",type(i))
print(student)
print(type(student))

#scanning tuple
tup=tuple(input().split())
print(tup)

