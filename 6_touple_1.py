nations = ("India", "United States", "China", "Russia", "Germany", "France", "Japan", "Brazil", "United Kingdom", "Australia","India","Sri lanka","India")
print(nations)

#display 0th position
print(nations[0])

#display 1st and 2nd and 3rd nations
print(nations[1:4])

#display all the items from 5th position onwards
print(nations[5:])

#findout what is the position of russia in tuple
print(nations.index("Russia"))

print("Count of india ",nations.count("India"))
print("Count of Finland ",nations.count("Finland"))
# print("Position of Norway ",nations.index("Norway"))
print(nations*2)
print("good bye")
