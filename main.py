import art
import os

def addition(numberOne, numberTwo):
    return numberOne + numberTwo


def subtraction(numberOne, numberTwo):
    return numberOne - numberTwo


def multiplication(numberOne, numberTwo):
    return numberOne * numberTwo


def division(numberOne, numberTwo):
    return numberOne / numberTwo


operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}


def calculator():
    print(art.logo)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    toContinue = True

    while toContinue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            toContinue = False
            os.system('clear')
            calculator()


calculator()