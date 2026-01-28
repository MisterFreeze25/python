def f(x)    :
    return 70-0.006*x*x-0.28*x

#On définit la fonction f sur laquelle on raisonne
#On cherche x tel que f(x)=0

def dicho(a, b, precision):
    if b-a<=precision :
        return a,b
    else : 
        c=a+(b-a)/2
        if f(a)*f(c)<= 0 :
            return dicho(a,c,precision)
        else :
            return dicho(c,b,precision)

#On crée une boucle permettant de trouver un intervalle [a,b] tel que f(a) et f(b) soient de signes contraires
   
solution=dicho(50,100,0.01)

#La procédure dicho() comporte trois paramètres
#Le premier correspond à la borne inférieure de l'intervalle
#Le deuxième correspond à la borne supérieure de l'intervalle
#Le troisième corespond à la précision souhaitée

print(solution)