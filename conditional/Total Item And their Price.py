# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 20:39:31 2019

@author: KM SONI
"""

n=int(input('Enter Total Number of Item Purchased :'))
P1= 120
P2= 100
P3= 70
if 0<n<10:
    P1 *= n
    print('Price of{0:5d} items is:{1:5d}'.format(n,P1))
elif 10<=n<100:
    P2 *=n
    print('Price of{0:5d} items is:{1:5d}'.format(n,P2))
elif 100<=n:
    P3 *=n
    print('Price of{0:5d} items is:{1:5d}'.format(n,P3))

