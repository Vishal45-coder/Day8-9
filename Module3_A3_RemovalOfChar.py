# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 19:13:54 2020

@author: vishal
"""

str = "Engineering"
   
 
print ("Original string: " + str) 
   
 
res_str = str.replace('e', '') 
   
 
# removes all occurrences of 'e' 
print ("The string after removal of character: " + res_str) 
   
# Removing 1st occurrence of e 
 
res_str = str.replace('e', '', 1) 
    
print ("The string after removal of character: " + res_str) 
