# Kullanıcıdan 10 adet sayı alalım ve bu sayılar arasından en büyük olanı kullanıcıya gösterelim.

def numbers():
    numberList = []
    for i in range(10):
        number = int(input("Bir sayı giriniz:    "))
        numberList.append(number)

    print("Girdiğiniz en büyük sayı:   ", max(numberList))


numbers()
