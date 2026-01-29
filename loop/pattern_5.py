'''
5 4 3 2 1
5 4 3 2 
5 4 3 
5 4 
5  
'''
for row in range(0,6,+1):
    for no in range(5,row,-1):
        print(no,end=' ')
    print("")