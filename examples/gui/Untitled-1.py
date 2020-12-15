def liste_entier_pairs():
   liste = [i for i in range(0, 102, 2)]
   liste.extend(i for i in range(99, 0, -1))
   return liste
