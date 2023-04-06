vize = int(input("Vize notunuzu giriniz: "))
final = int(input("Final notunuzu giriniz: "))
ortalama = (vize * 0.4) + (final * 0.6)

# eğer final 40'dan küçükse kullanıcı kaldı
# eğer ortalama 50'den küçükse kullanıcı kaldı
# eğer vize finalin 2 katı ise kullanıcı kaldı
# bunun dışındaki tüm durumlarda kullanıcı geçti yazdırmak istiyoruz.

if final < 40:
    print("Kaldınız, final notunuz yetersiz")
elif ortalama < 50:
    print("Kaldınız, ortalamanın altındasınız")
elif vize == (final*2):
    print("Kaldınız, Vize notunuz final notunuzun 2 katı")
else:
    print("Geçtiniz!")
