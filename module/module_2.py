import bank

amount = int(input("enter deposit amount :"))
print("balance before deposit amount :",bank.balance)
bank.deposit(amount)
print("balance after deposit amount :",bank.balance)

amount = int(input("enter withdrawal amount :"))
print("balance before withdraw amount :",bank.balance)
bank.withdrawal(amount)
print("balance after withdrawal amount :",bank.balance)