# write a lambda function to calculate and return simple interest of given amount rate year 

'''def simple_interest(amount,rate,year):
    interest = (amount * rate * year ) / 100
    return interest
'''

simple_interest = lambda amount, rate, year : (amount * rate * year) / 100

amount = float(input("enter amount :"))
rate = float(input("enter rate :"))
year = float(input("enter year :"))

interest = simple_interest (amount,rate,year)
print(interest)