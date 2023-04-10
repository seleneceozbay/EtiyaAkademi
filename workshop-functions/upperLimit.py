# Kullanıcının vereceği üst limit ile 0'dan bu üst limite kadar olan tüm 'çift' sayıları ekrana yazdıralım.

def uLimit():
    upperLimit = int(input("Üst limit giriniz:   "))
    for x in range(0, upperLimit):
        if x % 2 == 0:
            print(x, end="  ")


uLimit()
