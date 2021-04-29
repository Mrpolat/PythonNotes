# -*- coding: utf-8 -*-

try:
    a=5/0
except:
    print("istisna oluştu")
else:
    print(a)
#list set tuple ve dict zaten itere edileilir

#kendi iter fonksiyonumuz

class Ciftler:
    def __iter__(self):
        self.a =2
        return self
    
    def __next__(self):
        if self.a <10:
            x=self.a
            self.a +=2
            return x
        else:
            raise StopIteration
            
sinif = Ciftler()

x=iter(sinif)
print(next(x))

b=[0,1]
y=[b.append(b[i-1]+b[i]) for i in range(1,10)] 
print(y)