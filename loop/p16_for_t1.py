# write a program to count odd and even number in numeric list
list = [1,2,3,4,5,6,7,8,9,10]
odd = 0
even = 0
for num in list:
    if num % 2 == 0:
        even+=1
    else:
        odd+=1
print("odd number :",odd)
print("even number :",even)