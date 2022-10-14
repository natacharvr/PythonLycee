import sys
sys.path.append('package/')
from tables_de_multiplications import *

while 1:
    v = input("Voulez-vous connaître la table de multiplication d'un nombre? Notez 1 pour oui et 2 pour non")
    v = int(v)
    if v==1:
        a = input("saisissez le nombre dont vous voulez connaître  la table de multiplication : ")
        a = int(a)

        max = input("saisissez jusqu'où vous souhaitez connaître la table de multiplication : ")
        max = int(max)

        table(a,max)
        continue
    else:
        input("appuyez sur entrée pour fermer")
        break
