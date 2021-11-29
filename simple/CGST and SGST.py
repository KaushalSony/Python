# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 23:06:50 2019

@author: KM SONI
"""

"""SP : Selling Price CGST : Central Govt gst SGST : State Govt Gst"""
Item = input("Enter Item Name :")
SP = float (input("Enter Selling Price of Item" + Item + ":"))
GstRate = float (input("Enter GST Rate(%) :"))
CGST =SP*((GstRate/2)/100)
SGST = CGST
Amount =SP+CGST+SGST #Consumer will buy at this Price
print ("\' INVOICE \'")
print ("Price :" ,SP)
print ("CGST(@",(GstRate/2),"%) :" ,CGST)
print ("SGST(@",(GstRate/2),"%) :" ,SGST)
print ("Amount Payable :" ,Amount)
