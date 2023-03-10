 Python bünyesinde şu veri tiplerini barındırır:

# String (metin) → str
# Örnek olarak : metin = "batuhan" metin karakterlerini barındırırız.

# Numerik (sayısal) → int, float, complex
# Örnek olarak : b = 56 sayıları bu veri tipinde tutarız.

# Sequence (sıralama)→ list, tuple, range
# Örnek olarak : #eğitim aşamasında bunun hakkında daha bilgi edinmedim.

# Mapping (haritalama) → dict
# Örnek olarak : #eğitim aşamasında bunun hakkında daha bilgi edinmedim.

# Set → set, frozenset
# Örnek olarak : #eğitim aşamasında bunun hakkında daha bilgi edinmedim.

# Boolean → bool
# Örnek olarak : a = True, c = False Mantıksal ifadelerini tutan bir yapıdır.

# Binary → bytes, bytearray, memoryview
# Örnek olarak : #eğitim aşamasında bunun hakkında daha bilgi edinmedim.

# --------------------------------------------------------------------------------------------
-> Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.

# Sitede metinsel ifadeler (str) veri tipinde tutuluyor olabilir.
# Ders başarı ilerlemeler ise (int) veri tipinde tutuluyor olabilir.







->Kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz ve Python dilinde bu örnekleri koda dökünüz.
# 1-) Kullanıcı login kısmında girilen bilgilerin doğruluğunu kontrol eden bir şart bloğu yapısı olabilir.



Kodlamaio sayfasının login kısmının arka planındaki kod yapısında;


#eğitimde daha kullanıcadan giriş görmediğimiz için , önceden kayıtlı bir data varsıyımıdır.
mail = "ornek@gmail.com"
sifre = "orneksifre"

while True:

    mailgiris = input(" Kayıtlı mail adresinizi giriniz: ")
    sifregiris = input("Lütfen Sifrenizi giriniz: ")

    if mailgiris == mail and sifregiris == giris:

        print("Kullanıcı bilgileri dogru... ")
        

    else:
        
        print("Girdiginiz bilgiler hatalidir. Lütfen tekrar deneyiniz ! ")
