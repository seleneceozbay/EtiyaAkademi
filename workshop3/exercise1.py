# Kullanıcıdan 10 adet sayı alalım ve bu sayılar arasından en büyük olanı kullanıcıya gösterelim.
sayilar = []

for i in range(10):
    sayi = int(input("Bir sayı giriniz:    "))
    sayilar.append(sayi)
print(sayilar)
print(max(sayilar))
