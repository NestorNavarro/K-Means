import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb


class MB:
    def __init__(self):
        self.Window = tk.Tk()
        self.labelframe1 = ttk.LabelFrame(self.Window, text="Ingrese los valores")
        self.labelframe1.grid(column=0, row=0, padx=10, pady=10)
        self.agregar_componentes()
        self.Window.mainloop()

    def agregar_componentes(self):
        self.label1 = ttk.Label(self.labelframe1, text="Valor de K:")
        self.label1.grid(column=0, row=0, padx=5, pady=5, sticky="e")
        self.k = tk.StringVar()
        self.entry1 = ttk.Entry(self.labelframe1, textvariable=self.k)
        self.entry1.grid(column=1, row=0, padx=5, pady=5)

        self.label2 = ttk.Label(self.labelframe1, text="Número de iteraciones:")
        self.label2.grid(column=0, row=1, padx=5, pady=5, sticky="e")
        self.n = tk.StringVar()
        self.entry2 = ttk.Entry(self.labelframe1, textvariable=self.n)
        self.entry2.grid(column=1, row=1, padx=5, pady=5)

        self.label3 = ttk.Label(self.labelframe1, text="Número de corridas:")
        self.label3.grid(column=0, row=2, padx=5, pady=5, sticky="e")
        self.c = tk.StringVar()
        self.entry3 = ttk.Entry(self.labelframe1, textvariable=self.c)
        self.entry3.grid(column=1, row=2, padx=5, pady=5)

        self.boton1 = ttk.Button(self.labelframe1, text="Ok", command=self.enter)
        self.boton1.grid(column=1, row=3, padx=5, pady=5, sticky="we")

    def enter(self):
        if self.k.get() == "" or self.n.get() == "" or self.c.get() == "":
            self.flag = False
            mb.showerror("Cuidado", "No puede dejar los cuadros de entrada de números vacíos")
        else:
            self.flag = True
            self.Window.destroy()




