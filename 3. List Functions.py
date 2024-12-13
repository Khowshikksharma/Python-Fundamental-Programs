# LIST

# Reading list using for loop

student = [16, "PFSD", 2200031954, 16, 2.30, "Hero"]
for i in student:
    # this area id=s called indentation in for loop
    print(i, "type is", type(i))
print(student)
print(type(student))

print()

kk = [12, "khowshikk", 34, 2.30, 23]
print("integers,")
for i in kk:
    if type(i) == int:
        print(i)
print()
print("floats,")
for i in kk:
    if type(i) == float:
        print(i)
print()
print("strings,")
for i in kk:
    if type(i) == str:
        print(i)

print()

# appending list
ll = [12, "khowshikk", 10.12, 2004, 12.2004, "sharma", "love u dad", "20.04.2020"]
l1 = []
l2 = []
for x in ll:
    if type(x) == str:
        l1.append(x)
    if type(x) == float:
        l2.append(x)
print("Previous list,\nll =", ll)
print("New list,\nl1 =", l1, "\nl2 =", l2)

# Adding 2 list
l = []
l = l1 + l2
print("Combination of 2 newlists,\nl =", l)

for i in range(len(l) - 1, -1, -1):
    print(l[i])

# Reversing list
print("Reverse printing of a list,\n l =", l[::-1])

print()

# Reading list elements using keyboard
print("Enter the integer values for list k,")
k = []
n = 5
for i in range(n):
    a = input()
    k.append(a)
print("\nNew list,k reading using keyboard,\nk =", k)

student = [16, "PFSD", 2200031954, 16, 2.30, "Hero"]
f=student.copy()
print(f)

f1=student.extend(student)


#scanning list
ll=list(input().split())
print(ll)

l = [1, 2, 3, 4, 5, 6, 3, 3, 3, 7, 8, 9]
print(l)

print(l.count(3))

l[1:3] = [10, 11]
print(l)

l.append(15)
print(l)

l.insert(5, 20)
print(l)

l.sort()
print(l)

k = [21, 22, 23]
print(l)
l.extend(k)
print(l)

l.remove(15)
print(l)

l.reverse()
print(l)

l.pop()
print(l)

l.clear()
print(l)
