# write a program to figure out octal of given decimal number

def tooctal(number):
    if number>0:
        reminder = number % 8
        number = number // 8
        tooctal(number)
        print(reminder,end=' ')

number = int(input("enter number :"))

tooctal(number)