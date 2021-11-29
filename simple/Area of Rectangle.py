# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 22:58:26 2019

@author: KM SONI
"""

# To input length and breadth of a rectangle and calculate its area
Length = float (input("Enter length of the rectangle :"))
Breadth = float (input("Enter breadth of the rectangle :"))
Perimeter = 2*(Length+Breadth)
Area = Length * Breadth
print ("Rectangle Specifications")
print ("Length :",Length ,end='')
print ("Breadth :",Breadth ,)
print ("Perimeter :" ,Perimeter)
print ("Area :" ,Area)