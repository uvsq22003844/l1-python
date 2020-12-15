import tkinter as tk
import random as rd

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400

# if __name__ == '__main__':
root = tk.Tk()
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)

# Début de votre code
x0 = 100
x1 = CANVAS_WIDTH - 100
y = CANVAS_HEIGHT / 2

canvas.create_line(x0, y, x1, y)
canvas.create_oval(x0 - 50, y + 50, x0 + 50, y - 50)
canvas.create_oval(x1 - 50, y + 50, x1 + 50, y - 50)
canvas.create_oval((x0 + x1) / 2 - 50, y + 50, (x0 + x1) / 2 + 50, y - 50)

# Fin de votre code

canvas.pack()
root.mainloop()


def cercle:
    x = rd.randint(0, 401)
    y = rd.randint(0, 401)
    canvas.create_oval((x, y), (x+100, y+100), fill="blue")


def carree:
    x = rd.randint(0, 401)
    y = rd.randint(0, 401)
    canvas.create_rectangle((x, y), (x+100, y+100), fill="red")


def croix:
    x = rd.randint(0, 401)
    y = rd.randint(0, 401)
    canvas.create_line((x, y), (x+100, y+100), fill="yellow")
    canvas.create_line((x+100, y), (x, y+100), fill="yellow")


racine = tk.Tk()
racine.title("Mon dessin")

bouton_couleur = tk.Bouton(racine, text="Choisir une couleur", bg="grey100", fg="blue", padx=20, font=("Time", "20"))
bouton_cercle = tk.Bouton(racine, text="Cercle", bg="grey100", fg="blue", padx=20, font=("Time", "20"), command=cercle)
bouton_carre = tk.Bouton(racine, text="Carré", bg="grey100", fg="blue", padx=20, font=("Time", "20"), command=carre)
bouton_croix = tk.Bouton(racine, text="Croix", bg="grey100", fg="blue", padx=20, font=("Time", "20"), command=croix)

cpt = 0


def dessine_efface():
    global cpt, cercle
    cpt = 1 - cpt  # vaut alternativement 0 et 1
    if cpt == 0:
        cercle = canvas.create_oval((100, 100), (400, 400), fill="blue", width=5, outline="cyan")
    else:
        canvas.delete(cercle)
    canvas.after(1000, dessine_efface)


racine = tk.Tk()  # Création de la fenêtre racine
canvas = tk.Canvas(racine, bg="red", height=500, width=500)
canvas.grid(column=0, row=0)
cercle = canvas.create_oval((100, 100), (400, 400), fill="blue", width=5, outline="cyan")
dessine_efface()
racine.mainloop()  # Lancement de la boucle principale
