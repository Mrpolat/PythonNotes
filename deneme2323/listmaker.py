# -*- coding: utf-8 -*-
#liste yapıcılar
range(1,10,2)

a=list(range(1,10,2))

b=tuple(range(1,10,2))

c=set(range(1,10,2))

print(a,b,c)

#liste yi atama
x=list(range(1,5))

y=[i for i in x]

z=[i**2 for i in x]

print(y,z)

#döngü ile listeyi taşıma
z= [[i,i**2] for i in x]
print(z)

#set şeklinde key value değerleri ile atama
z=[{str(i):i} for i in x]
print(z)

#set şeklinde key value değerleri ile atama
a=["polat","melisa","adem","nesrin"]

b=["iyi","güzel","çirkin","boş"]

z=[{str(a[i]):b[i]} for i in range(len(a))]
print(z)

#tipi sayı olanları atama
x=["a",1,2,3,"b","c",4,5,6]

y=[i for i in x if str(i).isdigit()]
print(y)

#ortalaması yüzde20 uzak olan notları bulma
x = (30,40,50,60,70,80,90)
top = 0
for i in x:
    top=+i
    print(i)
ort = top/(len(x))
print(ort)

yeni_liste=[]

for a in x:
    if a<ort-ort*20/100:
        yeni_liste.append(a)
    if a>ort+ort*20/100:
        yeni_liste.append(a)
print(yeni_liste)

#ortalaması yüzde20 uzak olan notları bulma tek satırda örnek
x=[0,1,2,3,4,5,6,7,8,9,10]
yuzde=20

y=[i for i in x if {i>((yuzde+100)*sum(x)) / (len(x)*100) or i<((100-yuzde)*sum(x)) / len(x)*100}]
print(y)

#sayıları eşleştirme        
x=[1,2,3]
y=["a","b","c"]

z=[ [i,k] for i in x for k in y]
print(z)
#içerisinde nokta bulunan şifreleri bulma
sifreler=["ali123","234.","polat."]

x=[ i for i in sifreler if "." in i]
print(x)

#a da olup b olmayan ve a da olup b de olan
a=["polat","adem","melisa","nesrin"]
b=["polat","kubilay","ömer","nesrin"]

kesisim =[i for i in a if(i in a and i in b)]

fark =[i for i in a if(i in a and i not in b)]

print(kesisim,fark)
#yukarıda ki örnegin benzeri kısa yolu
x={"python","java","perl","scala"}

y={"ruby","pyhton","java","php"}

fark=x-y

birlesim=x|y

kesisim= x&y

simetrik_fark=x^y

x=[1,2,3]
y=["a","b","c"]
#demet
z=list(zip(x,y))
print(z)
#key-value
z=dict(zip(y,x))
print(z)