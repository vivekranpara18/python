balance = 1000
def deposit(amount):
    global balance
    if amount<0:
        print("amount can not be less than 0")
    else:
        balance = balance + amount

def withdrawal(amount):
    global balance
    if amount > balance:
        print("Withdrawal Failed: Insufficient Balance.")
    else:
        balance = balance - amount