# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import datetime
now=datetime.datetime.now()
dtm=str(now)
item='Amul Butter 100gms'
price = 45
qty= 4
val = price * qty
tax= val*0.05
net =val+tax
print('-'*65)
print('\t\t\t\tINVOICE')
print('-'*65)
print()
print('date:{0:>55s}'.format(dtm))
print('-'*65)
print('ITEM\t\t\tUnit Price\tQuantity\tValue')
print('-'*65)
print('{0:<25s}'.format(item),end=' ')
print('{0:>7.2f}'.format(price),end=' ')
print('{0:>10d}'.format(qty),end=' ')
print('{0:>14.2f}'.format(val))
print('Tax:{0:>57.2f}'.format(tax))
print('-'*65)
print('Amount Payable:{0:>46.2f}'.format(net))