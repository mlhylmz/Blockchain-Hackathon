from modul import *
from Crypto import Random
import base64
import pyodbc

#Veritabanı tanımlamaları
server = 'MLHYLMZ' 
database = 'BlockchainDB'


#Veritabanı Bağlantısı
try:
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server}; \
        SERVER='+ server +'; \
        DATABASE='+ database +';\
        Trusted_Connection=yes;'
    )
    cursor = cnxn.cursor()
except:
    print("WARNING !! DATABASE CONNECTION ERROR !!")

while True:
    print("BLOCKCHAIN HACKATHON\n------------\n")
    name = input("İsminiz : ")
    print("- - - - -\nHoşgeldiniz "+name+"\n\n")


    #Mesajı alma ve şifreleme işlemleri
    try:
        temp = input("Şifrelenmesini İstediğiniz Cümleyi Giriniz : ")

        text = sifrelemeYontemleri(temp)

        md5    = text.md5Sifrele()
        sha256 = text.sha256Sifrele()
        sha384 = text.sha384Sifrele()
        sha224 = text.sha224Sifrele()
        sha512 = text.sha512Sifrele()
        caesar = text.caesarSifrele()
        hmac   = text.hmacSifrele()
        des    = text.desSifrele()

    except:
        print("Hata! Metin şifrelenemedi.")
    else:
        print("\n-Metin başarıyla şifrelendi.\n")

    while True:
        secim = int(input("1. Şifrelenmiş verileri veritabanına aktar.\n2. Aktarmadan devam et.\nSeçim : "))

        if secim == 1:
            cursor.execute('INSERT INTO tblsifreleme (md5,sha256,sha224,sha384,sha512,caesar,des,hmac) VALUES (?,?,?,?,?,?,?,?)',md5,sha256,sha224,sha384,sha512,caesar,hmac,hmac)
            cnxn.commit()
            print("\nBaşarıyla veritabanına aktarıldı.")
            break

        elif secim == 2:
            print("\nDevam ediliyor.")
            break

        else:
            print("\nGeçerli seçim yapmadınız!")

        
    while True:
        secim = str(input("\nGirdiğiniz cümleye dilKontrol fonksiyonu uygulamak ister misiniz? [y/n] : "))

        if secim == 'y':

            #DilKontrol İşlemleri
            deneme = dilKontrol(temp)

            sesliHarf = deneme.sesliHarfSay()
            print("\nSesli Harf Sayisi : "+str(sesliHarf))

            cumleSayac= deneme.cumleAyir()
            print("Cümle Sayisi : "+ str(cumleSayac))

            kelimeSayac = deneme.kelimeAyir()
            
            buu = deneme.kuralaBak()

            
            

            while True:
                secim = int(input("\n1. Cümlenin çıktılarını veritabanına aktar.\n2. Aktarmadan devam et.\nSeçim : "))
                if secim == 1:
                    cursor.execute('INSERT INTO tblBuu (buuTSayi,buuFSayi) VALUES (?,?)',buu[0],buu[1])
                    cursor.execute('INSERT INTO tblKelime (cumleSayi,kelimeSayi,sesliSayi) VALUES (?,?,?)',cumleSayac,kelimeSayac,sesliHarf)
                    cnxn.commit()
                    print("\nVeritabanına başarıyla aktarıldı.")
                    break

                elif secim == 2:
                    print("\nDevam ediliyor.")
                    break

                else:
                    print("\nGeçerli seçim yapmadınız.")

            break

        if secim == 'n':
            print("\nUygulanmadı.")
            break

        else:
            print("\nGeçerli seçim yapmadınız.")

    while True:
        secim = int(input("\nVeritbanından çekmek istediğiniz veriyi seçiniz.\n1.SHA-256 Şifreleme\n2.Kelime Sayısı\n3.BÜU na Uyan Kelime Sayısı\n4.Çıkış\nSeçim : "))
        if secim == 1:    
            cursor.execute('SELECT sha256 FROM tblSifreleme WHERE sifreId = (SELECT MAX(sifreId) FROM tblsifreleme)')
            a = cursor.fetchone()
            b = a[0]
            print("\nSHA-256 : "+str(b))
        elif secim == 2:
            cursor.execute('SELECT kelimeSayi FROM tblKelime WHERE kelimeSayiId = (SELECT MAX(kelimeSayiId) FROM tblKelime)')
            a = cursor.fetchone()
            b = a[0]
            print("\nKelime Sayı : "+str(b))
        elif secim == 3:
            cursor.execute('SELECT buuTSayi FROM tblBuu WHERE buuId = (SELECT MAX(buuId) FROM tblBuu)')
            a = cursor.fetchone()
            b = a[0]
            print("\nBÜU na Uyan Kelime Sayısı : "+str(b))
        else:
            break


    print("Program kapatılıyor.")
    cursor.close()
    break


    '''yardim = helpMeAt()
    yardim.helpMd5Sifrele()
    yardim.helpSesliHarfSay()
    yardim.helpKuralaBak()
    yardim.helpCumleAyir()'''


    #Veritabanına verileri gönderme işlemleri
    '''
    cursor.execute('INSERT INTO tblBuu (buuTSayi,buuFSayi) VALUES (?,?)',buu[0],buu[1])
    cursor.execute('INSERT INTO tblsifreleme (md5,sha256,sha224,sha384,sha512,caesar,des,hmac) VALUES (?,?,?,?,?,?,?,?)',md5,sha256,sha224,sha384,sha512,caesar,str(des),hmac)
    cursor.execute('INSERT INTO tblKelime (cumleSayi,kelimeSayi,sesliSayi) VALUES (?,?,?)',cumleSayac,kelimeSayac,sesliHarf)
    cnxn.commit()
    '''






