def get_merit(computer,drawing,english,history,maths,science):
    total = maths + science + english
    return total

c = int(input("enter marks for computer :"))
d = int(input("enter marks for drawing :"))
e = int(input("enter marks for english :"))
h = int(input("enter marks for history :"))
m = int(input("enter marks for maths :"))
s = int(input("enter marks for science :"))


total = get_merit(computer=c,drawing=d,english=e,history=h,maths=m,science=s)
print(total)