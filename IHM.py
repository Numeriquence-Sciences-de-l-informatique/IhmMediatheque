from tkinter import Tk, ttk
from datagrid import Datagrid
class Fenetre(Tk):
    def __init__(self):
        super().__init__()
        self.texte:str = "Hi"
        self.nombre:int = 10
        self.title("Médiathèque")
        self.geometry('640x480')
        data_csv = "colonne1:50;colonne2:100;colonne3:50\n11;12;13\n21;22;23"
        self.data = Datagrid(data_csv)
        self.data.pack()

class Medias(ttk.Notebook):
    def __init__(self,fenetre):
        self.fenetre = fenetre
        self.pack()
        self.add(Creerlivre(self),text="creer livre")

class Creerlivre():
    def __init__(self,parent):
        self.parent = parent
        l1 = ttk.Label(text = "titre")
        l1.pack(padx = 5, pady = 5)
        l2 = ttk.Label(text = "auteur")
        l2.pack(padx)



def main():
    f = Fenetre()
    f.mainloop()

if __name__ == '__main__':
    main()