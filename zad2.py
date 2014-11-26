'''
Created on 5 lis 2014

@author: Alex
'''
#!/usr/bin/env python
#-*- coding: utf-8 -*-
from __builtin__ import float
def rachunek(zamowienie):
    menimoje=open("slownik.txt","r")
    for linia in menimoje:
        linia=linia.strip('\n').split(' ')
        for i in xrange(0,len(linia)/2):
            slownik={}
            klucz=linia[2*i]
            wartosci=linia[(2*i)+1]
            wart=float(wartosci)
            print klucz+": "+wartosci
            print wart
            
            cena=0.00
            for linia in menimoje: 
                for klu in zamowienie:
                    if klu in linia:
                        cena+=linia[klu]
                    return cena
        
    



zamowienie=["schabowy","kartoflanka"]
print rachunek(zamowienie)


