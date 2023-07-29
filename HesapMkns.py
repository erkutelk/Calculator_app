import pandas
class test:
    def __init__(self,sayi1,sayi2) -> None:
        self.sayi1=sayi1
        self.sayi2=sayi2
        self.toplam()
        self.carpma()
        self.cikarma()
        print(self.Birlestir())
    
    def __str__(self) -> str:
        return f'Birinci Sayi :\t{self.sayi1}\nİkinci Sayi: \t{self.sayi2}'

    def toplam(self):
        return self.sayi1+self.sayi2
    
    def cikarma(self):
        if self.sayi1<sayi2:
            return self.sayi2-self.sayi1
        else:
            return self.sayi1-sayi2

    def carpma(self):
        return self.sayi1*self.sayi2

    def Bolme(self):
        try:
            return self.sayi1/sayi2
        except:
            return print('Bilader Düzgün sayı gir bölme çalışmaz')
    
    def Birlestir(self):
        data = {'Sonuç': [self.toplam(), self.cikarma(), self.carpma(),self.Bolme()]}
        df = pandas.DataFrame(data, index=['Toplam', 'Cikarma', 'Carpma','Bolme'])#Carpma Bolme vb yazıların index değeri şeklinde gelmesi için bu kod kullanılmalı
        return df
    

while True:
    print('------------------------------')
    sayi1=int(input('Bir sayi giriniz>\t'))
    sayi2=int(input('Bir sayi giriniz>\t'))
    print('------------------------------')
    isim=test(sayi1,sayi2)
    print(isim)

