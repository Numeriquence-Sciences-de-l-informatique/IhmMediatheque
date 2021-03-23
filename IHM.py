from tkinter import Tk, ttk, Menu
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.ttk import Notebook

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
        self.onglets.add(o1, text='Onglet 1')  # Nom de l'onglet 1
        self.onglets.add(o2, text='Onglet 2')  # Nom de l'onglet 2
        data_csv = "colonne1:50;colone2:100;colonne3:50\n11;12;13\n21;22;23"
        data = Datagrid(o1, data_csv)
        data.pack()


class Medias(ttk.Notebook):
    def __init__(self,fenetre):
        self.fenetre = fenetre
        self.pack()
        self.add(Creerlivre(self),text="creer livre")


class Creerlivre(ttk.Frame):
    def __init__(self,parent):
        self.parent = parent
        l1 = ttk.Label(text="titre")
        l1.pack(padx = 5, pady = 5)
        l2 = ttk.Label(text="Auteur")
        l2.pack(padx = 5, pady = 5)
        b1 = ttk.Button()


        



        # data_csv = "colonne1:50;colonne2:100;colonne3:50\n11;12;13\n21;22;23"
        # self.data = Datagrid(self, data_csv)
        # self.data.pack()

class Medias(Frame):
    def __init__(self):
        super().__init__()



def main():
    f = Fenetre()

    f.mainloop()

if __name__ == '__main__':
    main()