# -*- coding: utf-8 -*-

import time
import random
import math
import locale

t1 = time.time()
t1 =t1+60*60

t2 =time.gmtime(t1)
print(t2)

for i in range(5):
    print(i)
    time.sleep(0.5)
    
print(random.random)

a=5
b=10

x=a+(int)(b-a*random.random())

print(x)

x=[1,2,3,'a','b']

print(random.choice(x))
print(random.sample(x,2))
random.shuffle(x)
print(x)

x="Python programlama dili"

for i in x:
    print(i)
    
print(x[4])
print(x[2:10])
print(x[2:])
print(x[:10])
print(x[0::2])
print(x[::-1])

x.strip(' ')

x.replace(',',' ')

x.upper()

x.lower()

a=x.split(' ')

print(a)

':'.join(a)

print(a)

math.pow(4,3)

min(3,4,5)
math.ceil(2.01)
math.floor(2.01)
math.sqrt(64)
math.pi

z=time.strftime("%B")
print(z)

locale.setlocale(locale.LC_ALL, "tr_TR")
t=time.strftime("%B")
print(t)

a=int(input())
b=int(input())
print(a+b)
