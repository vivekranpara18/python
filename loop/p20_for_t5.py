#write a program to count vowels, consonants, digits, words, and symbol in given list
string = input("enter list :")
vowels_list = ['a','e','i','o','u']
consonants_list = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm','n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
digits_list = ['0','1','2','3','4','5','6','7','8','9']
vowels = 0
consonants = 0
digits = 0
symbol = 0

for char in string:
    if char in digits_list:
        digits+=1
    elif char in vowels_list:
        vowels+=1
    elif char in consonants_list:
        consonants+=1
    else:
        symbol+=1

print("total words are ",len(string.split()))
print("vowels are ",vowels)
print("consonants are ",consonants)
print("digit are ",digits)
print("symbole are ",symbol)