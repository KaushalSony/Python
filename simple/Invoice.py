# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 12:30:07 2019

@author: KM SONI
"""

Name=input("Enter Name Of Item:")
Price=float(input("Enter Selling Price Of Item:"))
Qty=int(input("Enter Quantity Of Item:"))
dis=float(input("Enter Discount(%):"))
GstRate = float (input("Enter GST Rate(%) :"))
Dis=Price*(dis/100)
CGST =Price*((GstRate/2)/100)*Qty
SGST = CGST
Amount=((Price - Dis)*Qty)+CGST+SGST
print("Item Name:",Name)
print("Selling Price:",Price)
print("Quantity:",Qty)
print("Discount(%):",dis)
print ("CGST(@",(GstRate/2),"%) :" ,CGST)
print ("SGST(@",(GstRate/2),"%) :" ,SGST)
print("Amount Payable:",Amount)
