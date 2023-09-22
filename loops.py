#For 
for i in range(10):
    print(i)

#start,stop,step
for i in range(3,10,2):
    print(i)

#Kullanıcının vereceği üst limit ile alt limitten üst limite 
#kadar olan tüm çift sayılar yazılsın
""" forRangeMin = int(input("Döngünün alt limitini belirleyiniz."))
forRangeMax = int(input("Döngünün üst limitini belirleyiniz."))

for i in range(forRangeMin,forRangeMax+1):
    if i % 2 == 0 :
        print(i) """


#sayılar arasında en büyüğünü veren bir program
biggestValue = 0
""" for i in range(10):
    sayi= int(input(f"{i+1}. sayıyı giriniz."))
    if sayi > biggestValue:
        biggestValue = sayi


print(f"Girdiğiniz sayılar arasında en büyük olanı : {biggestValue}") """
hello= "merhaba"
userName= "irem"
totalText = hello +"Hoşgeldiniz" + userName
print(totalText)
totalText = f"Hoşgeldiniz {biggestValue} {userName}"
print(totalText)


sayilar = []
""" for i in range(3):
    sayilar.append(int(input(f"{i+1}. sayıyı giriniz: ")))

sayilar.sort(reverse=True) #default => küçükten büyüğe 
print(sayilar)
enbüyük = int(input("Sayılar arasında en büyük kaçıncı elemanı istiyorsunuz?" ))
print(sayilar[enbüyük-1]) """

ogrenciler = ["Yaren","Elif","Alpay","Elçin"]
#0 1 2 3
#4
print(len(ogrenciler))

for x in range(len(ogrenciler)):
    print(ogrenciler[x])

for ogrenci in ogrenciler:
    print(f"Ögrenci: {ogrenci}")
print("---------------------------------------------------")
#break => ilgili döngünün o anda kırılmasını sağlar
#continue => o an ki current değerini atlayıp bi sonraki değer ile devam etmemizi söyler

for i in range(len(ogrenciler)):
    if i > 1:
        break
    print(f"{i+1}. Ögrenci : {ogrenciler[i]}")


for i in ogrenciler:
    if i == "Elif":
        continue
    print(f"ogrenci: {i}")


#While
i=0
while i <10:
    print("merhaba")
    i=i+1  #i++


while True:
    print("hello")