#Write a program to calculate total amount after simple interest.
principle = int(input("enter principle :"))
rate = int(input("enter rate :"))
time = int(input("enter time :"))

si = principle * rate * time / 100

print(si)
tot = si + principle
print(tot)