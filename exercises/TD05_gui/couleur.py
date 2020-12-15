import tkinter as tk


def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def draw_pixel(i, j, color):
    canvas.create_oval((i, j), (i+1, j), fill=color)

racine = tk.Tk()  # Création de la fenêtre racine

canvas = tk.Canvas(racine, text="", padx=20, pady=20, font=("helvetica", "30"))
canvas.grid(row=1, column=1, columnspan=3)

bouton1 = tk.Button(racine, text="Aléatoire", command=draw_pixel, font=("helvetica", "30"))
bouton1.grid(row=1, column=0)

bouton2 = tk.Button(racine, text="Dégradé gris", command=draw_pixel, font=("helvetica", "30"))
bouton2.grid(row=1, column=1)

bouton3 = tk.Button(racine, text="Dégradé 2D", command=draw_pixel, font=("helvetica", "30"))
bouton3.grid(row=1, column=3)

racine.mainloop()  # Lancement de la boucle principale
