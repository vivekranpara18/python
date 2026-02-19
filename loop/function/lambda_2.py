#write a program to calculate fahrenheit of given celsius using lambda function 

fahrenheit = lambda celsius : celsius * (9/5) + 32

celsius = int(input("enter celsius :"))

result = fahrenheit(celsius)
print(result)