# Fibonacci

def fibonacci():
    numberOfTerms = int(input("How many numbers do you write?   "))
    firstNumber = 1
    secondNumber = 1

    fibonacciList = []
    if numberOfTerms < 0:
        print("Please write valid number, greater & equal to 0.")

    elif numberOfTerms == 0:
        fibonacciList.append(0)

    else:
        fibonacciList.append(firstNumber)
        fibonacciList.append(secondNumber)
        for i in range(2, numberOfTerms):
            thirdNumber = firstNumber+secondNumber
            fibonacciList.append(thirdNumber)
            firstNumber = secondNumber
            secondNumber = thirdNumber

    print(fibonacciList)


fibonacci()
