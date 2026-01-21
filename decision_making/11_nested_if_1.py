# write a program to find out which is cheaper product to purchase from 2 product's weight and price. 
# also display how much cheaper per gram 

price1 = float(input("enter 1st product price :"))
weight1 = float(input("enter 1st product weight :"))

price2 = float(input("enter 2nd product price :"))
weight2 = float(input("enter 2nd product weight :"))

if price1 <=0 or weight1 <=0 or price2 <=0 or weight2 <=0:
    print("negative or zero input not allowed")
else:
        product1_price_per_gram = price1 / weight1
        product2_price_per_gram = price2 / weight2

        if product1_price_per_gram < product2_price_per_gram:
            print("first product is cheaper ",product2_price_per_gram - product1_price_per_gram)
        else:
            print("second product is cheaper ",product1_price_per_gram - product2_price_per_gram)
