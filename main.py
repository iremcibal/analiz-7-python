print("Merhaba Etiya")

#yorum satırı 

print("Hoş geldiniz")
print("Hoş geldiniz user")
print("Hoş geldiniz User")
print("Hoş geldiniz User")

#degiskenler

#string 
text = "Merhaba Hoşgeldiniz"
print(text)
print(text)
print(text)
print(text)

studentCount = 45
#integer,int => tam sayı 
#studentCount = 45
#student = "50"
#print(studentCount + student)

print(studentCount + 5)

#double,decimal,float => ondalıklı sayıları ifade etmek için kullanırız
averagePoint = 25.5
print(averagePoint + 5)

#Boolean,Bool - karar yapılarını göstermek için 
isVerified = True
print(isVerified)

#Değişkenlerinin tipini öğrenmek için ;
print(type(text))
print(type(studentCount))
print(type(averagePoint))
print(type(isVerified))

#Operatörler => Matematiksel/Mantıksal Operatörler

#Matematiksel Operatörler
#+ - / * %

number = 10

print(number + number)
print(10 + 10)

print(number - 2)

print(number / 2)

print(number * 2)
#mod operatörü
#10/3 => 1
print(number % 3)

print(number + ((10-number) * (5/10))) 

#Mantıksal Operatörler - Karşılaştırma operatörleri
print(10 == 10) #true
print(11 == 10) #false
print(number == 10) #true

print(10 != 10) #false
print(11 != 10) #true

print(number>8) #true
print(number>= 10) #true

print(number < 10) #false
print(number <= 10) #true


#string interpolation => metin birleştirme
hello = "Merhaba"
userName = "irem"
totalText = hello + " " + userName
print(totalText)

totalText = "{message} {name}".format(message= "merhaba", name=userName)
print(totalText)

#f-string
totalText = f"Hoşgeldiniz {userName}"
print(totalText)

#Diziler

sayilar = [100,200,300,"Merhaba"]

#Programcı olarak sıfırdan saymaya başlıyoruz 
#index indis => 0 başlangıc değeri -1 son index
print(sayilar[1])
print(sayilar[0])
print(sayilar[-1])

print(sayilar)

degisken =[100,1,2,3]
sayilar.append(degisken)
print(sayilar)
print(sayilar[4][1])
sayilar.append(600)
print(sayilar)

sayilar.pop(3) #indexteki elemanı siler - default olarak son index
print(sayilar)

sayilar.remove(100) #Değere göre siler - Bulduğu ilk veriyi siler
print(sayilar)

dizi=[10,20,30] #tek bir değer değil listedeki tüm elemanları ekler
sayilar.extend(dizi)
print(sayilar)

sayilar.clear() 
print(sayilar)

#karar yapıları 

ortalamaNot = input("Lütfen ortalamanızı giriniz.")
#string=> int dönüşümü
#type conversion
print(type(ortalamaNot))
ortalamaNotInteger= int(ortalamaNot)
print(type(ortalamaNotInteger))

#indent => 1 tabl içerisinde olmak
""" if ortalamaNotInteger > 50 :
    print("Harika")
    if ortalamaNotInteger >80:
        print("Başarılı")
else:
    print("Kaldınız") """


if ortalamaNotInteger >80:
    print("Başarılı")
#else if => elif
elif ortalamaNotInteger >60:
    print("ortalama")
elif ortalamaNotInteger >50:
    print("normal")
else:
    print("Kaldınız")


studentCount=44
if studentCount >20:
    print("Ögrenciler derse hazır")

#10:05 :)













