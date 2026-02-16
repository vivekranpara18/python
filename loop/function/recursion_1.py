# write a program to display 1 to 10 in reverse order 

def printnumber(number):
    if number>=1:
        print(number,end=' ')
        number = number - 1
        printnumber(number)

number = int(input("enter number :"))
printnumber(number)