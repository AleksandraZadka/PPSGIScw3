'''
Created on 5 lis 2014

@author: Alex
'''
# -*- coding: utf-8 -*-
class Torba:
    def __init__(self,szer,dlug,gleb):
        self.szer = szer
        self.dlug = dlug
        self.gleb = gleb
    def get_szer(self):
        return self.__szer
    def set_szer(self):
        self.__szer=szer
    def get_dlug(self):
        return self.__dlug
    def set_dlug(self):
        self.__dlug=dlug
    def get_gleb(self):
        return self.__gleb
    def set_gleb(self):
        self.__gleb=gleb
    def __str__(self):
        return 'Torba ma wymiary:'+str(self.szer)+' x '+str(self.dlug)+' x '+str(self.gleb)+' cm'
    def pojemnosc(self):
        return str(self.szer*self.dlug*self.gleb)+' cm3'
    
class Walizkanakolkach(Torba):
    def __init__(self,szer,dlug,gleb,sredkol):
        Torba.__init__(self,szer,dlug,gleb)
        self.sredkol=sredkol
    def wysokosc(self):
        return 'Walizka ma wysokosc: '+str(self.dlug+self.sredkol)+'cm'

class Torebkadamska(Torba):
    def __init__(self,szer,dlug,gleb,nprzegrodek):
        Torba.__init__(self,szer,dlug,gleb)
        self.nprzegrodek=nprzegrodek
    def zawartosc(self):
        return 'Torebka posiada '+str(self.nprzegrodek)+' kieszeni'

class Kontenerdamski(Walizkanakolkach,Torebkadamska):
    def __init__(self,szer,dlug,gleb,sredkol,nprzegrodek):
        Torba.__init__(self,szer,dlug,gleb)
        Walizkanakolkach.__init__(self,szer,dlug,gleb,sredkol)
        Torebkadamska.__init__(self,szer,dlug,gleb,nprzegrodek)
        
t=Torba(10,20,30)
print t.__str__()
print t.pojemnosc()
w=Walizkanakolkach(10,20,30,5)
print w.wysokosc()    
p=Torebkadamska(10,20,30,6)
print p.zawartosc()    
k=Kontenerdamski(10,30,50,4,2)
print k.pojemnosc()
print k.wysokosc()
print k.zawartosc()