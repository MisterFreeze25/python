somme = 0
compteur = 0

valeur = int(input("Entrez une taille (-1 pour terminer) : "))

while valeur != -1:
    somme = somme + valeur
    compteur = compteur + 1
    valeur = int(input("Entrez une taille (-1 pour terminer) : "))

if compteur == 0:
    print("Aucune donnée saisie.")
else:
    moyenne = somme / compteur
    print("La taille moyenne est :", moyenne)