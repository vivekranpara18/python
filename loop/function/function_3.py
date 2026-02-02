#write a program to create function that calculate and 
# return simple interest of given amount rate and year

def simple_interest(p,r,n):
    return (p*r*n)/100   
p=int(input("enter price :"))
r=int(input("enter rate :"))
n=int(input("enter year :"))
si=simple_interest(p,r,n)

print(si)
