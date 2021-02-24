import random
import math 
"""
def Quadrillage(nb_points):
    Aire=0
    for i in range(n):
        x=random.random()
        y=random.random()
        if(math.sqrt( x**2 + y**2)<=1): #rayon = 1
            Aire += 1
    pi = Aire
    pi= pi/nb_points
    pi=pi*4
    return pi

n=int(input("Entrez un nombre de points\n"))
pi=Quadrillage(n)
print("PI ~",pi)

def Madhava(k):
    somme=0
    for i in range(0,k,1):
        somme += (((-1)**k)/(2*k+1))
    pi=4*somme
    return pi
n=int(input("Entrez un nombre d'itérations\n"))
pi=Madhava(n)
print("PI ~",pi)

def Wallis(k):
    produit=1
    for i in range(1,k,1):
        produit *= ((2*k)**2) / ((2*k)**2 - 1)
    pi = 2*produit
    return pi
    
n=int(input("Entrez un nombre d'itérations\n"))
pi=Wallis(n)
print("PI ~",pi)


def Newton(n):
    if(n==0):
        return 1
    else:
        return ((Newton(n-1)/2) + (1/Newton(n-1)))

n=int(input("Entrez n\n"))
sqrt2=Newton(n)
print("sqrt(2) ~",sqrt2)
"""