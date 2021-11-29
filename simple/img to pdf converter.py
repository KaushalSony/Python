# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 18:45:26 2020

@author: KM SONI
"""

from PIL import Image

image1 = Image.open(r'C:\Users\KM SONI\Downloads\WhatsApp Image 2020-03-03 at 10.52.20 AM.jpeg')
im1 = image1.convert('RGB')
im1.save(r'C:\Users\KM SONI\Desktop\kaushal\study\ip\45612.pdf')
