"""
#ex 1 

nb = input("Veuillez saisir un nombre\n")
print(nb)
nb=int(nb)
#ex2
liste_1 = []
for i in range(nb):
    n =int(input("Saisissez un nombre\n"))
    liste_1.append(n)
print(liste_1)   
print(min(liste_1))
print(max(liste_1))


#ex 4
prenom = input("Entrez votre prénom\n")
nom = input("Entrez votre nom\n")
date =  input("Entrez votre date de naissance\n")

print("Voici ce que vous avez rentré\n")
print("Nom\n", nom)
print("Prénom\n", prenom)
print("Date de naissance\n", date)


#ex5
var_liste = input("Saisir numérateur et dénominateur:\n").split()
num=int(var_liste[0])
denom=int(var_liste[1])
if denom != 0 : 
    print(num,'/',denom ,'=' ,num/denom)
else:
    print("division impossible")



#ex 6
heure, minute = int(input("Entrez une heure")),int(input("Entrez des minutes"))
if heure<0 | heure>23 :
    print("Erreur de la saisie")
else : 
    minute += 1
    if minute>59:
        minute = 00
        heure += 1
        if heure>23:
            heure=00
print("Il est",heure,':',minute)

#ex 7
j,m,a=int(input("Entrez un jour\n")),int(input("Entrez un mois\n")),int(input("Entrez une année\n"))
if (m==1) | (m==3) | (m==5) | (m==7) | (m==8) | (m==10) | (m==12):
    if (1<=j<=31):
        print("Nous sommes le",j,'/',m,'/',a)
        j += 1
        if j>31 :
            j=1
            m += 1
            if m>12:
                m=1
                a += 1
        print("Demain nous serons le",j,'/',m,'/',a)
    else:
        print("Jour inexistant")
elif (m==4) | (m==6) | (m==9) | (m==11):
    if 1<=j<=30:
        print("Nous sommes le",j,'/',m,'/',a)
        j += 1
        if j>30:
            j=1
            m+=1
        print("Demain nous serons le",j,'/',m,'/',a)
elif m==2:
    if (a%4==0 & a%100!=0) | (a%4==0): #bissextile
        if 1<=j<=29 :
          print("Nous sommes le",j,'/',m,'/',a)
          j+=1
          if j>29:
              j=1
              m +=1
          print("Demain nous serons le",j,'/',m,'/',a)             
        else:
            print("Jour inexistant")
    else : 
        if 1<=j<=28:
            print("Nous sommes le",j,'/',m,'/',a)
            j+=1
            if j>28:
                j=1
                m+=1
            print("Demain nous serons le",j,'/',m,'/',a)
        else:
            print("Jour inexistant")
#ex 8
choix = int(input("Choisir une méthode\n"))

def pgcd(n1,n2):
    while n2!=0:
        r=n1%n2
        n1=n2
        n2=r
    return n1

def eq2D(a,b,c):
    d=b*b-4*a*c
    if (d>0) :
        x1 = (-b-d**(0.5) )/2*a
        x2 = (-b+d**(0.5) )/2*a
        print("x1 = ",x1)
        print("x2 = ",x2)
    elif d==0:
        x0= -b / 2*a
        print("x0 = ",x0)
    else:
        print("Aucune solutions dans R")

if (choix==1):
    n=int(input("choisir un nombre\n"))
    fact=1
    for i in range(0,n):
        fact*=n-i
    print(n,'! =',fact)

if(choix==2):
    nb1,nb2=int(input("choisir nb1\n")),int(input("choisir nb2\n"))
    res=pgcd(nb1,nb2)
    print("PGCD(",nb1,',',nb2,')=',res)
    
if(choix==3):
    a,b,c=int(input("Coeff a ?\n")),int(input("Coeff b ?\n")),int(input("Coeff c ?\n"))
    resu=eq2D(a,b,c)
"""   
        
    

    

    