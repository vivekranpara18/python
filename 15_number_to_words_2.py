number=input('enter value :')
number = int(number)
temp = number

first = number // 100   
temp = temp // 10
middle = temp % 10
last = number % 10
words = ['zero','one','two','three','four','five','six','seven','eight','nine']
print(first,'   ',middle,'   ',last)
print(words[first],'',words[middle],'',words[last])