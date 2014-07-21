#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 16, 2014

@author: anroco

How to compare two float values in Python?

¿Cómo comparar dos valores float en Python?
'''

#create two float number
f1 = 0.3
f2 = 0.3
print(f1)
print(f2)

#uses the == operator to determine if the value ​​of two
#float number are equals
print(f1 == f2)

#create a float number
f3 = 0.2 + 0.1
print(f3)

#return False because the float numbers are represented in computer hardware
#as binary fractions and some float numbers can’t be represented exactly in
#binary, resulting in small roundoff errors.
#review https://docs.python.org/3/tutorial/floatingpoint.htm
print(f1 == f3)

#the round() function can be useful for rounding so that results with inexact
#values become comparable to one another.
print(round(f1, 2) == round(f3, 2))
