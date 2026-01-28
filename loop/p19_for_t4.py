#write a program to count digits in given string
string = str(input("enter string :"))
count = 0
for item in string:
    if item.isdigit():
        count+=1
print(count)