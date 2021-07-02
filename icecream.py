# -*- coding: utf-8 -*-
"""
Created on Mon May 17 11:24:13 2021

@author: Deepak Murugesan
"""
import random;
customer = ['deepak']
winner = random.choice(customer)
flavor = 'vannila'
print('Congratulations'+winner+'you have won an icream sundae!!! ')
prompt='Would you like to add a cherry on top??'
wants_cherry = input(prompt)
order = flavor + ' sundae '
if (wants_cherry == 'yes'):
 order = order + ' with a cherry on top'
 
print('One ' + order + ' for ' + winner + 
 ' coming right up...')