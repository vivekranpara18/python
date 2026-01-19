#write a program to accept length and width of two different farm from user. and 
# find out & display which farm is bigger 

length1 = float(input("enter 1st farm length :"))
weight1 = float(input("enter 1st farm weight :"))

length2 = float(input("enter 2nd farm length :"))
weight2 = float(input("enter 2nd farm weight :"))

farm1 = length1 * weight1
farm2 = length2 * weight2

if farm1 < farm2:
    print("1st farm is smaller")
else:
    print("2nd farm is bigger")
