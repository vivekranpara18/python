"""
* * * *
*     *
*     *
* * * *
"""
n = 4
for row in range(n):
    for no in range(n):
        if row==0 or no==0 or row==n-1 or no==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()