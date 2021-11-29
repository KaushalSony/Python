# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:24:38 2019

@author: KM SONI
"""

P=float(input("Enter Principal Amount:"))
R=float(input("Enter Annual Interest Rates:"))
T=int(input("Enter No. of years:"))
N= T*12
MR=R/(12*100)
EMI=(P*MR*(1+MR)**N)/((1+MR)**N-1)
A=EMI*N
I=A-P
print("\n""Principal Amount:",P)
print("Annual Rate of Interest:",R)
print("Monthly Rate of Interest:",MR)
print("No. of years:",T)
print("No. of Monthly Installments:",N)
print("EMI:",EMI)
print("Amount Payable:",A)
print("Total Interest payable:",I)