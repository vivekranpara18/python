person = {'name':'rahul sharma','age':40,'weight':74.22,'gender':True,'isMarried':False}
print(person)

print(person['name']) # rahul sharma

#update 
person['name'] = 'rohit sharma'
print(person)

#we can add new key value pair 
person['city'] = 'gujarat'
print(person)

#delete
del person['isMarried']
print(person)