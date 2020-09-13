p=int(input("Poids d'Haruhi :"))
q=int(input("Quantité de nourriture mangée par Haruhi :"))
n=int(input("nombre d'animaux :"))
caract=[[187000,15000],
[200,900],
[4200,100],
[2334,33444],
[2247,55677]]
ratioH=q/p
total=0
for i in range(n):
    ratioA=caract[i][1]/caract[i][0]
    if ratioA>ratioH:
        total+=1
        
print(total)