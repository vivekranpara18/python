'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 
'''
no = 1
for row in range(1,6):
    for astric in range(1,row+1):
        print(no,end=' ')
        no+=1
    print('')