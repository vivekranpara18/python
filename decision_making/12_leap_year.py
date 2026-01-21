# write a program to find out whether given year is leap year or not
# https://www.wikihow.com/Calculate-Leap-Years

year = int(input("enter year :"))

if year < 1:
    print("invalid year")
else:
    reminder1 = year % 4
    reminder2 = year % 100
    reminder3 = year % 400

    if reminder1 == 0 and reminder2 != 0:
        print("given year is leap year")
    elif reminder2 == 0 and reminder3 == 0:
        print("given year is leap year")
    else:
        print("given year is not a leap year")