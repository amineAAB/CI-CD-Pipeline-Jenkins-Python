import math

def somme(liste):
    return sum(liste)

def moyenne(liste):
    # moy = somme(liste) / len(liste)    
    if len(liste) == 0:
        return 0
    
    return somme(liste) / len(liste)

def ecart_type(liste):
    if len(liste) == 0:
        return 0
    moy = moyenne(liste)
    ecarts = [(x - moy) ** 2 for x in liste]
    variance = sum(ecarts) / len(liste)
    return variance ** 0.5

