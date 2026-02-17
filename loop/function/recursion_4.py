#write a program to figure out hexadcimal of given decimal number

def tohexadecimal(number):
    digits = "0123456789ABCDEF"
    
    if number > 0:
        reminder = number % 16
        number = number // 16
        tohexadecimal(number)
        print(digits[reminder],end=' ')

number = int(input("enter number :"))

tohexadecimal(number)