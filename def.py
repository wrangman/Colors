import os
from msvcrt import getwch



def calculate(x, y, operator):  # Function that can calculate with any operator
    if operator == 1:       # Plus
        return x+y
    elif operator == 2:     # Minus
        return x-y
    elif operator == 3:     # Multiply
        return x*y
    elif operator == 4:     # Division
        return x/y


os.system('cls')

while True:
    
    x = int(input("x: "))
    y = int(input("y: "))

    print("Vilket räknesätt? (1=plus, 2=minus, 3=gånger, 4=delat) ", end="")
    while True:
        try:
            op = int(getwch())
            break
        except:
            continue
    
    print("\n")
    print("Result: ", calculate(x, y, op))
    print("\n")
    