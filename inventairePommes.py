inventaire = [("pommes",22),("melons",4),("poires",18),("fraises", 76),("prunes",51)]

inventaire_inverse = [(qtt,fruit) for (fruit,qtt) in inventaire]

inventaire = [(fruit,qtt) for (qtt,fruit) in sorted(inventaire_inverse)]

print(inventaire)
input()