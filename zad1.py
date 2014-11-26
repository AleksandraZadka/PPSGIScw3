'''
Created on 5 lis 2014

@author: Alex
'''
#!/usr/bin/env python
#-*- coding: utf-8 -*-

pliczek=open("przyklad.txt",'r')
statystyki = {}
for slowo in pliczek.read().split():
    if slowo not in statystyki:
        statystyki[slowo] = 1
    else:
        statystyki[slowo] += 1   
statistic = open("statystyki.txt", 'a')
for s, l in statystyki.items():
    print s, ":", l
statistic.write(str(statystyki))
pliczek.close()
statistic.close()    
    