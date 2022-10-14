                CHAPTRE 2
un objet est une structure de données, comme les variables, qui peut contenir elle-même d'autres variables et fonctions
En Python, tout est objet

Tous les objets sont issus d'une classe, une classe est une forme de type de donnée. Chaque type de donnée a ses fonctions 
définies dans son type. Donc chaque type de variable contient des fonctions comme un module contient des données.
Par exemple le type chaine str contient la fonction lower qui met une chaine en minuscule. On y fait appel en l'appelant 
chaine.lower() sans variable dans les parenthèses. (chaine est une variable définie)
Ces fonctions définies dans les classes sont appelées des méthodes
lower met en minuscule, upper met en majuscule, upper met la première lettre en majuscule, stip retire les espaces en début 
et fin de chaine, la fonction center(nb) centrera la chaine au milieu d'espaces. Nb défini la longueur finale de la chaine.
La fonction lower permet notament de rentrer les condtions (genre quitter ? o/n) en minuscule si l'utilisateur les saisit en
majuscule

On peut associer un type à une variable ex: chaine = str()
On peut associer deux méthodes à la suite. Ex chaine.upper().center

On peut modifier et enregistrer une chaine en utilisant la fonction format
exemple "Je m'appelle {0} {1} et j'ai {2} ans".format(prenom, nom, age)
il faut alors définir les variables utilisées par format
IMPORTANT Python commence à compter à partir de 0
Si les variables sont citées dans le bon ordre on peut ne pas mettre les numéros dans les accolades. Dans notre exemple cela 
aurait fonctionné ainsi: "Je m'appelle {} {} et j'ai {} ans".format(prenom, nom, age)
On peut aussi nommer les variables entre accolades
ici : "Je m'appelle {prenom} {nom} et j'ai {age} ans".format(prenom, nom, age)

