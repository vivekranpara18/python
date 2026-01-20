#write a program to find out whether given year is millennium year or not. using if else decision making statements.

year = int(input("enter year :"))

if year % 1000 == 0:
    print("millennium year")
else:
    print("not millennium year")