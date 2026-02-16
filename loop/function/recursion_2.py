# write a program to figure out binary of given decimal number 

def tobinary(number):
    if number>0:
        reminder = number % 2
        number = number // 2
        tobinary(number)
        print(reminder,end=' ')

number = int(input("enter number :"))
tobinary(number)