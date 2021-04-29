# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 03:59:19 2021

@author: 90530
"""


for i in range(1,10):
    if i % 2==0:
        continue
    elif i%5==0:
        break
    else:
        print(i)
    
asal=True
x=17

for i in range(3,x):
    if x%i==0:
        asal=False
        break
print(x,'asaldir') if asal else print(x,"asal değildir")

x=18

for i in range(3,x):
    if x%i==0:
        print(x,"asal değildir")
        break
else:
    print(x,"asaldir")
    
    
x=17
i=2
while i<x:
    if x%i==0:
        print(x,"asal değil")
        break
    i+=1
else:
    print(x,"asaldir")
    
    
def topla(a,b):
    return a+b
print(topla(8,4))

def topla(a=3,b=5):
    return a+b
print(topla(5))

class Matematik:
    def __init__(self):
        self.pi =3.14
    
    def alan_hesapla(self,r=0):
        return self.pi*(r**2)
    def cevre_hesapla(self,r=0):
        return self.pi*2*r
    
daire=Matematik() 

print (daire.alan_hesapla(4))

print (daire.cevre_hesapla(4))