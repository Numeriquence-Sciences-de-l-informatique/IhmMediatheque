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
        self.mediatheque.initialisation()
        self.texte: str = "Hi"
        self.nombre: int = 10
        self.title("Médiathèque")
        self.geometry('640x480')
        self.onglets = ttk.Notebook(self)  # Création du système d'onglets
        self.onglets.pack(fill=tk.BOTH, expand=1)
        o1 = Medias(self.onglets)  # Ajout de l'onglet 1
        o1.pack(side=LEFT)
        o2 = Adherents(self.onglets)  # Ajout de l'onglet 2
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


class Medias(ttk.Notebook):
    def __init__(self, fenetre):
        super().__init__(fenetre)
        self.fenetre = fenetre
        self.pack()
        self.ld = ListeDocs(self)
        self.add(Creerlivre(self), text="creer livre")
        self.add(CreerCD(self), text="creer CD")
        self.add(SearchCD(self), text="Rechercher Document")
        self.add(self.ld, text="Liste des documents")


class Creerlivre(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # first Label
        ttk.Label(self, text="Titre").grid(row=0, column=0, padx=12, pady=5)

        # first Entry: titre
        self.titre = ttk.Entry(self)
        self.titre.grid(row=0, column=1)

        # second Label
        ttk.Label(self, text="Auteur").grid(row=1, column=0, padx=5, pady=5)

        # second Entry: auteur
        self.auteur = ttk.Entry(self)
        self.auteur.grid(row=1, column=1)

        # first Button: Create a book
        self.b1 = ttk.Button(self, text="Créer", command=self.creerLivre)
        self.b1.grid(row=2, column=1, padx=5, pady=5)

    def creerLivre(self):
        self.master.master.master.mediatheque.add(Livre(self.titre.get(), self.auteur.get()))
        self.master.ld.data.reload_data(self.master.master.master.mediatheque.to_csv())
        print(self.master.master.master.mediatheque)


class CreerCD(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        # For Title
        ttk.Label(self, text="Titre").grid(row=0, column=0, padx=12, pady=5)
        self.title = ttk.Entry(self)
        self.title.grid(row=0, column=1)

        # For Compositeur
        ttk.Label(self, text="Compositeur").grid(row=1, column=0, padx=12, pady=5)
        self.compositor = ttk.Entry(self)
        self.compositor.grid(row=1, column=1)

        # For Interprete
        ttk.Label(self, text="Interprete").grid(row=2, column=0, padx=12, pady=5)
        self.interprete = ttk.Entry(self)
        self.interprete.grid(row=2, column=1)

        # For the Button
        self.b1 = ttk.Button(self, text="Créer", command=self.createCD)
        self.b1.grid(row=5, column=1, padx=5, pady=5)

    def createCD(self):
        self.master.master.master.mediatheque.add(CD(self.title.get(), self.interprete.get(), self.compositor.get()))
        self.master.ld.data.reload_data(self.master.master.master.mediatheque.to_csv())
        print(self.master.master.master.mediatheque)


class ListeDocs(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.med_csv = self.master.master.master.mediatheque.to_csv()
        self.data = Datagrid(self, self.med_csv)
        self.data.pack()


class SearchCD(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        ttk.Label(self, text="Titre du document").grid(row=0, column=0, padx=12, pady=5)
        self.title = ttk.Entry(self)
        self.title.grid(row=0, column=1)

        self.search = ttk.Button(self, text="Rechercher", command=self.searchLivre)
        self.search.grid(row=1, column=1, padx=12, pady=7)

    def searchLivre(self):
        index: int = self.master.master.master.mediatheque.search(self.title.get())
        print(index)


class Adherents(ttk.Notebook):
    def __init__(self, fenetre):
        super().__init__(fenetre)
        self.pack()
        self.add(CreerAdherents(self), text="creer un Adherent")
        self.add(SupprimeAdherents(self), text="suprimer un Adherent")
        self.add(SearchCD(self), text="Liste des Adherents")


class CreerAdherents(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        # For Title
        ttk.Label(self, text="Nom").grid(row=0, column=0, padx=12, pady=5)
        self.title = ttk.Entry(self)
        self.title.grid(row=0, column=1)

        # For the Button
        self.b1 = ttk.Button(self, text="Créer", command=self.createAdherent)
        self.b1.grid(row=5, column=1, padx=5, pady=5)

    def createAdherent(self):
        self.master.master.master.mediatheque.add(Adherent(self._name.get()))
        print(self.master.master.master.mediatheque)


class SupprimeAdherents(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        # For Nom
        ttk.Label(self, text="Nom").grid(row=0, column=0, padx=12, pady=5)
        self.title = ttk.Entry(self)
        self.title.grid(row=0, column=1)

        # For the Button
        self.b1 = ttk.Button(self, text="Supprimer", command=self.suprimeAdherent)
        self.b1.grid(row=5, column=1, padx=5, pady=5)

    def suprimeAdherent(self):
        self.master.master.master.mediatheque.supprime(Adherent(self._name.get()))
        print(self.master.master.master.mediatheque)

class ListeAdherent(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        med_csv = self.master.master.master.mediatheque.to_csv()

    #methode non terminer



def main():
    f = Fenetre()

    f.mainloop()


if __name__ == '__main__':
    main()
