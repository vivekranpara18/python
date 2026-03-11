"""The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.

Examples(Operator, value1, value2) --> output
('+', 4, 7) --> 11
('-', 15, 18) --> -3
"""

def basic_op(operator, value1, value2):
    #your code here
    if op=='+':
        add = n1 + n2
        return add
    elif op=='-':
        sub = n1 - n2
        return sub
    elif op=='*':
        mul = n1 * n2
        return mul
    elif op=='/':
        div = n1 / n2
        return div

op = str(input("enter operstor :"))
n1 = int(input("enter first number :"))
n2 = int(input("enter second number :"))
print(basic_op(op,n1,n2))