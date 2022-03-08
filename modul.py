import hashlib
from Crypto import Random
import base64
import pyDes
from nltk.tokenize import word_tokenize, sent_tokenize
import hmac


class sifrelemeYontemleri:

    def __init__(self,text_main,text = "default"):
        self.text_main = text_main
        self.text = self.text_main


    def __set__(self, x):
        self.text_main = x

    def __get__(self):
        return self.text_main

    def yazdir(self):
        print(self.text_main)

    def md5Sifrele(self):
        self.text = self.text_main
        self.text = hashlib.md5(self.text.encode())
        #print("MD5 : "+self.text.hexdigest())
        return self.text.hexdigest()

    def sha256Sifrele(self):
        self.text = self.text_main
        self.text = hashlib.sha256(self.text.encode())
        #print("SHA-256 : "+self.text.hexdigest())
        return self.text.hexdigest()

    def sha384Sifrele(self):
        self.text = self.text_main
        self.text = hashlib.sha384(self.text.encode())
        #print("SHA-384 : "+self.text.hexdigest())
        return self.text.hexdigest()

    def sha224Sifrele(self):
        self.text = self.text_main
        self.text = hashlib.sha224(self.text.encode())
        #print("SHA-224 : "+self.text.hexdigest())
        return self.text.hexdigest()

    def sha512Sifrele(self):
        self.text = self.text_main
        self.text = hashlib.sha512(self.text.encode())
        #print("SHA-512 : "+self.text.hexdigest())
        return self.text.hexdigest()

    def caesarSifrele(self):
        self.text = self.text_main
        temp = ""
        for x in self.text:
            temp = temp + chr(ord(x) + 1)
        self.text = temp
        #print("Caesar Şifreleme : "+self.text)
        return self.text

    def desSifrele(self):
        self.text = self.text_main
        k = pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
        self.text = k.encrypt(self.text)

        #print("DES : ")
        #print(self.text)
        #print(k.decrypt(self.text))
        return self.text

    def hmacSifrele(self):
        self.text = self.text_main
        key = "loremipsum"
        self.text = hmac.new(key.encode(encoding="utf-8"),self.text.encode("utf8"),hashlib.md5)
        #print("HMAC : "+str(self.text.hexdigest()))
        return self.text.hexdigest()

class dilKontrol:
    def __init__(self,word_main,word = "d",cumleler = "d",kelimeler = "d",sesliHarf = "d",buut = 0,buuf = 0,bos = []):
        self.word_main = word_main
        self.word = word_main
        self.cumleler = cumleler
        self.kelimeler = kelimeler
        self.count = 0
        self.sesliHarf ="AEIİOÖUÜaeıioöuü"
        self.buut = 0
        self.buuf = 0
        self.bos = []


    def sesliHarfSay(self):
        self.count = 0
        for i in self.word_main:
            if i in 'AEIİOÖUÜaeıioöuü':
                self.count += 1      
        return self.count

    def cumleAyir(self):
        self.word = self.word_main
        self.cumleler = sent_tokenize(self.word)
        print("Cümleler : "+str(self.cumleler)+"\n")
        self.count = 0
        for element in self.cumleler:
            self.count += 1
        return self.count

    def kelimeAyir(self):
        self.word = self.word_main
        if self.word.endswith("."):
            pass
        else:
            self.word = self.word + " ."
        if self.word.endswith("!"):
            pass
        else:
            self.word = self.word + " !"
        if self.word.endswith("?"):
            pass
        else:
            self.word = self.word + " ?"
        
        self.kelimeler = word_tokenize(self.word)
        
        try: 
            if self.kelimeler.index("."):
                for i in range(0,self.count):
                    self.kelimeler.remove(".")
        except:
            print(" ")

        try:
            if self.kelimeler.index("!"):
                for i in range(0,self.count):
                    self.kelimeler.remove("!")
        except:
            print(" ")
            
        try:
            if self.kelimeler.index(","):
                for i in range(0,self.count):
                    self.kelimeler.remove(",")
        except:
            print(" ")

        try:
            if self.kelimeler.index("?"):
                for i in range(0,self.count):
                    self.kelimeler.remove("?")
        except:
            print(" ")

        
                
        print("Kelimeler : "+str(self.kelimeler))
        self.count = len(self.kelimeler)
        print("\nKelime Sayisi : "+ str(len(self.kelimeler)))
        return self.count

    def kuralaBak(self):
        self.count = 0
        kalin_unluler = ['a', 'ı', 'o', 'u']
        ince_unluler = ['e', 'i', 'ö', 'ü']
        sentence = self.kelimeler
        for i in self.word_main:
            if i in 'AEIİOÖUÜaeıioöuü':
                self.count += 1
        if(self.count == 1):
            print("Aranmaz")
            
        else:
            for i in self.kelimeler:
                if (sum(i.count(kalin) for kalin in kalin_unluler)) != 0 and (sum(i.count(ince) for ince in ince_unluler)) != 0:
                    self.buuf = self.buuf + 1
                    print(f"'{i.capitalize()}' Büyük Ünlü Uyumuna Uymaz.")
                else:
                    self.buut = self.buut + 1
                    print(f"'{i.capitalize()}' Büyük Ünlü Uyumuna Uyar.")
        print("\nBüyük ünlü uyumuna uyan kelime sayısı: "+ str(self.buut))
        print("Büyük ünlü uyumuna uymayan kelime sayısı:"+ str(self.buuf))
        return self.buut , self.buuf



