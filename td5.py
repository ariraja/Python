
"""
import numpy as np
tab = np.array([1,2,3,4,5,6,7,8,9,10])
#inverser tableau
t_i = tab[::-1]
print(t_i)


#somme
liste_1=[1,2,3,4,5,6,7,8,9,10]
liste_2=[4,8,11,1,0,3,7,20,7,10]

def somme(t1,t2):
    l3=[]
    for i in range(len(t1)):
        l3.append(t1[i]+t2[i])
    return l3

liste_3=somme(liste_1,liste_2)
print(liste_3)
"""


v1=(1,2,3)
v2=(5,6,7)
"""
#produit scalaire
def ProdSca(t1,t2):
    PS=0
    for i in range(len(t1)):
        PS += t1[i]*t2[i]
    return PS

produit_scalaire = ProdSca(v1, v2)
print("v1 . v2 =",produit_scalaire)
"""
#produit vectoriel
def ProdVect(v1,v2):
    v3=[]
    for i in [1,2,0]:
        if(i+1>=len(v1)):
            k=0
        else:
            k=i+1
        a=v1[i]
        b=v1[k]
        c=v2[i]
        d=v2[k]
        v3.append((a*d)-(b*c))
        v3.reverse()
    return tuple(v3)

v3=ProdVect(v1, v2)
print("v1 ^ v2 =",v3)    