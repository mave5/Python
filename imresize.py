# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 11:39:28 2015

@author: Moslem
"""
import numpy as np

a = np.array([[0, 1], [2, 3]], order='C')
a.resize((2, 1))

z=np.zeros((100,100))
print z.shape
z.resize((50,50))
print z.shape


