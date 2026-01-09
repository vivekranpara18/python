"""#write a program to display dinominations of currency for given amount
input : 887 Rupees 
output : 
500 x 1 = 500
200 x 1 = 200
100 x 1 = 100
50 x 1 =  50
20 x 1 =  20
10 x 1 =  10
5 x 1 =   05
2 x 1 =   02
1 x 1 =   01"""

amount = int(input("enter amount :"))

c500 = amount // 500
amount = amount % 500

c200 = amount // 200
amount = amount % 200

c100 = amount // 100
amount = amount % 100

c50 = amount // 50
amount = amount % 50

c20 = amount // 20
amount = amount % 20

c10 = amount // 10
amount = amount % 10

c5 = amount // 5
amount = amount % 5

c2 = amount // 2
amount = amount % 2

c1 = amount // 1
amount = amount % 1

ans=(f"""
500 x 1 = {c500}
200 x 1 = {c200}
100 x 1 = {c100}
50 x 1 =  {c50}
20 x 1 =  {c20}
10 x 1 =  {c10}
5 x 1 =   {c5}
2 x 1 =   {c2}
1 x 1 =   {c1}
""")

print(ans)