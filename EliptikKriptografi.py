SNSZ_NOKTA = None

class EliptikEgri:
    #Eğrinin tanımlanacağı noktalar
	def __init__(self, p, a, b):
		self.p = p
		self.a = a
		self.b = b


	def ekleme(self, P1, P2):
		if P1 == SNSZ_NOKTA:
			return P2
		if P2 == SNSZ_NOKTA:
			return P1

		(x1, y1) = P1
		(x2, y2) = P2

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


	def carpim(self, k, P):
		Q = SNSZ_NOKTA
		while k != 0:
			if k & 1 != 0:
				Q = self.ekleme(Q, P)
			P = self.ekleme(P, P)
			k >>= 1
		return Q


	def nokta_egimde_mi(self, x, y):
		return self.denk_modp(y * y, x * x * x + self.a * x + self.b)


####################### Yardımcı Fonksiyonlar ##########################

#Modp'nin 0 ile p-1 arasında olması için eksiltme fonksiyonu
	def eksilt_modp(self, x):
		return x % self.p

#İki integerın Modp'ye göre eşitliğini kontrol eder.
	def denk_modp(self, x, y):
		return self.eksilt_modp(x - y) == 0

        #Brutfotce ve for loop ile bu işlem çok yavaş çok yavaş
    # def ters_modp(self,x):
    #     #Bruteforce kullanarak.
    #     for y in range(self.p):
    #         if self.denk_modp(x*y, 1):
    #             return y
    #     return None
    
    #Fermatın küçük teoremi ile 

	def ters_modp(self, x):
		if self.eksilt_modp(x) == 0:
			return None
		return pow(x, p - 2, p)

# Dökümandan aldığım asal sayı
p = 26959946667150639794667015087019630673557916260026308143510066298881
a = -3
b = 18958286285566608000408668544493926415504680968679321075787234672564

P224 = EliptikEgri(p, a, b)

#Generative ponits(noktalar)
Gx = 19277929113566293071110308034699488026831934219452440156649784352033
Gy = 19926808758034470970197974370888749184205991990603949537637343198772
G = (Gx, Gy)

print(P224.nokta_egimde_mi(Gx, Gy))

Q = P224.carpim(1, G)
print(Q == G)

n = 26959946667150639794667015087019625940457807714424391721682722368061

Q = P224.carpim(n - 1, G)
print(Q)
print(P224.nokta_egimde_mi(Q[0], Q[1]))

Q = P224.carpim(n, G)
print(Q == SNSZ_NOKTA)