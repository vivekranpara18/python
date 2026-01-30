#write a program to create function that convert given fahrenheit into celsius

def fahrenheit(number):
    celsius=(number-32)*5/9
    return celsius

n1 = int(input("enter hahrenheit :"))
result = fahrenheit(n1)
print(result)