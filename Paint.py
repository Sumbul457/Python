import tkinter as tk
from tkinter import colorchooser

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Paint Application")

        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack()

        self.color = "black"
        self.brush_size = 5

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        self.create_menu()

    def create_menu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        color_menu = tk.Menu(menu)
        menu.add_cascade(label="Color", menu=color_menu)
        color_menu.add_command(label="Choose Color", command=self.choose_color)

        brush_menu = tk.Menu(menu)
        menu.add_cascade(label="Brush Size", menu=brush_menu)
        brush_menu.add_command(label="Small", command=lambda: self.set_brush_size(2))
        brush_menu.add_command(label="Medium", command=lambda: self.set_brush_size(5))
        brush_menu.add_command(label="Large", command=lambda: self.set_brush_size(10))

        clear_menu = tk.Menu(menu)
        menu.add_cascade(label="Clear", menu=clear_menu)
        clear_menu.add_command(label="Clear Canvas", command=self.clear_canvas)

    def choose_color(self):
        self.color = colorchooser.askcolor()[1]

    def set_brush_size(self, size):
        self.brush_size = size

    def paint(self, event):
        x, y = event.x, event.y
        r = self.brush_size
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=self.color, outline=self.color)

    def reset(self, event):
        pass

    def clear_canvas(self):
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()