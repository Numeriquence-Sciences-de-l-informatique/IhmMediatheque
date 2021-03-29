from tkinter import *
from tkinter import ttk
import tkinter as tk
from Mediatheque import *

from datagrid import Datagrid


class Fenetre(Tk):
    def __init__(self):
        super().__init__()
        self.mediatheque = Mediatheque()
        self.adherents = Adhesions()
        self.texte: str = "Hi"
        self.nombre: int = 10
        self.title("Médiathèque")
        self.geometry('640x480')
        self.onglets = ttk.Notebook(self)  # Création du système d'onglets
        self.onglets.pack(fill=tk.BOTH, expand=1)
        o1 = Medias(self.onglets)  # Ajout de l'onglet 1
        o1.pack(side=LEFT)
        o2 = ttk.Frame(self.onglets)  # Ajout de l'onglet 2
        o2.pack(side=LEFT)
        self.onglets.add(o1, text='Médiathèque')  # Nom de l'onglet 1
        self.onglets.add(o2, text='Adhérents')  # Nom de l'onglet 2

        """
        Sélection du document 
        """
        # rad1 = Radiobutton(o1, text='Tout les Documents', value=1)
        # rad2 = Radiobutton(o1, text='Livres', value=2)
        # rad3 = Radiobutton(o1, text='CD', value=3)
        #
        # rad1.grid(column=0, row=0)
        # rad2.grid(column=1, row=0)
        # rad3.grid(column=2, row=0)
        lbl = Label(o2, text="Hello", font=("Arial Bold", 50))
        lbl.pack()


class Medias(ttk.Notebook):
    def __init__(self, fenetre):
        super().__init__(fenetre)
        self.fenetre = fenetre
        self.pack()
        self.add(Creerlivre(self), text="creer livre")
        self.add(CreerCD(self), text="creer CD")


class Creerlivre(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        c1 = ttk.Frame(self, borderwidth=5)
        c1.pack()
        ttk.Label(c1, text="titre").pack(padx=5, pady=5, side="left")
        self.titre = ttk.Entry(c1)
        self.titre.pack(padx=5, pady=5)

        c2 = ttk.Frame(self, borderwidth=5)
        c2.pack()
        ttk.Label(c2, text="Auteur").pack(padx=5, pady=5, side="left")
        self.auteur = ttk.Entry(c2)
        self.auteur.pack(padx=5, pady=5)
        self.b1 = ttk.Button(self, text="Créer", command=self.creer)
        self.b1.pack()

    def creer(self):
        self.master.master.master.mediatheque.add(Livre(self.titre.get(), self.auteur.get()))
        print(self.master.master.master.mediatheque)


class CreerCD(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        f1 = ttk.Frame(self, borderwidth=5)
        f1.pack()
        ttk.Label(f1, text="Titre").pack(padx=31, pady=5, side="left")
        self.title = ttk.Entry(f1)
        self.title.pack(padx=5, pady=5, side="right")

        f2 = ttk.Frame(self, borderwidth=5)
        f2.pack()
        ttk.Label(f2, text="Compositeur").pack(padx=5, pady=5, side="left")
        self.compositeur = ttk.Entry(f2)
        self.compositeur.pack(padx=5, pady=5)

        f3 = ttk.Frame(self, borderwidth=5)
        f3.pack()
        ttk.Label(f3, text="Interprete").pack(padx=13, pady=5, side="left")
        self.interprete = ttk.Entry(f3)
        self.interprete.pack(padx=5, pady=5)

        self.b1 = ttk.Button(self, text="Créer", command=self.createCD())
        self.b1.pack()


    def createCD(self):
        self.master.master.master.mediatheque.add(CD(self.title.get(), self.compositeur.get(), self.interprete.get()))
        print(self.master.master.master.mediatheque)


def main():
    f = Fenetre()

    f.mainloop()


if __name__ == '__main__':
    main()
