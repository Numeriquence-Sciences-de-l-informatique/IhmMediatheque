from tkinter import Tk, ttk, Menu
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.ttk import Notebook, Progressbar

from datagrid import Datagrid

class Fenetre(Tk):
    def __init__(self):
        super().__init__()
        self.texte:str = "Hi"
        self.nombre:int = 10
        self.title("Médiathèque")
        self.geometry('640x480')
        self.onglets = ttk.Notebook(self)  # Création du système d'onglets
        self.onglets.pack(fill=tk.BOTH, expand=1)
        o1 = ttk.Frame(self.onglets)  # Ajout de l'onglet 1
        o1.pack(side=LEFT)
        o2 = ttk.Frame(self.onglets)  # Ajout de l'onglet 2
        o2.pack(side=LEFT)
        self.onglets.add(o1, text='Médiathèque')  # Nom de l'onglet 1
        self.onglets.add(o2, text='Adhérents')  # Nom de l'onglet 2

        """
        Sélection du document 
        """
        rad1 = Radiobutton(o1, text='Tout les Documents', value=1)
        rad2 = Radiobutton(o1, text='Livres', value=2)
        rad3 = Radiobutton(o1, text='CD', value=3)

        rad1.grid(column=0, row=0)
        rad2.grid(column=1, row=0)
        rad3.grid(column=2, row=0)

        lbl = Label(o2, text="Hello", font=("Arial Bold", 50))
        lbl.pack()

        style = ttk.Style()

        style.theme_use('classic')

        style.configure("black.Horizontal.TProgressbar", background='black')

        bar = Progressbar(o2, length=200, style='black.Horizontal.TProgressbar')


class Medias(ttk.Notebook):
    def __init__(self,fenetre):
        self.fenetre = fenetre
        self.pack()
        self.add(Creerlivre(self),text="creer livre")


class Creerlivre(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        l1 = ttk.Label(text="titre")
        l1.pack(padx = 5, pady = 5)
        l2 = ttk.Label(text="Auteur")
        l2.pack(padx = 5, pady = 5)
        b1 = ttk.Button()
        b1.pack()


def main():
    f = Fenetre()

    f.mainloop()

if __name__ == '__main__':
    main()