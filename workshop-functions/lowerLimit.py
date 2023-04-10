# 2. geliştirdiğimiz programa kullanıcının alt limiti belirlemesi için gerekli desteği ekleyelim.

def lowerLimit():
    lowerLimit = int(input("Alt limit giriniz:   "))
    upperLimit = int(input("Üst limit giriniz:   "))
    for y in range(lowerLimit, upperLimit):
        if y % 2 == 0:
            print(y, end="   ")


lowerLimit()
