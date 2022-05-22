import sqlite3
# encoding: utf-8 
print("            * Test Sistemine Hosgeldiniz *              ")
vt=sqlite3.connect("vt.sqlite")
ekTest=[]
im=vt.cursor()
im.execute("""CREATE TABLE IF NOT EXISTS giris(nickname, password)""")
kayit=0
while kayit==0:
    kayitkontrol=input("Kayıtlı mısınız?")
    if kayitkontrol=="E" or kayitkontrol=="e":
        adkontrol=input("Kullanıcı adınızı giriniz:")
        sifrekontrol=input("Şifrenizi giriniz:")
        kayit=1
    elif kayitkontrol=="h" or kayitkontrol=="H":
        ad=input("Kullanici adi belirleyiniz:")
        sifre=input("Şifre belirleyiniz:")
        im.execute("""INSERT INTO giris VALUES(?,?)""",(ad,sifre))
        vt.commit()
        kayit=0

while True:
    kirma=0
    def anamenü(a):
        kontrol=int(input("Ana menüye dönmek icin 1'i sistemden cikmak icin 2'yi tuslayiniz: "))
        try:
            if kontrol==1:
                a=1
                return a
            else:
                print("sistemden çıkış yapılıyor...")
                a=2
                return a
        except:
            print("hatalı giriş")
            
    plaj=0 
    orman=0
    dag=0
    sehir=0
    
    italyan=0
    fransiz=0
    japon=0
    ispanyol=0
    alman=0
    turk=0
    amerika=0
    
    paranoid=0
    antisosyal=0
    histriyonik=0
    narsisistik=0
    bagımlı=0
    obsesif=0

    cevaplar=[]
    print("Testinizin sonunda puanlarınız gözükecek.")        
    test2={}
    test3={}
    testSecim=int(input("""
Hangi testi yapmak istersiniz?
    
1- Hangi tatil insanisin? 
2- Hangi dunya mutfagi insanisin? 
3- Hangi kisilik bozukluguna yatkinsin? 
==>  """))
    if (testSecim==1):
                soru1=input("1-)Tatilde tuvalet, banyo konforuna onem verir misiniz?(e/h): ")
                if soru1=='e':
                    sehir+=1
                soru2=input("2-)Dogadaki hayvanlarin sana yakin olmasi seni rahatsiz eder mi?(e/h): ")
                if soru2=='e':
                    plaj+=1
                    sehir+=1
                else:
                    orman+=1
                    dag+=1
                soru3=input("3-)Boceklerden korkar misiniz?(e/h): ")
                if soru3=='e':
                    sehir+=1
                else:
                    orman+=1
                    dag+=1
                    plaj+=1
                soru4=input("4-)Ne bulursam yerim der misiniz?(e/h): ")
                if soru4=='e':
                    orman+=1
                    dag+=1
                else:
                    plaj+=1
                    sehir+=1
                soru5=input("5-)Basari yolunda kendini zorlar misin?(e/h): ")
                if soru5=='e':
                    dag+=1
                soru6=input("6-)Gece olunca yapay isiklardan uzaklasmak istiyor musunuz?(e/h): ")
                if soru6=='e':
                    plaj+=1
                    orman+=1
                    dag+=1
                else:
                    sehir+=1
                soru7=input("7-)Sahilde vakit gecirmeyi sever misiniz?(e/h): ")
                if soru7=='e':
                    plaj+=1
                soru8=input("8-)Ormanin icinde olmak sana huzur verir mi?(e/h): ")
                if soru8=='e':
                    orman+=1
                soru9=input("9-)Gece olunca eglence mekanina gitmek ister misiniz?(e/h): ")
                if soru9=='e':
                    sehir+=1
                    plaj+=1
                    test1={}
                sonuc=[plaj,orman,dag,sehir]
                isim=("plaj","orman","dag","sehir")
                for i in range(0,int(len(isim))):
                    test1.setdefault(isim[i],sonuc[i])
                print("Puanlariniz:\n",test1)
                class soru:
                    def sorgu(self):
                        sorgu=(input("Daha çok test görmek ister misiniz?(e/h):\n"))
                        if sorgu=="E" or sorgu=="e":
                            oneri=input("Ne tarz bir test görmek istersiniz?:")
                            ekTest.append(oneri)  
                        elif sorgu=="h" or sorgu=="h":
                            print("Teşekkürler")
                kirma=anamenü(0)
                if kirma==1:
                    continue
                elif kirma==2:
                    break
    if (testSecim==2):
            soru1_1=int(input("""
Yemegi yapan mi onemli yemegin kendisi mi?
1- Yemegi yapan
2- Yemegin kendisi
==>  """))
            if (soru1_1==1):
                turk+=1
                fransiz+=1
                italyan+=1
            elif (soru1_1==2):
                japon+=1
                ispanyol+=1
                alman+=1
                amerika+=1
            else:
                print("Gecerli bir tuslama yapiniz.")
            soru2_1=input("Yemek konusunda hijyene dikkat eder misiniz?(e/h):")
            if (soru2_1=='e'):
                fransiz+=1
                italyan+=1
                ispanyol+=1
            else:
                alman+=1
                turk+=1
                japon+=1
                amerika+=1
            soru3_1=input("Yemegin tadına bakmadan baharat atar misiniz?(e/h):")
            if (soru3_1=='e'):
                alman+=1
                turk+=1
                amerika+=1
            soru4_1=input("Yemek secimine göre bir insana dair olan dusunceleriniz degisir mi?(e/h):")
            #Her sorunun bir islevi olmasa da olur sanirim
            soru5_1=int(input("""
Yemek yerken hangi tur muzik dinlemek istersiniz?
1- Jazz, blues.
2- Musiki.
3- Hard rock, heavy metal.
4- Hip hop.
5- Pop.
6- Sessizligi tercih ederim.
==>  """))
            if(soru5_1==1 or 3 or 4):
                amerika+=1
            elif(soru5_1==2):
                turk+=1
            elif(soru5_1==5):
                alman+=1
                japon+=1
            elif(soru5_1==6):
                print("Iyi yapiyorsun canim:)")
            else:
                print("Gecerli bir tuslama yapiniz.")
            soru6_1=input("Peynir ve soslari yemeklerde sever misiniz?(e/h):")
            if(soru6_1=='e'):
                italyan+=1
            soru7_1=input("Deniz urunlerini ve bunlarin hos servis edilmesini sever misiniz?(e/h):")
            if(soru7_1=='e'):
                fransiz+=1
            soru8_1=int(input("""
Pirinc, noodle, susi ve tofular desek?
1- Hayir derim.
2- Bayilirim!
3- Iclerinden yalnizca bazilarını tuketiyorum.
==>  """))
            if(soru8_1==2):
                japon+=1
            else:
                print("Gecerli bir tuslama yapiniz.")
            soru9_1=int(input("""
Mezelerle araniz nasildir?
1- Oley oley oley bayilirim!
2- Pek sevmem.
3- Aram yok.
==>  """))
            if(soru9_1==1):
                ispanyol+=1
            else:
                print("Gecerli bir tuslama yapiniz.")
            soru10_1=int(input("""
Islenmis et hakkindaki düsüncelerinizi alalim:
1- Et olsun da gerisi onemli degil!
2- Et tuketmiyorum.
3- Cok aram yok bazen yerim.
==>  """))
            if(soru10_1==1):
                alman+=1
                turk+=1
            else:
                 print("Gecerli bir tuslama yapiniz.")
            soru11_1=int(input("""
Zeytinyaglilar, hamur isleri ve etli yemekler desek ne derdiniz?
1- Hepsine bayilirim!
2- Hicbrini tuketmeyi sevmiyorum.
3- Et varsa ben yokum.
4- Bazılarini yiyorum sanirim.
==>  """))
            if(soru11_1==1):
                turk+=1
            else:
                print("Gecerli bir tuslama yapiniz.")
            sonuc=[italyan,fransiz,japon,ispanyol,alman,turk,amerika]
            isim=("italyan","fransiz","japon","ispanyol","alman","turk","amerika")
            for i in range(0,int(len(isim))):
                test2.setdefault(isim[i],sonuc[i])
            print("Puanlariniz:\n",test2)
            kirma=anamenü(0)
            if kirma==1:
                continue
            elif kirma==2:
                break
    if (testSecim==3):
            soru1_2=int(input("""
Bu sorunların kac tanesinin sizde oldugunu dusunuyorsunuz?:
-Güvensizlik ve başkalarına karşı şüphe duyma
-Kin tutma eğilimi
-Eş veya sevgilinin sadakatsiz olduğuna dair şüphe
-Başkaları tarafından kullanılacaklarını düşünme nedeniyle güvensizlik
1)Hicbiri
2)Birkacina evet dedim
3)Hepsi
==>  """))
            if (soru1_2==2 or 3):
                paranoid+=1
            soru2_2=int(input("""
Bu sorunların kac tanesinin sizde oldugunu dusunuyorsunuz?:
-Tutarsızca sorumsuz davranışlarda bulunma
-Yaptıklarından pişman olmama 
-Başkalarının haklarının ihlal etme
-Takma ad kullanmak
-Yalan söylemek
1)Hicbiri
2)Birkacina evet dedim
3)Hepsi
==>  """))
            if (soru2_2==2 or 3):
                antisosyal+=1
            soru3_2=int(input("""
Bu sorunların kac tanesinin sizde oldugunu dusunuyorsunuz?:
-Sürekli dikkat çekmek  
-Aşırı duygusal, dramatik bir ruh halinde olma
-Başkaları tarafından kolayca etkilenme
-Hızla değişen duygular
-Fiziksel görünümden dolayı aşırı endişe duyma
1)Hicbiri
2)Birkacina evet dedim
3)Hepsi
==>  """))
            if (soru3_2==2 or 3):
                histriyonik+=1
            soru4_2=int(input("""
Bu sorunların kac tanesinin sizde oldugunu dusunuyorsunuz?:
-Güç, başarı ve çekiciliğin fantezileri
-Başarıları veya yetenekleri abartma
-Sürekli övgü ve hayranlık beklentisi            
-İnsanların yaptığı iyiliklerden faydalanma ve yalan söyleme
-Başkalarını kıskanma ya da başkalar tarafından kıskanıldığını düşünme    
1)Hicbiri
2)Birkacina evet dedim
3)Hepsi
==>  """))
            if (soru4_2==2 or 3):
                narsisistik+=1
            soru5_2=int(input("""
Bu sorunların kac tanesinin sizde oldugunu dusunuyorsunuz?:
-Özgüven eksikliği
-Projeler başlatmak veya yapmakta zorluk çekmek
-Yakın bir ilişki bittiğinde hemen akabinde yeni bir ilişkiye başlamak 
-Başkalarına aşırı bağımlılık    
1)Hicbiri
2)Birkacina evet dedim
3)Hepsi
==>   """))
            if (soru5_2==2 or 3):
                bagımlı+=1
            soru6_2=int(input("""
Bu sorunların kac tanesinin sizde oldugunu dusunuyorsunuz?:
-Detaylar, düzen ve kurallarla meşgul olma
-Bir projeyi bitirememe duygusu 
-Aşırı mükemmeliyetçilik
-İnsanların, görevlerin ve durumların kontrolünü elde tutma 
1)Hicbiri
2)Birkacina evet dedim
3)Hepsi
==>   """))
            if (soru6_2==2 or 3):
                obsesif+=1
            soru7_2=int(input("""
Bu sorunların kac tanesinin sizde oldugunu dusunuyorsunuz?:
-Kırık veya değersiz nesneleri atamama (eşya biriktirme)
-Sert ve inatçı bir ruh hali
-Para harcama üzerinde yanlış kontrol
-Ahlak, etik veya değerler konusunda esnek davranış sergileyememe
1)Hicbiri
2)Birkacina evet dedim
3)Hepsi
==>   """))
            if (soru7_2==2 or 3):
                obsesif+=1
            soru8_2=int(input("""
Yalnız kaldığında kendi bakımını sağlayamadğınızı düşünüyor musunuz?:
1)evet
2)hayır
==>  """))
            if (soru8_2==1):
                bagımlı+=1
            sonuc=[paranoid,antisosyal,histriyonik,narsisistik,bagımlı,obsesif]
            isim=("paranoid","antisosyal","histriyonik","narsisistik","bagımlı","obsesif")
            for i in range(0,int(len(isim))):
                test2.setdefault(isim[i],sonuc[i])
            print("Puanlariniz:\n",test2)
            kirma=anamenü(0)
            if kirma==1:
                continue
            elif kirma==2:
                break