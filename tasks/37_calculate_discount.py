#Write a program to calculate discount amount using price and discount rate.

price = int(input("enter price :"))
rate = int(input("enter rate :"))

discount = price * rate /100
final = price - discount
print(final)