def beregn_diff(liste):
    differanser = []

    for num in range(len(liste) - 1):
        diff = liste[num + 1] - liste[num]
        differanser.append(diff)

    return differanser
liste_input = [1, 3, 6, 10, 15]
differanser = beregn_diff(liste_input)
print(differanser)
