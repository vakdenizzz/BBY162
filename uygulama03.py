print("<<< ipucunuz öğrencilerin en sevdiği ders")
print("""
Adam Asmaca Oyununa Hoşgeldiniz
Toplam 5 Can Hakkınız Bulunmaktadır
Tahmin Girişlerinizi Küçük Harf Olarak Yapınız
""")
print("LÜTFEN BÜYÜK HARF KULLANINIZ")
kelime = "BOŞDERS"
bosluk = len(kelime) * "_"
list_cizgi = []
list_kelime = []
can = 5
for i in bosluk:
    list_cizgi.append(i)
for i in kelime:
    list_kelime.append(i)

# can bittiğinde oyununda bitmesi için while döngüsü
while (can != 0):
    flag = False
    print("can :", can)
   # döngü her başa döndüğünde oyuncuya kelime tablosunu göstermek için for döngüsü
    for i in list_cizgi:
        print(i, "\v")
    tahmin = input("\vbir harf giriniz : ")
    print()
    # kelime değişkeninde karakterleri index ve value olacak şekilde ayrılması
    for index, value in enumerate(kelime):
    # girilen harf doğru ise oyuncuya gösterilen tabloyu günceller
        if kelime[index] == tahmin:
            list_cizgi[index] = value
            flag = True
    # girilen harf yanlış ise, canı 1 azaltır
    if (flag == False):
        print("bilemediniz\v")
        can -= 1
    if (can == 0):
        print("oyun bitti KAYBETTİNİZ\v")
    # kelime tamamlanınca oyunu bitirmek için
    if (list_cizgi == list_kelime):
        print("BOŞDERS\v")
        print("TEBRİKLER kelimeyi buldunuz")
        break