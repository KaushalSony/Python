# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 19:12:40 2019

@author: KM SONI
"""

Days = float(input("input Days:"))*24*3600
Hours =int(input("input Hours:"))*3600
Minutes = int(input("input Minutes:"))*60
Seconds = int(input("input Seconds:"))
Amount = Days + Hours + Minutes + Seconds
print("The Amount of Seconds consumed:",Amount)