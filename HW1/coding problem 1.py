# Zachary Arroyo
# UHID 1810267

# Homework 1 - Coding Problem 1

cmonth = int(input("Enter the current month: "))
cday = int(input("Enter the current day: "))
cyear = int(input("Enter the current year: "))

bmonth = int(input("Enter the birth month: "))
bday = int(input("Enter the birth day: "))
byear = int(input("Enter the birth year: "))
age = cyear - byear - 1

if cmonth >= bmonth:
    if cday >= bday:
        age += 1

if cmonth == bmonth:
    if cday == bday:
        print("Happy birthday!")
print(f"You are {age} years old.")