def AfficheTriangle(n,espace,etoile):
    res=''
    for i in range(1,n+1):
        res=espace*(n-i)+ etoile*(i*2-1)+espace*(n-i)
        print(res)


def TableMultiplication(n):
    for i in range(1,11,1):
        res = n*i
        print(i,"x",n,"=",res)
        
def estAmstrong(n):
    somme=0
    amstrong=n
    while n>0:
        reste= n%10
        chiffre=reste**3
        n//=10
        somme += chiffre
    if(somme == amstrong):
        print("C'est un nombre Amstrong")
    else:
        print("Non ce n'est pas un nombre Armstrong")
    
        
nb=int(input("Entrez un nombre"))
"""AfficheTriangle(nb," ","*")"""
"""TableMultiplication(nb)"""
estAmstrong(nb)

    

