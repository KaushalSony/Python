# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 12:15:12 2019

@author: KM SONI
"""

import datetime
s=input('Enter Date')
d,m,y=map(int,s.split('-'))
now=datetime.date(y,m,d)
dtm=str(now)
n=int(input('Enter Total Number of Items:'))
a =0
print('-'*65)
print('\t\t\t\tINVOICE')
print('-'*65)
print()
print('date:{0:>55s}'.format(dtm))
print('-'*65)
print('ITEM\t\t\tUnit Price\tQuantity\tValue')
print('-'*65)
for i in range(1,n+1,1):
    item=input('Enter Name of Item :')
    price=float(input('Enter Price of Item :'))
    qty=int(input('Enter Quantity Required :'))
    val = price * qty
    a += val
    tax= a*0.05
    net =a+tax
    i=1
    for j in range(0,i,1):
       print('{0:<25s}'.format(item),end=' ')
       print('{0:>7.2f}'.format(price),end=' ')
       print('{0:>10d}'.format(qty),end=' ')
       print('{0:>16.2f}'.format(val))
       i +=1
print('Tax:{0:>57.2f}'.format(tax))
print('-'*65)
print('Amount Payable:{0:>46.2f}'.format(net))
