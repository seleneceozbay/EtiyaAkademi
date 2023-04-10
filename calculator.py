def sum(firstNumber: float, secondNumber: float):
    sum = firstNumber+secondNumber
    print(f"{firstNumber} + {secondNumber} = {sum}")


def substract(firstNumber: float, secondNumber: float):
    substract = firstNumber - secondNumber
    print(f"{firstNumber} - {secondNumber} = {substract}")


def multiplication(firstNumber: float, secondNumber: float):
    multiplication = firstNumber*secondNumber
    print(f"{firstNumber} * {secondNumber} = {multiplication}")


def divide(firstNumber: float, secondNumber: float):
    divide = firstNumber/secondNumber
    if secondNumber != 0:
        print(f"{firstNumber}/ {secondNumber} = {divide}")

    else:
        print("Please enter a valid number!")


def mod(firstNumber: float, secondNumber: float):
    mod = firstNumber % secondNumber
    print(f"{firstNumber} % {secondNumber} = {mod}")


def calculator(firstNum: float, secondNum: float, operation: str):
    if operation == "+":
        sum(firstNumber=firstNum, secondNumber=secondNum)

    elif operation == "-":
        substract(firstNumber=firstNum, secondNumber=secondNum)

    elif operation == "*":
        multiplication(firstNumber=firstNum, secondNumber=secondNum)

    elif operation == "/":
        divide(firstNumber=firstNum, secondNumber=secondNum)

    elif operation == "%":
        mod(firstNumber=firstNum, secondNumber=secondNum)

    else:
        print("Please enter a valid operator!")


while True:
    print("--------------------------------------\n")
    firstNumber = float(input("Please enter a number:   "))
    operator = input("Pick an operator :  +, -, *, /, %:   ")
    secondNumber = float(input("Please enter a number:   "))

    calculator(firstNumber, secondNumber, operator)
    isContinue = input("If you want to Quit press 'q' / Continue for 'Enter'")

    if isContinue == "q":
        print("\n Operation Ended.")
        break
    else:
        pass
