# write a program to print given amount into words
# input : 12345 output : one two three four five 
words = ['zero','one','two','three','four','five','six','seven','eight','nine']

number = int(input("enter amount :"))
list = []
while number>0:
    reminder = number % 10 
    list.insert(0,words[reminder])
    number = number // 10 

print(' '.join(list))