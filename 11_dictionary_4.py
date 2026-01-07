person = {'name':'vivek ranpara','age':20,'weight':61.22,'gender':True,'isMarried':False}
print(person)

#using get function
print(person.get('name'))
print(person.get('age'))

print(person.get('city'))

person2 = person.copy()
#print(person,person2)
person2.clear()
print(person,person2)

print(person.keys())
print(person.values())
print(person.items())

book = ['name','author','pages','price','isbnno']
python_book = dict.fromkeys(book)
print(python_book)
python_book['name'] = "Mastering Python" #update
python_book['author'] = "vivek" #update
python_book['publisher'] = "ABC" #create

print(python_book)

python_book.pop('price')
python_book.pop('country',False)
python_book.popitem()
print(python_book)
print("good bye")