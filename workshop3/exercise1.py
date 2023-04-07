# Kullanıcıdan 10 adet sayı alalım ve bu sayılar arasından en büyük olanı kullanıcıya gösterelim.
numbers = []

for i in range(10):
    number = int(input("Bir sayı giriniz:    "))
    numbers.append(number)

print(numbers)
print(max(numbers))
