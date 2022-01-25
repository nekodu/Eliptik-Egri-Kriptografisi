# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 23:43:07 2022

@author: nekodu
"""



# For-loop her nekadar küçük asal sayılar için yazılabilir olsada, büyük asal sayıları bu looptan geçirmek çook uzun 
#sürüyor !!!!!!!


import math


#Soyut bir sonsuz nokta gerekiyordu.
SNSZ_NOKTA = None

class EliptikEgri:
    
    #Eğrinin tanımlanacağı noktalar
    def __init__(self,a,b,p): 
        self.a = a
        self.b = b
        self.p = p
        #Eğrinin üzerindeki noktalar, y^2=x^3+ax+b denklemini sağlayan x,y noktaları
        self.noktalar =[]
        self.noktalari_sapta()
        
        #Verilen eğrideki noktaları saptar.
    def noktalari_sapta(self):
        self.noktalar.append(SNSZ_NOKTA)
        
        #Denkelemi bulmak için gereken tüm çiftler taranıyor.
        for x in range (self.p):
            for y in range(self.p):
                if self.denk_modp(y * y, x * x * x + self.a * x + self.b):
                    #Bir çözüm bulunduğunda noktalar listesine ekleniyor.
                    self.noktalar.append((x,y))
                    
                    # Yukarıdaki işlemde küçük asal sayılar listeye sığıyor fakat büyük asal sayılar geldiğinde
                    #bu kadar fazla sayıyı depolamak mümkün olmuyor.Dünyadaki toplam veri 4 * 10^22 eliptik eğrideki
                    #nokta sayısı 1.5 * 10^69
    
    
    def ekleme(self,P1,P2):
        if P1 == SNSZ_NOKTA:
            return P2
        if P2 == SNSZ_NOKTA:
            return P1
        
        x1 = P1[0]
        y1 = P1[1]
        x2 = P2[0]
        y2 = P2[1]
        
        if self.denk_modp(x1, x2) and self.denk_modp(y1, -y2):
            return SNSZ_NOKTA

        if self.denk_modp(x1, x2) and self.denk_modp(y1, y2):
            # u = lambda işareti ve p1 ve p2 arasındaki eğim
            u = self.eksilt_modp((3 * x1 * x1 + self.a) * self.ters_modp(2 * y1))
        else:
            u = self.eksilt_modp((y1 - y2) * self.ters_modp(x1 - x2))
            
        v = self.eksilt_modp(y1 - u * x1)
        x3 = self.eksilt_modp(u * u - x1 - x2)
        y3 = self.eksilt_modp(-u * x3 - v)

#Gerçekleştirilen binary operasyonunun p1 ve p2 nokataları sonucu
        return (x3, y3)
#Gerçekleştirilen binary operasyonun brileşim özelliğini kontrol etmek için gereken fonksiyon
    def test_birlesim(self):
        n = len(self.noktalar)
        for i in range (n):
            for j in range(n):
                for k in range(n):
                    P = self.ekleme(self.noktalar[i], self.ekleme(self.noktalar[j], self.noktalar[k]))
                    Q = self.ekleme(self.ekleme(self.noktalar[i], self.noktalar[j]), self.noktalar[k])
                    if P != Q:
                        return ("Yok")#false
        return ("Var")#true
            
    def nokta_sayısı(self):
        return len(self.noktalar)
    
        
    def print_noktalar(self):
            print(self.noktalar)
            
   
            
    def diskriminant(self):
        D = -16*(4 * self.a * self.a * self.a + 27 * self.b*self.b)
        return self.eksilt_modp(D)
    
    
    def hasse_ispat(self):
        return abs(self.nokta_sayısı() - (self.p + 1)) <= 2 * math.sqrt(p)
        
####################### Yardımcı Fonksiyonlar ##########################
        
        #Modp'nin 0 ile p-1 arasında olması için eksiltme fonksiyonu
    def eksilt_modp(self,x):
        return x % self.p 
        
  
        
        #İki integerın Modp'ye göre eşitliğini kontrol eder.
    def denk_modp(self,x,y):
            return self.eksilt_modp (x-y) == 0
        
        
        #Modp'ye göre  Fp nin 0 olamayan çarpılabilir tersleri 
    def ters_modp(self,x):
        #Bruteforce kullanarak.
        for y in range(self.p):
            if self.denk_modp(x*y, 1):
                return y
        return None
        






p= 101
#a = 9
#b= 23

epsilon = 2 * math.sqrt(p)
hasse_alt_sınır = math.ceil((p+1) - epsilon)
hasse_üst_sınır = math.floor((p+1) + epsilon)

#A ve B deki spesifik bir eğim yerine her mümkün sonuca bakmak için


grup_derecesi=[]

for a in range (0, p):
    for b in range(0, p):
        ee = EliptikEgri(a, b, p)
        if ee.diskriminant()== 0:
            continue
        grup_derecesi.append(ee.nokta_sayısı())
        if ee.hasse_ispat() == False:
            print("Hasse Teoremi gerçekleşitirilemedi")
            break


print("alt sınır = ", hasse_alt_sınır)
print("Minimum grup dizisi", min(grup_derecesi))
print("üst sınır = ", hasse_üst_sınır)
print("Maksimum grup dizisi", max(grup_derecesi))


# Hasse intervalindeki tüm numaraların bir eliptik eğriye denk gelip gelmediğini
#test etmek için

derecesiz_grup = []
for i in range(hasse_alt_sınır, hasse_üst_sınır+1):
    if i not in grup_derecesi:
        derecesiz_grup.append(i)
        
if len(derecesiz_grup) == 0:
    print("Mümkün aralıktaki tüm integerlar grubun derecesidir.")
else:
    #bu olmaması gerekiyor
    print("Bu integerlar eliptik eğrinin bir derecesi değildir.")
    print(derecesiz_grup)

#Ortamala grup derecesi
print("Ortalama grup derecesi =", sum(grup_derecesi) / len(grup_derecesi))
print("p+1 =", p+1)















#Küçük bir deneme

# ee = EliptikEgri(2, 7, 19)
# ee.print_noktalar()
# print(ee.nokta_sayısı())
# print(ee.diskriminant())# Sonuç 0 değil ise bunun bir eliptik eğri olduğunu anlayabiliriz.
# N = ee.ekleme(ee.noktalar[5], ee.noktalar[14])
# print(N)
# print(ee.test_birlesim())



# p=7
# count=0
# for a in range(p):
#         for b in range(p):
#             ee = EliptikEgri(a, b, p)
#             if ee.diskriminant()==0:
#                 continue
#             count +=1
#             print("a="+ str(a)+ "  b="+str(b))
#             print("diskriminant="+ str(ee.diskriminant()))
#             print("Noktaların Sayısı=" + str(ee.nokta_sayısı()))
#             print("Birleşim= " + str(ee.test_birlesim()))
#             ee.print_noktalar()
#             print("==========================================")
            
# print("F"+ str(p)+ " üzerindeki eliptik eğrideki numaraların sayısı =" + str(count))

