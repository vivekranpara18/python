set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
print(set1,set2)

#get unique value
set3 = set1.union(set2)
print(set3)

#get common value
set4 = set1.intersection(set2)
print(set4)

#get all values that is in one(set1) set but not in other set (set2)
set5 = set1.difference(set2)
print(set5)

numbers = [11,15,17,24,29,33,11,17,39,41,33]
print(numbers)

print(len(numbers))

#remove dublicate number
unique_numbers = (set(numbers))
print(unique_numbers)
