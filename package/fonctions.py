"""module donnant les tables de multiplications"""

def table(a,max=10):
    """fonction affichant la table de multiplication de a, de 1*a à max*a"""
    b=0

    while b<max:
        print(b+1,"x",a, "=", (b+1)*a)
        b+=1