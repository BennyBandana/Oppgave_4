# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 17:56:38 2023

@author: Stian
"""

from lister_for_del_1 import temperaturer

def tell_storre_eller_lik(liste, verdi):
    antall_storre_eller_lik = 0
    
    for element in liste:
        if element >= verdi:
            antall_storre_eller_lik += 1
    
    return antall_storre_eller_lik

sommerdager = tell_storre_eller_lik(temperaturer, 20)
høysommerdager = tell_storre_eller_lik(temperaturer, 25)
tropedager = tell_storre_eller_lik(temperaturer, 30)

print(f"Antall sommerdager (over 20 grader): {sommerdager}")
print(f"Antall høysommerdager (over 25 grader): {høysommerdager}")
print(f"Antall tropedager (over 30 grader): {tropedager}")
