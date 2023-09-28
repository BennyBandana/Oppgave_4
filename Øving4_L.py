# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 18:11:04 2023

@author: Stian
"""

from lister_for_del_1 import temperaturer

def beregn_plantevekst(temperaturliste):
    summen = 0  

    for temperatur in temperaturliste:
        if temperatur > 5:
            vekst = temperatur - 5  
            summen += vekst  

    return summen

total_vekst = beregn_plantevekst(temperaturer)

print("Total vekst for planten er:", total_vekst)

