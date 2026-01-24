#write a program to figure out whether given number  is perfect number or not
num = int(input("enter number :"))
i = 1
sum = 0

while i < num:
    if num % i == 0:
        sum = sum + i
    i+=1

if num == sum:
    print("number is a perfect number")
else:
    print("num is not perfect number")