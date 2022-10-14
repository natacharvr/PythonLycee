            CHAPITRE 1:

le modulo écrit % permet de connaitre le reste d'une division (exemple 10%2=0)
Pour obtenir la partie entière de la division on note // (exemple 10//2=5)

les nombres entiers sont appelés int pour integer en anglais
les nombres décimaux sont appelés float (ne pas oublier que les virgules sont des points)
les chainess de caractères sont des phrases stockées entre apostrophes ou guillemets 'coucou' elles sont appelées str raccourcis de strings

pour éviter que les apostrophes en milieu de message soient considérées comme la fin, on "échappe" les apostrophes en mettant un anti-slash avant exemple 'j\'aime le chocolat'
pour noter sur plusieurs lignes en faisant entrée, encadrer de triple guillemets

pour augmenter la valeur d'une variable (ou quelque opération) on peut écrire au lieu de a = a + 1
a += 1

on peut permuter la valeur de deux variables en écrivant a,b = b,a

le symbole anti-slash permet aussi d'indiquer que l'instruction continue sur la ligne suivante

pour obtenir le type d'une donnée a taper type(a)

pour afficher une donnée utiliser la fonction print() et pour afficher plusieurs données, les séparer dans les parenthèses par une virgule

pour écrire supérieur ou égal >= ; égal à == ; différent de != Attention, pour comparer l'égalité, utiliser == plutot que = qui correspond à l'affectation de valeur

les conditions : if (si) elif (sinon si) else (sinon)
il faut mettre deux points : après un if/elif/else

on peut affecter True ou False à une variable. Ne pas oublier la majuscule
Pour poser plusieurs conditions, écrire if nanana and nanana:

le mot is compare deux valeurs
le mot not inverse le symbole exemple not a==5 équivaut à a != 5

Pour demander une variable à l'utilisateur, utiliser la fontion input() SAUF que le résultat sera une chaine de caractère, donc utiliser le type de le réponse attendu, par exemple un entier, int() comme fonction pour le transformer. Voir lignes 1&2 du programme année bissextile

Pour tester si un nombre est le multiple d'un autre utiliser le modulo %

on peut utiliser les parenthèses pour mettre deux conditions ensemble

on peut utiliser and et or

l'instruction while (tant que) permet defaire des boucles

On peut parcourir une séquence grâce à la syntaxe
for element in sequence:
Python crée tout seul la variable element en y mettant l premier élément de la chaine sequence
break permet de stopper une boucle infinie
par exemple quand la condition est toujours vraie (while 1)
continue permet de faire recommencer la boucle au début en sautant les dernières lignes de cette boucle

On peut définir une valeur par défaut des variables appliquées à une fonction si l'utilisateur  ne la saisit pas ex: f(a,b=2)

on peut aider l'utilisateur sur l'utilisation de la fonction en entrant un message entre triple guillemets juste après les : de définition avec le meme alinéa. On peut afficher ce message en tapant help(fonction)

Pour définir la valeur des variables d'une fonction on peut les appeler par leur nom. exemple avec f(a=1,b=2,c=3)
f(b=6) donnera a=1 b=6 c=3

La fonction return permet de renvoyer la valeur obtenue par une fonction et d'ensuite la stocker dans une variable. Si une fonction f return une valeur je peux faire une variable a = f(2)

pour une seule instruction on peut utiliser les fonctions lambdas, qui s'écrivent ainsi :
lamba x,y: instruction
cela simplifie la fonction. Pour y faire appel il faut l'associer à une variable
f= lamba x,y :...

On peut créer des modules. Pour cela, entrer plusieurs fonctions ayant un lien dans un fichier. Dans un autre fichier on peut faire appel
à ces fonctions à conditions que les deux fichiers soient contenus dans le même dossier. Il suffit d'utiliser le mot clé import.
On peut aussi ranger les modules dans des dossiers appelés packages. De même il suffit d'utiliser import.
Les onctions sont donc rangées dans des modules qui sont eux-mêmes rangés dans des packages qui peuvent être contenus dans de plus grands packages.

Si le programme rencontre une erreur il est possible de recommencer l'action.
Pour cela il faut utiliser les mots clés try et except
Par exemple si je demande un nombre et que l'utilisateur saisit une chaine de caractères, le programme plante
pour éviter ca dans le programme, enfermer l'instruction qui risque de planter dans un bloc try:
et ensuite un bloc except: et mettre les instructions à effectuer en cas de problème
Ces instructions ne différencient pas les types d'erreurs/exceptions qui peuvent être levées. Il faut définir des instructions à effectuer en fonction de l'erreur
en nottant except nomDeLErreur:
Autrement, l'exception ctrl + C pour fermer le programme sera traitée comme une exception et le programme ne se fermera pas.
On peut mettre plusieurs blocs erreurs traitant les differents types d'erreurs à la suite

On peut également faire en sorte que le programme affiche le type d'ereur en l'associant à une variable
except: type_de_l_exception as erreur
print("voici l'erreur", erreur)
Il faut donc entrer plusieurs blocs ainsi avec les différents types d'erreurs pour que le programme affiche la bonne
Une erreur de convertion s'appelle ValueError
si une variable utilisée n'existe pas c'est une erreur appellée NameError
Si une opération est aeffectuée sur un type qui ne peut l'effectuer c'est une erreur TypeError
et la division par zéro est ZeroDivisionError

Le raccourci Ctrl+C permet de fermer le programme

On distiingue le bloc try qui peut provoquer des erreurs de ce qui s'effectue s'il n'y en a pas grâce au mot clé else:
Pour effectuer des instructions après le bloc try quelqu'en soit le résultat il faut mettre un bloc finally:
Même si le bloc try contient un return, e bloc s'effectuera
On peut également faire en sorte que rien ne se passe en cas d'erreur en mettant le mot clé' pass dans un bloc except:

On peut vérifier qu'une condition est respectée grâce au mot clé' assert
la syntaxe est celle ci : assert test
par exemple assert a==5
si cette condition est fausse, une exception du type AssertionError sera levée. On peut donc ainsi faire en sorte de régler le problème

on peut lever nous mêmes les exceptions grâce au mot clé raise
la syntaxe estcelle là
if nanana
    raise TypeDeLErreur("texte à saisir")
Voir roulette pour plein d'autres options