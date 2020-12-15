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


def circle:
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


root = tk.Tk()
root.title("Mon dessin")

bouton_couleur = tk.Bouton(root, text="Choisir une couleur", bg="grey100", fg="blue", padx=20, font=("Time", "20"))
bouton_cercle = tk.Bouton(root, text="Cercle", bg="grey100", fg="blue", padx=20, font=("Time", "20"), command=cercle)
bouton_carre = tk.Bouton(root, text="Carré", bg="grey100", fg="blue", padx=20, font=("Time", "20"), command=carre)
bouton_croix = tk.Bouton(root, text="Croix", bg="grey100", fg="blue", padx=20, font=("Time", "20"), command=croix)
