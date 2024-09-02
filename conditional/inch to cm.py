# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

n=int(input('Enter length (in Cm) :'))
i=2.54
if n<=0:
    print('Please Enter a Positive Length')
elif n==1:
    print('Length in Inch {0:5d} is :{1:5f}'.format(n,i))
elif n>1:
    i *= n
    print('Length of{0:5d} Cm in Inch is :{1:5f}'.format(n,i))
