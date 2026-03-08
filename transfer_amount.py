#write a program to accept transfer amount from user & transfer amount. 
# if amount>balance or greater then daily transfer limit raise custom exception 
class transferlimitexception(Exception):
    pass
balance = 125000
daily_limit = 100000

amount = int(input("enter transfaring amount :"))
try:
    if amount>balance:
        raise transferlimitexception("insufficient balance")
    elif amount>daily_limit:
        raise transferlimitexception("trasfer daily limit exceeded")
    else:
        balance = balance - amount
        print("transaction is succesfully")
        print('remaining balance in your account :',balance)
except transferlimitexception as error:
    print(error)
finally:
    print("thank you for banking with us")