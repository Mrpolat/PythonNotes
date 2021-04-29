# -*- coding: utf-8 -*-

import random

x =[1,2,3,4,5]

#indisle beraber indisde bulunan değeride gösterir
for i in enumerate(x):
    print(i)

for indis,eleman in enumerate(x):
    print(indis,eleman)
    
for indis,eleman in enumerate(x):
    print("x[{}]={}".format(indis,eleman))
    
#dizileri kolaylıkla birleştirebiliriz
a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)

x=[
   [1,0,0],
   [0,1,0],
   [0,0,1]
   
   
   ]
print(len(x))
print(len(x[0]))
print(x)

#2 boyutlu dizinin yapılmasının bir yolu
z=[]

for i in range(5):
    z.append([random.randint(1,5) for c in range (4)])
    
print(z)

a=[1,2,3,4,5]

a[0:3]=[3,5,8]
 
#tuplelar değiştirlemez güncellenemez oldukları için önce listeye dönüştürüp daha sonra tekrar tuple yapıyoruz
x=("ali","veli","hakan")
y=list(x)
y[1]="fatma"

x=tuple(y)
print(x)

#atama işlemini tek bir isim ile yapabiliriz solda sağa baz alınır
gizliler=("ali","123")
user,sifre=gizliler
print(user,sifre)

#setler
x={1,2,3,4,1,2}
print(x)
print(len(x))
x.update({1,2,3,5,6})
print(x)

x={"user":"ali","sifre":"123","login_count":5}
#erişim
print(x['user'])
#update
x["user"]="ali cevher"
#yeni key-value ilave etme
x["tckimlik"]="12345678910"
#key-value çifti silme
x.pop("tckimlik")
#sözlükteki eleman sayısı
len(x)

for k,v in x.items():
    print(k,":",v)
    
for k in x.keys():
    print(k)
    
for v in x.values():
    print(v)
    
a=list(x.values())
print(a)