from oppgave_F import null_sekvens
from lister_for_del_1 import dogn_nedbor

# bruker null_sekvens funksjon fra oppgave_F
def dogn_torke():
    return null_sekvens(dogn_nedbor)  # Endret her

# Kjører funksjonen og lagrer resultatet i en variabel
lengste_tork_periode = dogn_torke()

# Skriver ut resultatet
print(f"Lengste periode uten nedbør er: {lengste_tork_periode} dager")
