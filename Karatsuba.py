# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 18:20:06 2018

@author: louis
"""



def Karatsuba(x,y):
    
    if x<10 or y<10:
        return x*y   
    
    else:
        prior_n = max(len(str(x)), len(str(y)))
        prior_n = int(prior_n)
        n = prior_n//2
    
        a = x//(10**n)
        b = x%(10**n)
        c = y//(10**n)
        d = y%(10**n)
        
        ac = Karatsuba(a,c)
        bd = Karatsuba(b,d)
        ad_bc = Karatsuba(a+b,c+d)-ac-bd        
        
        if prior_n%2 == 0: 
            result = (10**prior_n)*ac+(10**n)*ad_bc+bd
        else:
            result = (10**(prior_n-1))*ac+(10**n)*ad_bc+bd
             
        return result
    
x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627

print(Karatsuba(x,y))
