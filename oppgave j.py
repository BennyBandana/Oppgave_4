def beregn_diff(liste):
    diff = []

    for i in range(len(liste) - 1):
        diff1 = liste[i + 1] - liste[i]
        diff.append(diff1)

    return differanser

def finn_trend(diff_liste):
    for indeks, diff in enumerate(diff_liste):
        if diff > 0:
            print(f"Tidspunkt {indeks}: Stigende")
        elif diff < 0:
            print(f"Tidspunkt {indeks}: Synkende")
        else:
            print(f"Tidspunkt {indeks}: Uforandret")

liste_input = [1, 3, 6, 10, 15]
differanser = beregn_diff(liste_input)
print(differanser)
finn_trend(differanser)
