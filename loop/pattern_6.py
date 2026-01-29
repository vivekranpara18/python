'''
1 
1 0 
1 0 1
1 0 1 0
1 0 1 0 1
'''

for row in range(1,6):
    for no in range(1,row+1):
        if no % 2 == 0:
            print(0,end=' ')
        else:
            print(1,end=' ')
    print("")