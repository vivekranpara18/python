#write a program to find out elder brother from given two brother's age.

age1 = int(input("enter first brother age :"))
age2 = int(input("enter second brother age :"))

if age1 > age2:
    print("first brother is elder")
if age1 < age2:
    print("second brother is elder")