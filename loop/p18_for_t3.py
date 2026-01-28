#write a program to count words in given string
string = input("enter string :")
words = string.split()
count = 0
for item in words:
    count+=1
print(count)