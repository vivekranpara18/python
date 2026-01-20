'''write a program to accept 2 number from user. and accept choice for operations.
operations will be addition, subtraction, multiplication, division
do operation and display result as per user choice about operation using if elif else statements.
'''
no1 = int(input("enter first number :"))
no2 = int(input("enter second number :"))

choice = str(input("enter your choice :"))

if choice=='+':
    print("sum is :",(no1+no2))
elif choice=='-':
    print("subtraction is :",(no1-no2))
elif choice=='*':
    print("multiplication is :",(no1*no2))
elif choice=='/':
    print("division is :",(no1/no2))
else:
    print("invalid operation")