# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 12:47:24 2019

@author: KM SONI
"""

P=float(input("Enter Principal Amount:"))
R=float(input("Enter Annual Interest Rates:"))
N=int(input("Enter No. of Monthly Installments:"))
MR=R/(12*100)
EMI=(P*MR*(1+MR)**N)/((1+MR)**N-1)
A=EMI*N
I=A-P
print("\n""Principal Amount:",P)
print("Annual Rate of Interest:",R)
print("Monthly Rate of Interest:",MR)
print("No. of Monthly Installments:",N)
print("EMI:",EMI)
print("Amount Payable:",A)
print("Total Interest payable:",I)