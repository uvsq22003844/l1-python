import tkinter as tk


def draw_pixel(event):
    canvas.create_oval((event.x, event.y), (event.x + 1, event.y), fill="red")


root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500, bg="black")
canvas.create_line(point, (event.x, event.y), outline+"white", fill="black")
canvas.bind("<Button-1>", draw_pixel)
canvas.grid()
root.mainloop()
