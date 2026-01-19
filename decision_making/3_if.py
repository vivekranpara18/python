"""write a program to accept day of week (between 1 to 7) and then display name of day. 
    (use simple if decision making)
            input 1 : monday 
            input 2 : tuesday 
            input 7 : sunday 
"""

day = int(input("enter day :"))

if day == 1:
    print("monday")
if day == 2:
    print("tuesday")
if day == 3:
    print("wednesday")
if day == 4:
    print("thursday")
if day == 5:
    print("friday")
if day == 6:
    print("saturday")
if day == 7:
    print("sunday")
if day > 7 or day < 1:
    print("invalid")