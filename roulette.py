import random

mise = 10

parite_joueur = input("Pariez sur pair ou impair : ").lower()
couleur_joueur = input("Pariez sur rouge ou noir : ").lower()
numero_joueur = input("Pariez sur un numéro entre 0 et 12 ou : ").lower()
if numero_joueur:
    numero_joueur = int(numero_joueur)
else:
    numero_joueur = None

numero = random.randint(0, 12)
print("Numéro tiré :", numero)

if numero == 0:
    parite_numero = None
else:
    if numero % 2 == 0:
        parite_numero = "pair"
    else:
        parite_numero = "impair"

rouges = [1, 3, 5, 7, 9, 12]
noirs = [2, 4, 6, 8, 10, 11]

if numero in rouges:
    couleur_numero = "rouge"
elif numero in noirs:
    couleur_numero = "noir"
else:
    couleur_numero = None

if parite_numero != parite_joueur:
    print("Perdu. Vous perdez", mise, "euros.")
else:
    if couleur_numero == couleur_joueur:
        print("Gagné. Pair/impair et couleur corrects.")
        print("Gain :", mise * 3, "euros.")
    else:
        print("Gagné. Pair/impair correct.")
        print("Gain :", mise * 2, "euros.")