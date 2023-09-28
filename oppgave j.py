def beregn(liste):
    diff = []

    for t in range(len(liste) - 1):
        diff1 = liste[t + 1] - liste[t]
        diff.append(diff1)

    return diff

def finn_trend(diff_liste):
    for indeks, diff in enumerate(diff_liste):
        if diff > 0:
            print(f"Tidspunkt {indeks}: Stigende")
        elif diff < 0:
            print(f"Tidspunkt {indeks}: Synkende")
        else:
            print(f"Tidspunkt {indeks}: Uforandret")

liste_input = [1, 3, 6, 10, 15]
differanser = beregn(liste_input)
print(differanser)
finn_trend(differanser)
