#write a program to figure out whether given number  is composite number or not

number = int(input("enter number :"))
count = 0
i = 1

while i < number:
    if number % i == 0:
        count += 1
        
    i+=1

if count > 2:
    print("it is composite number")
else:
    print("it is not a composite number")