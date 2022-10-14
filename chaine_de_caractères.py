chaine = input("entrez un texte: ")
for lettre in chaine:
    if lettre not in "AEIOUYaeiouyàéÉÀèÈâäÂÄêÊËöÖïÏüÜûÛùÙ":
        print(lettre)
    else:
        print(".")

input("appuyez sur entrée pour fermer")