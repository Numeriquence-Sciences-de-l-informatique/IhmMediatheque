## Onglets

from tkinter import *
from tkinter import ttk

jeu = Tk()

n = ttk.Notebook(jeu)   # Création du système d'onglets
n.pack()
o1 = ttk.Frame(n)       # Ajout de l'onglet 1
o1.pack()
o2 = ttk.Frame(n)       # Ajout de l'onglet 2
o2.pack()
n.add(o1, text='Onglet 1')      # Nom de l'onglet 1
n.add(o2, text='Onglet 2')      # Nom de l'onglet 2

Button(o1, text='Quitter', command=jeu.destroy).pack(padx=100, pady=100)
Button(o2, text='En attente', command=None).pack(padx=100, pady=100)

jeu.mainloop()