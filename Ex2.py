from random import*
N=randint(1,100)

essai=0
prop=""

while N!=prop:
    essai=essai+1
    prop=int(input("choisissez un nombre entre 1 et 100: "))
    if prop>N:
        print("Plus petit")
    if prop<N:
        print("Plus grand")
    if prop==N:
        print("Vous avez trouvez ",N," en ",essai," coups")
    
    