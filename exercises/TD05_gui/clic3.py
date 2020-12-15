import tkinter as tk

nb_clic = 0
point = (0, 0)


def draw_pixel(event):
    global nb_clic, point
    if nb_clic == 0:
        nb_clic = 1
        point = (event.x, event.y)
    else:
        nb_clic = 0
        if (250 - event.x) * (250 - point[0]) >= 0:
            color = "blue"
        else:
            color = "red"
        canvas.create_line(point, (event.x, event.y), fill=color)


root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500, bg="black")
canvas.create_line(point, (event.x, event.y), outline+"white", fill="black")
canvas.bind("<Button-1>", draw_pixel)
canvas.grid()
root.mainloop()
