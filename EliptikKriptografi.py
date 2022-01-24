# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 23:43:07 2022

@author: nekodu
"""

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
        self.noktalariSapta()
        
        #Verilen eğrideki noktaları saptar.
    def noktalariSapta(self):
        self.noktalar.append(SNSZ_NOKTA)
        
        #Denkelemi bulmak için gereken tüm çiftler taranıyor.
        for x in range (self.p):
            for y in range(self.p):
                if self.denkModp(y * y, x * x * x + self.a * x + self.b):
                    #Bir çözüm bulunduğunda noktalar listesine ekleniyor.
                    self.noktalar.append((x,y))
    
    
    def ekleme(self,P1,P2):
        if P1 == SNSZ_NOKTA:
            return P2
        if P2 == SNSZ_NOKTA:
            return P1
        
        x1 = P1[0]
        y1 = P1[1]
        x2 = P2[0]
        y2 = P2[1]
        
        if self.denkModp(x1, x2) and self.denkModp(y1, -y2):
            return SNSZ_NOKTA

        if self.denkModp(x1, x2) and self.denkModp(y1, y2):
            u = self.eksiltModp((3 * x1 * x1 + self.a) * self.tersModp(2 * y1))
        else:
            u = self.eksiltModp((y1 - y2) * self.tersModp(x1 - x2))

        v = self.eksiltModp(y1 - u * x1)
        x3 = self.eksiltModp(u * u - x1 - x2)
        y3 = self.eksiltModp(-u * x3 - v)

        return (x3, y3)
    
    def testBirlesim(self):
        n = len(self.noktalar)
        for i in range (n):
            for j in range(n):
                for k in range(n):
                    P = self.ekleme(self.noktalar[i], self.ekleme(self.noktalar[j], self.noktalar[k]))
                    Q = self.ekleme(self.ekleme(self.noktalar[i], self.noktalar[j]), self.noktalar[k])
                    if P != Q:
                        return False
        return True
            
    def noktaSayısı(self):
        return len(self.noktalar)
    
        
    def printNoktalar(self):
            print(self.noktalar)
            
   
            
    def diskriminant(self):
        D = -16*(4 * self.a * self.a * self.a + 27 * self.b*self.b)
        return self.eksiltModp(D)
        
####################### Yardımcı Fonksiyonlar ##########################
        
        
    def eksiltModp(self,x):
        return x % self.p 
        
  
        
        #İki integerın Modp'ye göre eşitliğini kontrol eder.
    def denkModp(self,x,y):
            return self.eksiltModp (x-y) == 0
        
        
        #Modp'ye göre  Fp nin 0 olamayan çarpılabilir tersleri 
    def tersModp(self,x):
        #Bruteforce kullanarak.
        for y in range(self.p):
            if self.denkModp(x*y, 1):
                return y
        return None
        


ee = EliptikEgri(2, 7, 19)
ee.printNoktalar()
print(ee.noktaSayısı())
print(ee.diskriminant())# Sonuç 0 değil ise bunun bir eliptik eğri olduğunu anlayabiliriz.
N = ee.ekleme(ee.noktalar[5], ee.noktalar[14])
print(N)
print(ee.testBirlesim())

p=7
count=0
for a in range(p):
        for b in range(p):
            ee = EliptikEgri(a, b, p)
            if ee.diskriminant()==0:
                continue
            count +=1
            print("a="+ str(a)+ "  b="+str(b))
            print("diskriminant="+ str(ee.diskriminant()))
            print("Noktaların Sayısı=" + str(ee.noktaSayısı()))
            print("Birleşim= " + str(ee.testBirlesim()))
            ee.printNoktalar()
            print("==========================================")
            
print("F"+ str(p)+ " üzerindeki eliptik eğrideki numaraların sayısı =" + str(count))

