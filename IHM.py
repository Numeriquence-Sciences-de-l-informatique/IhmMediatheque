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
        self.data = Datagrid(self, data_csv)
        self.data.pack()

def main():
    f = Fenetre()
    f.mainloop()

if __name__ == '__main__':
    main()