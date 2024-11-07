#from math import sqrt
#### Fonction secondaire
"""
Permet de déterminer si un entier est premier

"""
def isprime(p):
    """
    Fonction qui permet de déterminer si un entier est premier
    """

    # votre code ici
    #premier = True
    #p = int(input("Entrer votre nombre:"))
    #RCp = int(math.sqrt(p))
    if p<=1 :
        return False
    for i in range(2, p-1):
        if p%i == 0:
            return False


    return True


#### Fonction principale


def main():
    """
    Fonction principale
    """
    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=",")
        #print()

if __name__ == "__main__":
    main()
