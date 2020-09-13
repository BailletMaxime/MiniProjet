ligne=int(input("Choisir un nombre de ligne : "))
caract="^"
for i in range(ligne):
    esp=""
    for j in range(i,ligne):
        esp+=" "
    sapin=esp+caract
    caract+="^^"
    print(sapin)
    