class helpMeAt:
    def helpMd5Sifrele(self):
        print('''   

        -MD5 FONKSİYON YARDIM-

        Kütüphane : hashlib

        Girilen mesajı MD5 kullanarak şifreler.'self.text_main' ana mesajdır. 
        Self.texte eşitler ve 'hashlib.md5(self.text.encode())'komutuyla 
        şifreleme yapar. String olarak geri gönderir.

        self.text = self.text_main
        self.text = hashlib.md5(self.text.encode())
        return self.text.hexdigest()''')

    def helpSha256Sifrele(self):
        print('''   

        -SHA-256 FONKSİYON YARDIM-

        Kütüphane : hashlib

        Girilen mesajı SHA-256 kullanarak şifreler.'self.text_main' ana mesajdır. 
        Self.texte eşitler ve 'hashlib.sha256(self.text.encode())'komutuyla 
        şifreleme yapar. String olarak geri gönderir.

        self.text = self.text_main
        self.text = hashlib.sha256(self.text.encode())
        return self.text.hexdigest()''')

    def helpSha384Sifrele(self):
        print('''   

        -SHA-384 FONKSİYON YARDIM-

        Kütüphane : hashlib

        Girilen mesajı SHA-384 kullanarak şifreler.'self.text_main' ana mesajdır. 
        Self.texte eşitler ve 'hashlib.sha384(self.text.encode())'komutuyla 
        şifreleme yapar. String olarak geri gönderir.

        self.text = self.text_main
        self.text = hashlib.sha384(self.text.encode())
        return self.text.hexdigest()''')

    def helpSha224Sifrele(self):
        print('''   

        -SHA-224 FONKSİYON YARDIM-

        Kütüphane : hashlib

        Girilen mesajı SHA-224 kullanarak şifreler.'self.text_main' ana mesajdır. 
        Self.texte eşitler ve 'hashlib.sha224(self.text.encode())'komutuyla 
        şifreleme yapar. String olarak geri gönderir.

        self.text = self.text_main
        self.text = hashlib.sha224(self.text.encode())
        return self.text.hexdigest()''')

    def helpSha512Sifrele(self):
        print('''   

        -SHA-512 FONKSİYON YARDIM-

        Kütüphane : hashlib

        Girilen mesajı SHA-512 kullanarak şifreler.'self.text_main' ana mesajdır. 
        Self.texte eşitler ve 'hashlib.sha512(self.text.encode())'komutuyla 
        şifreleme yapar. String olarak geri gönderir.

        self.text = self.text_main
        self.text = hashlib.sha512(self.text.encode())
        return self.text.hexdigest()''')

    def helpCaesarSifrele(self):
        print('''


        -CAESAR ŞİFRELEM YARDIM-

        Built-in Function

        Girilen mesajı Caesar tekniğini kullanarak şifreler.Her harfi ascii koduna göre
        belirtilen sayıda ileri veya geri öteler. Şifreleme for döngüsü içinde gerçekleşir.
        Şifre string olarak geri döner.

        self.text = self.text_main
        temp = ""
        for x in self.text:
            temp = temp + chr(ord(x) + 1)
        self.text = temp
        return self.text
            ''')

    def helpDesSifrele(self):
        print('''


        -DES ŞİFRELEME YARDIM-

        Kütüphane : PyDes

        Girilen mesajı simetrik şifreleme yöntemi DES ile şifreler.İlk olarak şifrelenecek 
        Metin sol ve sağ olarak 2 parçaya ayrılır. Daha sonra bu parçalar 
        ayrı ayrı bir işlemden geçer. Bu işlemde parçalardan biri ve anahtar F fonksiyonuna girer 
        ve sonrasında diğer parça ile XOR işlemine uğrar. Son olarak parçaların yerleri değiştirilir.
        Bu işlem 'pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)'
        komutu sayesinde kullanılır.Byte olarak geri döner.

        Not : Türkçe karakter desteği yoktur.

        self.text = self.text_main
        k = pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
        self.text = k.encrypt(self.text)
        return self.text
            ''')

    def helpHmacSifreleme(self):
        print('''


        -HMAC ŞİFRELEME YARDIM-

        Kütüphane : hmac , hashlib

        Girilen mesajı verilen keye göre hash kullanarak şifreler.Key fonksiyonda tanımlıdır.
        'hmac.new(key.encode(encoding="utf-8"),self.text.encode("utf8"),hashlib.md5)' kodu yardımıyla
        şifreleme gerçekleştirilir.

        self.text = self.text_main
        key = "loremipsum"
        self.text = hmac.new(key.encode(encoding="utf-8"),self.text.encode("utf8"),hashlib.md5)
        return self.text.hexdigest()

            ''')

    def helpSesliHarfSay(self):
        print('''

        -sesliHarfSay FONKSİYON YARDIM-

        built-in function

        Mesajımız for içinde döngüye sokulur. Harfler tek tek önceden tanımladığımız
        sesli harflerde aratılır. Eşleşme  bulunursa sayaca +1 eklenir. Int olarak geri döner.

        self.count = 0
        for i in self.word_main:
            if i in 'AEIİOÖUÜaeıioöuü':
                self.count += 1
        return self.count
            ''')

    def helpCumleAyir(self):
        print('''

        -cumleAyir FONKSİYON YARDIM-

        Kütüphane : nltk.tokenize(sent_tokenize)

        Boş string içine sent_tokenize fonksiyonu kullanılarak mesajımız cümlelere ayırılır.
        Bir liste içinde tutulur.Artı olarak cümleleri sayıp int olarak geri döndürür.

        self.word = self.word_main
        self.cumleler = sent_tokenize(self.word)
        print(self.cumleler)
        self.count = 0
        for element in self.cumleler:
            self.count += 1
        return self.count
            ''')

    def helpKelimeAyir(self):
        print('''

        -kelimeAyir FONKSİYON YARDIM-

        Kütüphane : nltk.tokenize(word_tokenize)

        Boş string içine word_tokenize fonksiyonu kullanılarak mesajımız kelimelere ayırılır.
        Bir liste içinde tutulur.if ve for döngüsü kullanılarak kelimeler noktalardan , virgüllerden,
        ünlemlerden ve soru işaretlerinden arındırılır.
        Artı olarak kelimeler sayılıp int olarak geri döndürülür.

        self.word = self.word_main
        self.kelimeler = word_tokenize(self.word)
        if self.kelimeler.index("."):
            for i in range(0,self.count):
                self.kelimeler.remove(".")
                
        print(self.kelimeler)
        self.count = len(self.kelimeler)
        print("Kelime Sayisi : "+ str(len(self.kelimeler)))
        return self.count

            ''')

    def helpKuralaBak(self):
        print('''

        -kuralaBak FONKSİYON YARDIM-

        Fonksiyonda kalin_unluler ve ince_unluler tanımlı olarak gelmektedir.Kelimeler for döngüsüne sokulur.
        For döngüsü içinde Büyük Ünlü Uyumu kuralına tabi tutulur. Uyan kelimeler self.buut uymayan kelimeler 
        self.buuf içine atılır.
        List olarak geri döner.

        kalin_unluler = ['a', 'ı', 'o', 'u']
        ince_unluler = ['e', 'i', 'ö', 'ü']
        sentence = self.kelimeler
        for i in self.kelimeler:
            if (sum(i.count(kalin) for kalin in kalin_unluler)) != 0 and (sum(i.count(ince) for ince in ince_unluler)) != 0:
                self.buuf = self.buuf + 1
                print(f"'{i.capitalize()}' Büyük Ünlü Uyumuna Uymaz.")
            else:
                self.buut = self.buut + 1
                print(f"'{i.capitalize()}' Büyük Ünlü Uyumuna Uyar.")
        print("BÜU uyan kelime : "+ str(self.buut))
        print("BÜU uymayan kelime :"+ str(self.buuf))
        return self.buut , self.buuf


            ''')    