number = input("enter value :")
number = int(number)

temp = number

first = number // 100
temp = temp // 10
middle = temp % 10
last = number % 10

firstno = ['hundred','one hundred','two hundred','three hundred','four hundred','five hundred','six hundred','seven hundred','eight hundred','nine hundred']
secondno = ['','','twenty','thirty','fouty','fifthy','sixty','seventy','eighty','ninety']

thirdno = ['zero','one','two','three','four','five','six','seven','eight','nine']

print(firstno[first],'',secondno[middle],'',thirdno[last])