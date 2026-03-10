def string_to_number(number):
    try:
        return int(number)
    except(ValueError):
        return("input is not valid")

n1=input("enter string :")
print(string_to_number(n1))

