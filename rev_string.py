#Write a program to reverse a given string.

def reverse_str(string):
    return string[::-1]

string = input("enter string :")
s1 = reverse_str(string)
print(s1)