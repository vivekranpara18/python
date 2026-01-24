'''
write a program to figure out whether given number is prime number or not 
'''
number = int(input("enter number :"))
divisor = 2
while number<divisor:
    reminder = number % divisor
    if reminder == 0:
        print("it is not a prime number")
    else:
        divisor += 1

print("it is prime number")