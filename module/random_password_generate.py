#generate random password  (letters in mixed case,digits,symbols)
import random as r
import string as s

seeds=s.ascii_lowercase + s.ascii_uppercase+s.digits+s.punctuation

seeds=list(seeds)
r.shuffle(seeds)

size=len(seeds)
#print(seeds)
count=1
letter=[]
num=int(input("how many letter you want password:"))
while count<=num:

    letter.append(seeds[r.randint(0,size)])
    count=count+1
#conver list into string
password=''.join(letter)
print(password)