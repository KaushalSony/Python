# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 12:47:24 2019

@author: KM SONI
"""

P=float(input("Enter Principal Amount:"))
r=float(input("Enter Monthly Interest Rates:"))
N=int(input("Enter No. of Monthly Installments:"))
R=r/100
EMI=(P*R*(1+R)**N)/((1+R)**N-1)
A=EMI*N
I=A-P
print("\n""Principal Amount:",P)
print("Monthly Rate of Interest:",R)
print("No. of Monthly Installments:",N)
print("EMI:",EMI)
print("Amount Payable:",A)
print("Total Interest payable:",I)