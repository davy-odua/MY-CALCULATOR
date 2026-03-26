#CALCULATOR PROGRAM
#Requirements
#1). (-----MY CALCULATOR-----)
#2). Basic operators: ('+','-','*','/','^','%')
#3). Advanced operators: (log, sqrt)

import math

print("-----MY CALCULATOR-----")
print("Basic Operators: '+','-','*','/','^','%' ")
print("Advanced Operators: (log, sqrt) ")

calculating = True
while calculating:
    # Binary operator
    operat_or = input("Enter the operator: ").lower()
    if operat_or in ['+', '-', '*', '/', '^', '%']:
        try:
            first_numb = float(input("Enter the first number: "))
            second_numb = float(input("Enter the second number: "))
        except ValueError:
            print("Please enter a number")
            continue

        if operat_or == '+':
            print(f"The answer is {first_numb + second_numb}")
        elif operat_or == '-':
            print(f"The answer is {first_numb - second_numb}")
        elif operat_or == '*':
            print(f"The answer is {first_numb * second_numb}")
        elif operat_or == '/':
            if second_numb == 0:
                print(f"Zero cannot be divided")
            else:
                print(f"The answer is {first_numb / second_numb}")
        elif operat_or == '^':
            print(f"The answer is {first_numb ** second_numb}")
        elif operat_or == '%':
            print(f"The answer is {first_numb % second_numb}")

    # Unary operator
    elif operat_or in ['sqrt', 'log']:
        try:
            numb = float(input("Enter the number: "))
        except ValueError:
            print("Enter a number")
            continue

        if operat_or == 'sqrt':
            if numb >= 0:
                print(f"The answer is {math.sqrt(numb)}")
            else:
                print("Cannot calculate the square root of a negative number")
        elif operat_or == 'log':
            if numb > 0:
                print(f"The answer is {math.log10(numb)}")
            else:
                print("Cannot calculate the log of a zero or negative number")

    # Invalid operator
    else:
        print("Invalid operator")

    continu_e = input("Continue (y/n): ").lower()
    if continu_e == "n":
        break

