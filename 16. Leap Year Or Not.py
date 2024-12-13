#2.	Write a python Program to check whether a year is LEAP YEAR or not.

def CheckLeapYear(year):
    if((year%400==0)or(year%100!=0)and(year%4==0)):
        print("given is leap year")
    else:
        print("given year is not a leep year")

year=int(input("enter the year : "))
CheckLeapYear(year)