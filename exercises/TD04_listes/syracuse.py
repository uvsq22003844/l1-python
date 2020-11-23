def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    res = []
    while True:
        res.append(n)
        if n == 1:
            break
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
    return res


print(syracuse(3))


def alt_max(n):
    alt = n
    while True:
        if n == 1:
            break
        if n > alt:
            alt = n
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    return alt


print("L'altitude maximale est", alt_max(3))
liste_altitude = [alt_max(i) for i in range(1, 10001)]
altitude_max = max(liste_altitude)
print("L'altitude maximale entre 1 et 10000", altitude_max)
print("elle est atteinte par l'entier", liste_altitude.index(altitude_max) + 1)
