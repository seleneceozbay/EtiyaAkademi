# Kullanıcıdan 10 adet sayı alalım ve bu sayılar arasından en büyük olanı kullanıcıya gösterelim.
sayilar = []

for i in range(10):
    sayi = int(input("Bir sayı giriniz:    "))
    sayilar.append(sayi)
print(sayilar)
print(max(sayilar))


# Kullanıcının vereceği üst limit ile 0'dan bu üst limite kadar olan tüm 'çift' sayıları ekrana yazdıralım.
numbers = []
for x in range(0, max(sayilar), 2):
    numbers.append(x)

print(numbers)


ustLimit = max(sayilar)
altLimit = int(input("Lütfen Alt limit giriniz:  "))

liste = []

for i in range(altLimit, ustLimit):
    if i % 2 == 0:
        print(i, end=" ")

print(liste)
