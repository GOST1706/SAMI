import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from itertools import cycle

class AnimatedButton:
    def __init__(self, button):
        self.button = button
        self.colors = cycle(['red', 'green', 'blue', 'yellow', 'orange'])
        self.animate()

    def animate(self):
        color = next(self.colors)
        self.button.configure(background=color)
        self.button.after(1000, self.animate)

def on_button_click():
    messagebox.showinfo("Mensaje", "¡Haz clic en el botón animado!")

root = tk.Tk()
root.title("Botón Animado")

button = ttk.Button(root, text="Haz clic aquí", command=on_button_click)
button.pack()

animated_button = AnimatedButton(button)

root.mainloop()
