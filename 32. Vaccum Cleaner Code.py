current={"a":-1,"b":-1}
goal={"a":0,"b":0}
n=len(current)
count=0
for i in current:
    current[i]=int(input("Enter the present state of location: "))
    if(current[i]==1):
        count=count+1
locate=input("\nEnter the current location: ")
print("\n Vaccume cleaner started,")
def move(locate):
    if(locate=="a"):
        locate="b"
    else:
        locate="a"
    return locate
def vca(current,goal,locate):
    if (locate == "a"):
        if (current[locate] == 1):
            current[locate] = goal[locate]
            print("Cleanning in process...,", locate, "is cleaned..!")
        else:
            print(locate, " is already cleaned...!")
    else:
        if (current[locate] == 1):
            current[locate] = goal[locate]
            print("Cleanning in process...,",locate, "is cleaned..!")
        else:
            print(locate, " is already cleaned...!")
while n>0:
    vca(current, goal, locate)
    locate=move(locate)
    count=count+1
    n=n-1
print("\nAfter vaccum cleaner worked, current status of locations ->",current)
print("Number of steps in count ->",count)