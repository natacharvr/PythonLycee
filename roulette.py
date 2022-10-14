from math import ceil
from random import randrange

somme_finale = 1000
continuer_partie = True

print("Bienvenue au casino. Vous vous trouvez à la table de la roulette. Les règles sont simples, vous pariez la somme que vous souhaitez sur le nombre de la table de votre choix. Je lance la bille sur la roulette et fait tourner la roulette. SI la bille s'arrête sur le nombre que vous avez choisi, vous remportez trois fois la somme pariée. Autrement, si les deux nombres sont de même couleur (les nombres pairs sont noirs et les nombres impairs sont rouges.), vous remportez la moitié de votre mise. Sinon, vous perdez votre mise. Vous commencez la partie de roulette avec 1000 $")

while continuer_partie==True:
	pari=-1#on défini une valeur qui ne rentre pas dans les conditions nécéssaires à la continuation du jeu
	while pari < 0 or pari > 49: #conditions pour que le jeu continue

		pari = input("Sur quel numéro voulez-vous parier? La roulette va de 0 à 49 :")
		try:#on évite que le jeu plante à cause d'erreurs de la valeur saisie par l'utiliateur
		    pari = int(pari)

		except ValueError:
			print("Saisissez un nombre seul, les caractères ne sont pas compris")
			pari = -1 #on remet pari à -1 pour que la demande de la ligne 14 revienne
			continue #on retourne au while
		if pari < 0 or pari > 49:
			print("Le numéro choisi n'est pas contenu sur la roulette")#on explique à l'utilisateur pourquoi le programme lui redemande une valeur

	somme = -1
	while somme<=0 or somme>somme_finale:

		somme = input("Saisissez la somme que vous souhaitez parier : ")
		try:
		    somme = int(somme)
		except ValueError:
			print("Saisissez un nombre seul, les caractères ne sont pas compris")
			somme = -1
			continue
		except TypeError:
			print("saisissez un nombre entier")
			somme=-1
			continue

		if somme > somme_finale:
			print("vous n'avez pas assez d'argent")

		if somme< 0:
			print("Vous ne pouvez pas parier un nombre négatif d'argent, ni rien du tout")

	if pari%2==0:
	    pair = 'noirs'
	else:
	    pair = 'rouges'

	print("Je lance la roue")
	print("Je lance la bille")
	b = randrange(50) #on définit la valeur prise aléatoirement par la bille sur la roulette

	print("La bille s'est arrêtée sur le numéro", b)

	if b==pari:
	    somme_finale = somme_finale + 36*somme
	    print("Vous avez gagné, vous aviez parié", somme, "$. Vous avez désormais", somme_finale, "$")

	elif (pari%2 == 0 and b%2==0) or (pari%2!=0 and b%2!=0):
	    somme_finale = somme_finale + ceil(somme/2)
	    print("Le numéro que vous avez choisi et le numéro sur lequel s'est arrêté la roulette sont tous deux", pair, "Par conséquent vous gagnez la moitié de la somme que vous avez parié. Vous aviez parié ", somme, "$. Vous avez désormais ", somme_finale, "$")

	else:
	    somme_finale = somme_finale - somme
	    print("Vous avez perdu vous avez désormais", somme_finale, "$")

	if somme_finale == 0:
		print("Désolé, vous êtes ruiné, Au revoir")
		continuer_partie = False # on interrompt le jeu si le joueur n'a plus d'argent en invalidant la condition de la boucle
	else:
		quitter = input("Voulez-vous quitter le casino avec vos gains ? o/n ")
		if quitter == "O" or quitter == "o":
			print("Vous quittez le casino avec ",somme_finale,"$")
			continuer_partie = False
input("appuyez sur entrée pour quitter")