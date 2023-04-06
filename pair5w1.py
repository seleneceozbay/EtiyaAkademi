
sayi1 = float(input("sayı1:   "))
sayi2 = float(input("sayı2:   "))

islem = input("Yapmak istedğiniz işlemi seçiniz (+ , - , * , /:  ")

if islem == "+":
    toplama = sayi1+sayi2
    print("Toplama=  ", {toplama})

elif islem == "-":
    fark = sayi1-sayi2
    print("Fark=    ", {fark})

elif islem == "*":
    carpma = sayi1*sayi2
    print("Çarpma=   ", {carpma})

elif islem == "/":
    bolme = sayi1/sayi2
    print("Bölme=   ", {bolme})

else:
    print("Uygun bir işlem seçmediniz.")


print("-----------------------------------")


vize = float(input("Vize notunu giriniz: "))
final = float(input("Final notunu giriniz:   "))

ortalama = (vize*0.4) + (final*0.6)

if ortalama <= 49:
    print("notunuz FF")

elif 50 <= ortalama <= 59:
    print("notunuz DD")

elif 60 <= ortalama <= 69:
    print("notunuz CC")

elif 70 <= ortalama <= 79:
    print("notunuz BB")

else:
    print("notunuz AA")
