#write a program to findout day of week(monday/tuesday/wednesday) from given date.  

day=int(input("enter day 1 to 31:"))#25
month=int(input("enter month 1 to 12:"))#1
year=int(input("enter year:"))#26

week=['','sunday','monday','tuesday','Wednesday','Thursday','Friday','Saturday']
m=['',0,3,3,6,1,4,6,2,5,0,3,5]
y=year%100

ans=(day+y+(y//4)+m[month])%7

print(week[ans])
