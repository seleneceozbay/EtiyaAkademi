# Perfect Numbers

def perfectNumber():
    checkNumber = int(input("Enter a number:  "))

    sum = 0
    for i in range(1, checkNumber):
        if (checkNumber % i == 0):
            sum += i

    if sum == checkNumber:
        print(f"{checkNumber} is a Perfect Number")

    else:
        print(f"{checkNumber} is not a Perfect Number")


perfectNumber()
