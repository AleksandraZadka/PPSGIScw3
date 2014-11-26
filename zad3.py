'''
Created on 5 lis 2014

@author: Alex
'''
from math import sqrt

class zespolona:
    def __init__(self,r,u):
        self.r = r
        self.u = u
    def get_r(self):
        return self.__r
    def set_r(self,r):
        self.__r=r
    def get_u(self):
        return self.__u
    def set_u(self,u):
        self.__u=u
    def __str__(self):
        return str(self.r)+' + '+str(self.u)+'i'
    def dodaj(self,r2,u2):
        return str(self.r+r2)+' + '+str(self.u+u2)+'i'
    def odejmij (self,r2,u2):
        return str(self.r-r2)+' + '+str(self.u-u2)+'i'
    def modul(self):
        return sqrt(self.r**2 + self.u**2)
pass  

zesp=zespolona(2,2)
print zesp.modul()
print zesp.dodaj(3,4)
