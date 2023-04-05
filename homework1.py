# DEĞİŞKENLER -START
baslik = "HABERİNİZ OLSUN"  # string
vade = 12  # int
faizOrani = 1.47  # float

print(baslik)
print(type(baslik))
print(type(vade))
print(type(faizOrani))

mesaj = "Hoşgeldin"
musteriAdi = "Selen Ece"
musteriSoyadi = "Özbay"
sonucMesaj = mesaj + " " + musteriAdi + " " + musteriSoyadi + "!"
print(sonucMesaj)
# print(mesaj, musteriAdi, musteriSoyadi)  => neden bu şekilde yazdırmadık?

sayi1 = 15
sayi2 = 50

print(sayi1 + sayi2)

print(sonucMesaj)
# DEĞİŞKENLER -END

# ŞART BLOĞU -START
dolarDun = 7.65
dolarBugun = 7.85
if dolarDun > dolarBugun:
    print("Azalış oku")
    print("Bitti")

elif dolarDun < dolarBugun:
    print("Artış oku")

else:
    print("Eşittir oku")

print("Bitti")

# if dolarDun < dolarBugun:
#     print("Artış oku")

# if dolarDun == dolarBugun:
#     print("Eşittir oku")
# ŞART BLOĞU -END

# ARRAY -START
krediler = ["Hızlı Kredi", "Maaş Kredisi", "Emekli İhtiyaç Kredisi"]

print(krediler)
print(krediler[0])
print(krediler[1])
print(krediler[2])

print(len(krediler))

krediler[0] = "Çabuk Kredi"
print(krediler)
# ARRAY -END

# DÖNGÜLER -START
for kredi in krediler:
    print(kredi)

# alias => döngü sırasında bulunduğu değer

for i in range(10):
    print(i)

for i in range(len(krediler)):
    print(krediler[i])

for i in range(3, 10):
    print(i)

for i in range(0, 10, 2):
    print(i)
# DÖNGÜLER -END

# FONKSİYONLAR -START
print("--İLK SAYFA")


def kredileriListele():

    krediler = ["Hızlı Kredi", "Maaş Kredisi", "Emekli İhtiyaç Kredisi"]

    for kredi in krediler:
        print(kredi)


kredileriListele()

print("--İKİNCİ SAYFA")
kredileriListele()
# FONKSİYONLAR -END
