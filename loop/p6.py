#print series 1    -8   27  -64  .....    1000

no = 1
while no<10:
    cube = no*no*no
    if no % 2 == 0:
        cube = 0 - cube
        
    print(cube,end=' ')
    no = no + 1