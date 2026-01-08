#write a program to convert given 2 digit amount into words
amount=input('enter value :')
amount = int(amount)

last = amount % 10

first = amount // 10

words = ['zero','one','two','three','four','five','six','seven','eight','nine']

print(words[first],'',words[last])