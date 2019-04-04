print("Merhaba arkadaşlar hoşgeldiniz 4 şıktan oluşan genel kültür testimize hoşgeldiniz...")
print("LÜTFEN CEVAPLARI BÜYÜK HARFLER İLE BELİRTİNİZ")
sorular = [ 'Dinazorların nesli kaçıncı yüzyılda tükenmiştir?',\
            'ABD başkanının besledikleri hayvanlar arasında aşağıdakilerden hangisi yoktur ?',\
            'Bir futbol maçı sonucu kaç farklı sonuçta bitebilir?',\
            'Santrançta tek şah kaldıktan sonra kaç hamle sonra oyun pat olur?',\
            'Aşağıdaki unvanlardan tarih boyunca varolmayan hangisidir?']
#Yukarıdaki  satırda soruların atadım
cevaplar = ['D', 'B', 'C', 'C', 'D']
# Yukardaki soruların cevaplarını cevaplar adı altında atadım
cevapA = [' 16.',\
          ' Muhabbet kuşu.',\
          ' 1.',\
          ' 32.',\
          ' Avusturya Prensi.']
cevapB = [' 17.',\
          ' Zürefa',\
          ' 2.',\
          ' 45 .',\
          ' Avusturya Arşidükü']
cevapC = [' 18.',\
          ' Sırtlan.',\
          ' 3.',\
          ' 52.',\
          ' Avusturya İmparatoru.']
cevapD = [' 19.',\
          ' Su aygırı',\
          ' 4.',\
          ' 55.',\
          ' Avusturya Kralı.']
#yukarıda girdiğim sorulara cevaplar atadım
Test_puanınız= 0
# Yukarıda test için puan başlangıcı belirledim her dogru yanıtta artacak
for i in range(len(sorular)):
    print("sorular"+str(i+1)+":"+sorular[i])
    print(("A") + cevapA[i])
    print(("B") + cevapB[i])
    print(("C") + cevapC[i])
    print(("D") + cevapD[i])
    #for döngüsünü devreye sokarak her sorudan sonra diğer soruya geçiş sagladım ve cevapları ve soruları eşleştirdim.
    cevap = input("Cevap: ")
    if(cevaplar[i] == cevap.upper()):
        #cevapları eşlendirerek doğrulugunu belirledim
        Test_puanınız +=1
print("Test sonucunuz:{}".format(Test_puanınız*20))