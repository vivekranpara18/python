#create function and return square and cube

def get_square(number):
    square = number * number
    return square

def get_cube(num):
    cube = get_square(num) * num
    return cube

n1 = int(input("enter number :"))
result = get_square(n1)
print("square = ",result)
result2 = get_cube(n1)
print("cube = ",result2)