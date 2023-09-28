# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 17:46:29 2023

@author: Stian
"""


def beregn_plantevekst(temperaturliste):
    total_vekst = 0
    
    for temperatur in temperaturliste:
        if temperatur > 5:
            vekst = temperatur - 5
            total_vekst += vekst
    
    return total_vekst

temperaturliste = [1, 4, 7, 11, 15, 20]
total_vekst = beregn_plantevekst(temperaturliste)
print(f"Total plantevekst: {total_vekst}")
