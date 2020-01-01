# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 17:34:31 2018

@author: munsh
"""

import pprint
import scipy
import scipy.linalg   # SciPy Linear Algebra Library

A = scipy.array([ [25, 5, 1], [64, 8, 1], [144, 12, 1] ])
P, L, U = scipy.linalg.lu(A)

print("A:")
pprint.pprint(A)

print("P:")
pprint.pprint(P)

print("L:")
pprint.pprint(L)

print("U:")
pprint.pprint(U)