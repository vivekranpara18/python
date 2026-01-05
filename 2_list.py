mark=[50,60,70,80,85,90]
frutes=['apple','banana','apple','kiwi','mango','apple','banana','kiwi']

#insert value at 0th place
frutes.insert(0,'mango')
print(mark)
print(frutes)

#count value
print(frutes.count('apple'))

#index
print(frutes.index('mango'))

#appand
frutes.append('orange')
print(frutes)

#remove
frutes.remove('mango')
print(frutes)

#copy
frutes2 = frutes.copy()
print(frutes)
print(frutes2)

#clear
frutes2.clear()
print(frutes2)

#update
frutes[0] = 'orange'
print(frutes)
