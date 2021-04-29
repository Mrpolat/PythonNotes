# -*- coding: utf-8 -*-

import os

os.getcwd()


lines=open("dosya.txt","r")

for i in lines:
    print(i) 
    
os.chdir()#dizin

klasorler=os.getcwd()

len(klasorler)

#mkdir dosya olusturur
"""
isfile() #dosyamı

isdir() #directory mi

readable() #okunabilirbmi

writeable() #yazılabilir mi

os.remove() #dosyayı silecek

os.rmdir() #klasörü silecek
"""
#try except else kullanabilirsin
#try except finally kullanabilirsin