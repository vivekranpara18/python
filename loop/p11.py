#write a program to figure out whether given number  is armstrong number or not
number = int(input("enter number :"))
count = len(str(number))
sum = 0
number2 = number
while number2>0:
    reminder = number2 % 10
    sum += pow(reminder,count)
    number2 //= 10
if sum == number:
    print("it is a armstrong number")
else:
    print("it is not a armstrong number")