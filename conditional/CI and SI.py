# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 10:17:30 2019

@author: KM SONI
"""

P = float (input("Enter the Principal Amount :" ))
R = float (input ("Enter the Interest Rate :" ))
T = int (input("Enter the Time Period(in Years) :"))
print('1. Calculate Simple Interest')
print('2. Calculate Compound Interest')
C = int(input('Enter Your Choice(1 or 2) :'))
if C == 1:
    I =(P*R*T)/100
    A = P+I
    print('\n')
    print ("Principal Amount:" ,P)
    print ("Interest Rate:" ,R) 
    print ("Time Period:" ,T,"\n") 
    print('Simple Interest:{0:16.2f}'.format(I))
    print('Amount  After Interest:{0:12.2f}'.format(A))
else:
    N=int(input('Number of times interest is Compounded in a Year:'))
    R /= 100
    p = T*N
    A = P*(1+R/N)**p
    I = A - P
    print ("Principal Amount:" ,P)
    print ("Interest Rate:" ,R) 
    print ("Time Period:" ,T,"\n") 
    print('Compound Interest:{0:16.2f}'.format(I))
    print('Amount  After Interest:{0:12.2f}'.format(A))