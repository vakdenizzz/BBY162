print("*Aşagıdaki soruları cevaplayınız ? * ")
print("Dogru cevaplar için -Tebrikler, sonucunuz doğru-, yanlış cevap için -Üzgünüz, doğru cevap değil- yazınız. ")
print("-----------Pratik cevap verme seviyesini ölçmek için soruları cevaplayınız...-----------")
#yukarıda içerik hakkında bilgi vererek girdiler oluşturdum.
sorular = [ '30 sayısını yarıma bölüp 10 eklediniz sonuç kaç olur ? [25/70]',\
            '3 elma vardı, ikisini aldım. Kaç elmam var ? [2/5]',\
            ' Bir futbol maçında en fazla kaç dakika uzatma verilir ? [45/44]',\
            ' 1 saat kaç saliseden oluşur ? [36000\360000]',\
            'Bir uçak kaç adet tekerlege sahiptir? [3/5]']
#sorular kısmına soruları girdim ve devamında  cevaplar  kısmına soruların cevaplarını atadım.
cevaplar = ['70', '2', '44', '360000', '3']
puan = 0
#puan kısmı oluşturarak dogru cevaplarda +=1 seklindde artış sagladım.

#soru 1
cevap = input((sorular[0])) # cevap satırana input girdisi sağladım ve bu sayede programa giriş oluşturdum.
if cevaplar[0] == cevap.upper():
    print("Tebrikler, sonucunuz doğru!")
    puan += 1               # Bu satırda her dogru yanıt üstüne bir koyarak artması için kod girdim.
else:                       # Bu satırla birlikte eğer cevao dogru değilse  komutun devreye girmesini sağladım.
    print("Üzgünüz doğru cevap değil!")
#soru 2
cevap = input((sorular[1]))
if cevaplar[1] == cevap.upper():
    print("Tebrikler, sonucunuz doğru!")
    puan += 1
else:
    print("Üzgünüz doğru cevap değil!")
#soru 3
cevap = input((sorular[2]))
if cevaplar[2] == cevap.upper():
    print("Tebrikler, sonucunuz doğru!")
    puan += 1
else:
    print("Üzgünüz doğru cevap değil!")
#soru 4
cevap = input((sorular[3]))
if cevaplar[3] == cevap.upper():
    print("Tebrikler, sonucunuz doğru!")
    puan += 1
else:
    print("Üzgünüz doğru cevap değil!")
#soru 5
cevap = input((sorular[4]))
if cevaplar[4] == cevap.upper():
    print("Tebrikler, sonucunuz doğru!")
    puan += 1
else:
    print("Üzgünüz doğru cevap değil!")
#test sonu
print("pratik cevap düzeyiniz: " +str(puan*20))
# puanlar her dogru  cevapta +1 seklinde  artış sagladı son olarak en son kaç adet dogru varsa 20 ile çarpıp yüz üzerinden bir puan oluşturdum.
