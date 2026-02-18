#write a program to figure out factorial of given number

def factorial(number):
    if number==0 or number==1:
        return 1
    else:
        return number * factorial(number - 1)
    
number = int(input("enter number :"))
result = factorial(number)
print(f"{number}! = {result}")