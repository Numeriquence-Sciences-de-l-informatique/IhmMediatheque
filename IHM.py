from tkinter import Tk, ttk, Menu
from tkinter.ttk import Notebook

from datagrid import Datagrid
class Fenetre(Tk):
    def __init__(self):
        super().__init__()
        self.texte:str = "Hi"
        self.nombre:int = 10
        self.title("Médiathèque")
        self.geometry('640x480')

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




def main():
    f = Fenetre()

    f.mainloop()

if __name__ == '__main__':
    main()