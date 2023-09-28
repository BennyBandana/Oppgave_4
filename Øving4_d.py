# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



def tell_storre_eller_lik(liste, verdi):
    antall_storre_eller_lik = 0
    
    for element in liste:
        if element >= verdi:
            antall_storre_eller_lik += 1
    
    return antall_storre_eller_lik

min_liste = [1.846, 2.8576, 3.999999, 4.00001, 4.63542, 6.000463, 9.47, 10.9999, 16.23]
verdi = 4.0

resultat = tell_storre_eller_lik(min_liste, verdi)
print(f"Antall elementer større enn eller lik {verdi}: {resultat}")
