poules = int(input("Poules tuées : "))
chiens = int(input("Chiens tués : "))
vaches = int(input("Vaches tuées : "))
amis = int(input("Amis tués : "))

def amende(poules,chiens,vaches,amis) :
    points= poules + 3*chiens + 5*vaches + 10*amis
    print("Vous avez perdu ",points,"points")
    if points>=100:
        print("Vous n'avez plus de points sur votre permis")
    permis = points/100
    return 200*permis

somme= amende(poules, chiens, vaches, amis)

if somme == 0:
    print("rien à payer")
else :
    print("Somme à débourser : ",somme, "euros")