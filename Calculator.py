import os
def add(a,b):
    return int(a+b)
def sub(a,b):
    return int(a-b)
def mul(a,b):
    return int(a*b)
def div(a,b):
    return int(a/b)
operations_dict = {"+": add, "-": sub, "*": mul, "/": div}
def calculator():
    n1 = float(input("Enter your first number:"))
    for i in operations_dict:
        print(i)
    flag = True
    while flag:
        op = input("Enter the operator: ")
        n2 = float(input("Enter your second number: "))
        calc = operations_dict[op]
        output = calc(n1, n2)
        print(f"{n1}{op}{n2}={output}")
        s = input(f"Enter 'yes' to continue the calculator or 'new' to newly update and 'no' to exit:").lower()
        if s == 'yes':
            n1 = output
        elif s == 'new':
            flag = False
            os.system('cls')
            calculator()
        else:
            print(f"Calculator ends.")
            flag = False
calculator()
