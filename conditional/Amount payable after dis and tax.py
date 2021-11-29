# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
S=float(input('Enter Sales Amount:'))
if S<=20000:
    disrate=10
else:
    disrate=17.5
dis=S*disrate/100
P= S-dis
StaxRate=float(input('Enter Sales Taxrate(5-12%):'))
Stax=P*StaxRate/100
Net= P + Stax
print('Actual Amount:',S)
print('Discount Offered @',disrate,'%:',dis)
print('Applicable Sales Tax @',StaxRate,'%:',Stax)
print('Net Payable Amount:',Net)