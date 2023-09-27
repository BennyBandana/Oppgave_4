def null_sekvens(liste):
    Antall = 0
    lengde = 0

    for num in liste:
        if num == 0:
            lengde += 1
            if lengde > Antall:
                Antall = lengde
        else:
            lengde = 0

    return Antall


Tallliste = [1, 0, 0, 3, 0, 0, 4, 5, 0, 0,0]
lengde = null_sekvens(Tallliste)
print(f"Lengste sekvensen av nuller er: {lengde}")