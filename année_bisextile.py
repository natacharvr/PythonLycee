#-*-coding:utf-8-*

#programme testant si une année saisie par l'utilisateur est bissextile ou non

a = False
while a == False:
	annee = input("saisissez une année:")
	try:
		annee = int(annee)
	except ValueError:
		print("vous n'avez pas saisi un nombre entier, le programme n'a pas compris quelle année vous avez saisi")
		continue
	if annee % 400 == 0 or (annee% 4 == 0 and annee % 100 != 0):
		print("l'année saisie est bissextile.")
		a = True
	else:
		print("L'année saisie n'est pas bissextile.")
		a=True
input("appuyez sur entrée pour fermer")

