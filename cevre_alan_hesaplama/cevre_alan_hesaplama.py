pi = 3.14

class Sekil():
    def __init__(self):
        self.birim1 = "cm"
        self.birim2 = "cm2"
        self.birim3 = "cm3"
        
class Kare(Sekil):
    def __init__(self,kenar):
        super().__init__()
        self.kenar = kenar
        
    def cevrehesapla(self):
        cevre = 4 * self.kenar
        return cevre
    
    def alanhesapla(self):
        alan = self.kenar * self.kenar
        return alan
        
    def sekilyazdir(self):
        print("Kare")
    
    def cevreyazdir(self,cevre):
        print("Cevre =",cevre,self.birim1)
    
    def alanyazdir(self,alan):
        print("Alan =",alan,self.birim2)

class Dikdortgen(Sekil):
    def __init__(self,en,boy):
        super().__init__()
        self.en = en
        self.boy = boy
        
    def cevrehesapla(self):
        cevre = 2 * (self.en + self.boy)
        return cevre
    
    def alanhesapla(self):
        alan = self.en * self.boy
        return alan
        
    def sekilyazdir(self):
        print("Dikdortgen")
    
    def cevreyazdir(self,cevre):
        print("Cevre =",cevre,self.birim1)
    
    def alanyazdir(self,alan):
        print("Alan =",alan,self.birim2)

class Daire(Sekil):
    def __init__(self,yaricap):
        super().__init__()
        self.yaricap = yaricap
        
    def cevrehesapla(self):
        cevre = 2 * pi * self.yaricap
        return cevre
    
    def alanhesapla(self):
        alan = pi * self.yaricap * self.yaricap
        return alan
        
    def sekilyazdir(self):
        print("Daire")
    
    def cevreyazdir(self,cevre):
        print("Cevre =","%.2f" %cevre,self.birim1)
    
    def alanyazdir(self,alan):
        print("Alan =","%.2f" %alan,self.birim2)

class Silindir(Sekil):
    def __init__(self,yaricap,yukseklik):
        super().__init__()
        self.yaricap = yaricap
        self.yukseklik = yukseklik
        
    def hacimhesapla(self):
        hacim = pi * self.yaricap * self.yaricap * self.yukseklik
        return hacim 
    
    def yuzeyalanihesapla(self):
        yuzeyalani = (2 * pi * self.yaricap) * (self.yaricap + self.yukseklik)
        return yuzeyalani
    
    def sekilyazdir(self):
        print("Silindir")
        
    def hacimyazdir(self,hacim):
        print("Hacim =","%.2f" %hacim,self.birim3)
        
    def yuzeyalaniyazdir(self,yuzeyalani):
        print("Yuzeyalani =","%.2f" %yuzeyalani,self.birim2)
        

kenar = int(input("Karenin bir kenarini giriniz: "))
en = int(input("Dikdortgenin enini giriniz : "))
boy = int(input("Dikdortgenin boyunu giriniz :"))
r = int(input("Dairenin yaricapini giriniz :"))
sr = int(input("Silindirin yaricapini giriniz : "))
h = int(input("Silindirin yuksekligini giriniz : "))

kare = Kare(kenar)
kare.sekilyazdir()
ckare = kare.cevrehesapla()
kare.cevreyazdir(ckare) 
akare = kare.alanhesapla()
kare.alanyazdir(akare)

print("")

dikdortgen = Dikdortgen(en,boy)
dikdortgen.sekilyazdir()
cdikdortgen = dikdortgen.cevrehesapla()
dikdortgen.cevreyazdir(cdikdortgen)
adikdortgen = dikdortgen.alanhesapla()
dikdortgen.alanyazdir(adikdortgen)

print("")

daire = Daire(r)
daire.sekilyazdir()
cdaire = daire.cevrehesapla()
daire.cevreyazdir(cdaire)
adaire = daire.alanhesapla()
daire.alanyazdir(adaire)  

print("")

silindir = Silindir(sr,h)
silindir.sekilyazdir()
yasilindir = silindir.yuzeyalanihesapla()
silindir.yuzeyalaniyazdir(yasilindir)
hsilindir = silindir.hacimhesapla()
silindir.hacimyazdir(hsilindir)