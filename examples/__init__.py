#temps[0] : années, temps[1]: jours, temps[2]: heures

heure = 0
annee = 2020

def tempsEnHeure(temps):
    return((((temps[2] / 24) + temps[[1]) * 365) + temps[0])

temps = (annee, 0, 0)
print(type(temps))
print(tempsEnAnnee(temps))