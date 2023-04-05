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
dolarBugun = 7.35
if dolarDun > dolarBugun:
    print("Azalış oku")
    print("Bitti")

if dolarDun < dolarBugun:
    print("Artış oku")

if dolarDun == dolarBugun:
    print("Eşittir oku")

# ŞART BLOĞU -END