On peut mettre bout à bout deux chaines (c'est appelé concaténer) avec l'addition
chain_complete = chaine1 + chaine2
et pour insérer un espace entre les deux
chaine_complète = chaine1 + " " + chaine2

Avant de concaténer un nombre et une chaine il faut changer le nombre en str (chaine + str(21) par exemple)

Pour accéder à un caractère d'une chaine il faut préciser sa position entre crochets après le nom de la chaine (commence à 0)
ex : chaine = 'Jour'
chaine[0]
'J'

On peut aussi compter depuis la fin avec un indice négatif
ici chaine[-1]
'r'

La fonction len(chaine) permet de connaître la longueur de la chaine
ici len(chaine) == 4

Pour sélectionner des caractères on utilise chaine[nb:NB] avec nb et NB des indices de position et nb et NB ne sont pas 
obligés d'être écrits pour indiquer 0 ou len(chaine) il comprend que chaine[:] sélectionne tout
Je sais pas trop quand c'est compris ou non



LES LISTES
Les listes sont des objets contenant d'autres objets pouvant être de tous types
elles s'appellent list et se notent entre crochets
les différents objets sont séparés par des virgules
exemple liste = [1,2,3,'b']

On accède aux éléments de la liste de la même manières qu'aux caractères d'une chaine mais contrairement à eux on peut les 
remplacer grâce à la syntaxe:
liste[2] = 'R'
dans ce cas ma liste sera
[1,2,'R','b']

La méthode append() de list permet de rajouter un objet à la fin de la liste

IMPORTANT pour les chaines, les méthodes comme upper ne modifient pas l'objet, elles en renvoient un autre, pour les listes 
c'est l'inverse elles modifient directement l'objet sans renvoyer la liste

On ajoute un objet avec insert()
Dans les parenthèses on met la position où l'on veut mettre l'objet, virgule l'objet
ex: liste.insert(2, 3) donnera [1,2,3,'R','b']

Pour concaténer deux liste il existe 3 façons
la même que pour les chaines avec +
la méthode extend() ex liste1.extend(liste2)
et liste1 += liste2
Ces deux dernières méthodes associent la liste finale à liste1 tandis que la première ne fait que l'afficher

le mot clé del permet de supprimer par exemple une variable
si je défini une variable a = 2 et qu''ensuite je note del a cette variable est simplement supprimée

Dans le contexte des listes, l'utilisation de del est très simple
liste = [1,2,3]
del liste[1]
liste
[1,3]

Une autre façon de faire existe avec la méthode remove(). Elle prend en charge directement l'élément et pas son indice de 
position dans la liste [1,2,3,1]
liste.remove(1)
liste
[2,3,1]
Attention, cette méthode ne supprime que la première occurence de la variable

la fonction enumerate() permet de parcourir une liste en notant
for indice, élément/elt in enumerate(liste):
    print("a la {}eme place se trouve {}".format(indice, elt))
Cette notation peut être simplifiée ainsi for elt in enumerate(liste):
Ainsi, le tuple associant l'indice et l'élément de la liste sont tous deux associés à la variable elt

On peut aussi noter list(enumerate(liste)) mais les valeurs avec leur indice apparraissent toutes sur une ligne dans des 
tuples. Sur cette dernière notation, on peut attribuer un départ de numérotation différent de 0. Cela en notant
list(enumerate(liste, start= X))


Un tuple est l'équivalent d'une liste mais une fois défini, il n'est plus modifiable. La syntaxe est la même que pour une 
liste mais à la place des crochetson met des parenthèses.
Pour créer un tuple avec une seule valeur il faut tout de même mettre une virgule après la valeur pour que Python comprenne
On peut affecter plusieurs variables d'un coup ex a, b = 3, 4
qui en fait représente deux tuples (a, b) = (3, 4)

On peut définir des fonctions qui renvoient plusieurs valeurs. Comme par exemple le reste et la partie entière d'une division.
l''instruction return partieEntière, reste créera un tuple de valeurs.

La méthode split() des chaines permet de convertir la chaine en liste en donnant à split le caractère qui est utilisé comme
délimiteur des différents objets qui seront contenus dans la chaine.
ex chaine = Bonjour à toi!
chaine.split("à")
['Bonjour ',' toi!']
Le symbole qui a été utilisé est effacé de la liste.

Pour transformer une liste en chaine on utilise la méthode join.
our cette méthode, on écrit la chaine qui est insérée entre chaque objet de la liste ( souvent un espace pour une phrase) 
suivie de .join(liste)
ex liste = ["Je", "m'appellle", "Natacha"]
" ".join(liste)
"Je m'appelle Natacha"

On peut utiliser ces transformations pour afficher des flottants plus symplement par exemple
>>> def flottant(x):
...     x=str(x)
...     (entier, reste) = x.split(".")
...     return ",".join([entier, reste[:3]]) #on affiche la liste en ne prenant que les 3 premiers décimaux

On peut créer des fonctions dont on ne connait pas le nombre de variables à l'avance. Elle s'écrit
def f(*paramètres)
ainsi, quand on fait appel à la fonction, tout ce qui est inséré dans les parenthèses est inséré dans un tuple. Libre à nous 
d'en faire ce que l'on souhaite.
On peut aussi créer une fonction avec des paramètres qui doivent être fourni puis un fourre tout.
exemple def f(nom, prenom, *autres)

ATTENTION COMPLIQUÉ
>>> def afficher(*variables, sep = ' ', fin='\n'):#on veut afficher toutes les variables capturées avec la séparation' '
...     variables = list(variables)#on transforme le tuple contenant les variables en liste pour pouvoir le modifier
...     for i, elt in enumerate(variables):#on énumère les objets
...         variables[i]= str(elt)#chaque objet de la liste est remplacé par lui même mais en chaine de caractère 
#( 2 devient '2'
...     chaine = sep.join(variables)#on crée une chaine avec toutes les chaines contenues dans la liste chacune séparée 
#des autres par sep qui est un espace
...     chaine += fin# on ajoute seulement '\n' qui a été défini dans afficher à la fin de la chaine
...     print(chaine, end = '')#on imprime la chaine toute préparée avec rien à la fin

On peut donner à une fonction comme paramètre une liste ou un tuple déjà définie
cela en nottant f(*liste)
exemple
liste = [1,2,3]
print(*liste)
1 2 3

écrire a**2 signifie mettre au carré

On peut appliquer une instruction à chaque élément d'une liste pour en créer une nouvelle
exemple avec la liste ci dessus
[nb**2 for nb in list]
ce qui donne [1,4,9]
On peut aussi la filtrer en mettant une condition à l'affichage
[nb for nb in liste if nb%2==0]#on affiche le nombre de la liste s'il est pair
ce qui donne [2]
On peut mélanger les deux méthodes en appliquant une instruction sur chaque objet et en mettant une condition à leur apparence
ex fruits = [4,7,2,9]
print([nb-6 for nb in fruits if nb>6])

LES DICTIONNAIRES
les dictionnaires dont des onjets qui en contiennent d'autre un peu comme une liste
mais chaque objet contenu est associé à un mot clé appelé clé qui peut être de bcp de types qu'il suffir d'entrer pour 
obtenir l'information.
Les carnets d'adresses par exemple sont des dictionnaires

La classe des dictionnaires est dict. La syntaxe est dictionnaire = {}
Les parenthèses délimitent les tuples, les crochets délimitent les listes et les accolades {} délimitent les dictionnaires.

Pour remplir un ditionnaire il y a deux méthodes,
pour la première il faut, d'abord, créer un dico vide
dico = {}
Ensuite entrer la première variable et sa 'valeur'
dico["pseuso"] = "nataccord"
Ainsi de suite pour toutes les variables. Et pour appeler une variable on note
dico["pseudo"]
'nataccord'
Ici, "pseudo" est la clé associée à la valeur "nataccord"
pour la deuxième il faut tout simplement le remplir ainsi
placard = {"chemise":3, "pantalon":6, "tee-shirt":7}
Les mots clés peuvent comporter des espaces
Si on appelle une valeur qui n'existe pas,' une erreur de type KeyError sera levée
Les clés peuvent être des entiers, ainsi pas besoin de ""
On peut utiliser quasiment tous les types comme clés et comme valeurs

Il existe aussi un autre type , les set, qui sont très similaires aux listes sauf qu'ils ne peuvent contenir deux fois une
meme valeur 
Un set est aussi entouré de {}

On peut supprimer une clé grâce à del
del placard["pantalon"]
ou bien grâce à la méthode pop qui en plus de supprimer la clé, renvoie la valeur supprimée
placard.pop("pantalon")
6

On peut stocker des fonctions dans un dictionnaire
dico[print] = print
et on y fait appel 
dico[print]("coucou")
ainsi

On peut parcourir un ditionnaire de la même façon qu'une liste
mais il y a d'autres manières
pour parcourir les clés : for cle in dico.keys()
	print cle

la méthode keys renvoie la liste des clés sur une seule ligne
Pour parcourir les clés et les valeurs on utilise la méthode items de la même façon que enumerate sauf que quand celle ci 
s''écrit enumerate(liste) la méthode items s''écrit dico.items()

On peut faire exactement la même chose avec la méthode values qui renvoie les valeurs au lieu de clés
on peut faire une fonction qui accespte à la fois des paramètres non nommés comme vu plus haut avec une *
def fonction(*paramètresNonNommés)
qu'il faut appeler' fonction(3,4,5)
et les paramètres nommés avec deux**
def fonction(**paramètresNommés)
qu'il faut appeler' fonction(p=2, i=5, y=7)
ainsi : def fonction(*nonNommés, **nommés)
qu'on peut appeler' fonction(3,4,p=2,5,i=5, y=7)

sep est un mot clé qui veut dire qu'il place la valeur associée ex sep ="'" en séparation de chaque valeur
et end place sa valeur associée à la fin de la liste

Comme pourune liste on peut appeler un dictionnaire en tant que paramètres d'une fonction grâce à la syntaxe
dicoParamètres = {"premier paramètre" : 1, "deuxième paramètres" : 2}
f(**dicoParamètres)

Pour ouvrir un fichier, on l'associe à une variable pour pouvoir l'appeller et on utilise la fonction open
Cette fonction prend en paramètre le chemin pour accéder au fichier entre guillemets, puis la façon de l'ouvrir
il y a la foçon 'r' qui est le mode lecture, 'w' qui est pour écrire en écrasant toutes les anciennes données et 
'a' qui écrit la la suite
pourouvrir en binaire? il faut ajouter b à la suite de ces lettres

Pour intéragir avec un fichier texte on utilise les méthodes de sa classe TextIoWrapper
Pour lire un fichier on utilise la méthode read qui affiche l'intégralité du fichier
Pour écrire dans un fichier, on utilise la méthode write en lui mettant en paramètre la chaine de caractères que l'on souhaite 
ajouter/ écrire. (elle renvoie le nb de caractères écrits) Ceci à condition de l'avoir ouvert avec a ou w

Ne pas oublier de fermer les fichier après utilisation
pour cela on utilise la méthode close du fichier sans lui donner de paramètres

On peut enfermer l'utilisation d'un fichier dans un bloc with
with open("fichier.txt",'r') as fichier
	blablabla
Ainsi, si il y a une erreur, le bloc se ferme et ferme le fichier pour éviter qu'il reste ouvert
pour vérifier qu'un fichier est bien fermé on peut appeler la variable nomDuFichier.closed qui vaudra True s'il est fermé

Pour enregistrer des infos dans un fichier il faut importer le module pickle et ouvrir le fichier de sorte de pouvoir écrire 
dedans
Ensuite, il faut convertir le fichier dans la classe Pickler en l'utilisant comme fonction appartenant à pickle
On utilise ensuite la méthode dump à laquelle on passe en paramètre ce que l'on veut enregistrer

import pickle
with open ('fichier', 'wb') as fichier:
	mon_pickler = pickle.Pickler(fichier)
	mon_pickler.dump(liste)

Pour récupérer le fichier, c'est exactement pareil sauf que le fichier est ouvert en lecture seule, la classe s'appelle 
Unpickler et la méthode s'appelle load et ne prend rien en paramètre
import pickle
with open ('fichier', 'rb') as fichier:
	mon_pickler = pickle.Unpickler(fichier)
	a = mon_pickler.load()
Le fichier charge la première information contenue dans le fichier, pour avoir les suivantes il faut réutiliser load.
Il est donc plus simple de ne mettre qu'une information par fichier pour ne pas se tromper

Les fonctions ne peuvent modifier les variables qui sont dans l'espace local dans lequel elles sont appelées. 
Càd que la fonction f ne pourra pas modifier la valeur d'une variable
Seules les méthodes des listes le peuvent car elles modifient directement l'objet
En revanche, si on définit une variable comme étant globale les fonctions peuvent l'influencer.
Par convention on met la définition de la variable globale à la liste juste après def
Exemple
def inc_a():
	global a
	a +=1
Cette fonction ajoutera 1 à a quand elle sera effectuée


Pour utiliser des objet d'un fichier autre que celui dans lequel on est, on utilise le package sys (donc il faut importer sys) et on lui donne le chemin du fichier selon cette syntaxe :
sys.path.append('path/dossier/')
ensuite il suffit d'importer ce que l'on veut à l'intérieur de ce dossier, comme les fonctions contenues dans un script

