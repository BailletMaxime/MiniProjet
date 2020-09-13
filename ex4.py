prixHT = float(input("Prix HT (entrez 0 pour terminer) : "))
prixTTC= prixHT*1.196
while prixHT > 0:
    print("Prix TTC : ",prixTTC," €")
    prixHT = float(input("Prix HT (entrez 0 pour terminer) : "))

print("programme terminé")
