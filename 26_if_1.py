#write a program to calculate profit and loss for sell product using if statement

purchase_price = float(input("enter purchase price of product :"))
sell_price = float(input("enter selling price of product :"))

difference = sell_price - purchase_price

if difference > 0:
    print("profit is :",difference)

if difference < 0:
    print("loss is :",difference)

if difference == 0:
    print("no profit no loss")