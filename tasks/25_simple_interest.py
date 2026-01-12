#Write a program to calculate simple interest using principal, rate, and time.
principle = int(input("enter principle :"))
rate = int(input("enter rate :"))
time = int(input("enter time :"))

si = principle * rate * time / 100

print(si)