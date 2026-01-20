'''Write a program that takes a 5 subject marks from user. 
calculate total and Percentage  and prints the grade using the following conditions:

| Percentage | Grade |
| ---------- | ----- |
| 90–100     | A+    |
| 80–89      | A     |
| 70–79      | B     |
| 60–69      | C     |
| 50–59      | D     |
| below 50   | Need to improve  |
'''

s1 = int(input("enter first subject mark :"))
s2 = int(input("enter second subject mark :"))
s3 = int(input("enter third subject mark :"))
s4 = int(input("enter fourth subject mark :"))
s5 = int(input("enter fifth subject mark :"))

total = s1+s2+s3+s4+s5
per = total / 5

if per >= 90 and per <=100:
    print("grade A+")
elif per >= 80 and per <=89:
    print("grade A")
elif per >= 70 and per <=79:
    print("grade B")
elif per >= 60 and per <=69:
    print("grade C")
elif per >= 50 and per <=59:
    print("grade D")
else:
    print("need to improve")

