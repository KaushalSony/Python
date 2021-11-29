# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 12:24:24 2019

@author: KM SONI
"""

Name=input("Enter Name Of Item:")
Price=float(input("Enter Selling Price Of Item:"))
Qty=int(input("Enter Quantity Of Item:"))
dis=float(input("Enter Discount(%):"))
Dis=Price*(dis/100)
Amount=(Price - Dis)*Qty
print("Item Name:",Name)
print("Selling Price:",Price)
print("Quantity:",Qty)
print("Discount(%):",dis)
print("Amount Payable:",Amount)
