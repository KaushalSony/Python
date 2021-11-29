# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 14:52:05 2019

@author: KM SONI
"""

P = int (input("Enter the Principal Amount :" ))
R = int (input ("Enter the Interest Rate :" ))
T = int (input("Enter the Time Period :"))
SI = (P*R*T)/100
Amount1 = P + SI
Amount2 = P*(1+R/100)**T 
CI = Amount2 - P
print("\n")
print ("Principal Amount:" ,P)
print ("Interest Rate:" ,R) 
print ("Time Period:" ,T,"\n") 
print ("Simple Interest :" ,SI)
print ("Amount Payable (after SI) :" ,Amount1,"\n")
print ("Compound Interest :" ,CI)
print ("Amount Payable (after CI) :" ,Amount2)
