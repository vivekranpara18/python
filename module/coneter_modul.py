import conerter as c

#here c is alias for converter, instead of writing converter, we can use c 
#take input meter, foot, cm 
meter = float(input("Enter value in meters: "))
foot = float(input("Enter value in feet: "))
cm = float(input("Enter value in centimeters: "))


inch=c.metertoinch(meter)
print("meter to inch:",inch)

inch=c.foottoinch(foot)
print("foot to inch:",inch)


inch=c.cmtoinch(cm)
print("cm to inch:",inch)