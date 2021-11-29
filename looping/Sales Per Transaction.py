# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 20:54:45 2019

@author: KM SONI
"""

TT = 0
TS = 0
count = 1
while count<=7:
    T=int(input('Transactions Made on Day'+str(count)+':'))
    S=int(input('Items Sold on Day'+str(count)+':'))
    TT +=T
    TS += S
    count += 1
AS = TS/TT
print('\n')
print('Total Sales Made :',TS)
print('Total Transactions Made :',TT)
print('Average Sales per Transaction :',AS)