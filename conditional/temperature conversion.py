# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 16:06:42 2019

@author: KM SONI
"""
t=float(input('Enter Temperature (in Celcius/farenheit/kelvin): '))
print('1. conversion of celcius temperature into Farenheit and kelvin')
print('2. conversion of Farenheit temperature into celcius and kelvin')
print('3. conversion of kelvin temperature into Farenheit and celcius')
n=int(input('Enter Your Temperature Choice(1 or 2 or 3) :'))
if n==1:
    c=t
    f=(9*t/5)+32
    k=t+273.15
elif n==2:
    f=t
    c=((t-32)*5)/9
    k=c+273.15
elif n==3:
    c=t-273.15
    f=(9*c/5)+32
    k=t
print('Temperature in Celcius :',c)
print('Temperature in Farenheit :',f)
print('Temperature in Kelvin :',k)