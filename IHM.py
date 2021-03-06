from tkinter import *
from tkinter import ttk, messagebox
from tkinter.font import Font
import tkinter as tk
from tkinter.messagebox import askokcancel

from Mediatheque import *
from Mediatheque import Livre

from datagrid import Datagrid


class Fenetre(Tk):
    def __init__(self):
        super().__init__()
        self.mediatheque = Mediatheque()
        self.adherents = Adhesions()
        self.mediatheque.initialisation()
        self.adherents.initialisation()
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
        self.creerl = Creerlivre(self)
        self.creercd = CreerCD(self)
        self.add(self.creerl, text="creer livre")
        self.add(self.creercd, text="creer CD")
        self.add(SearchCD(self), text="Rechercher Document")
        self.add(self.ld, text="Liste des documents")


class Creerlivre(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.modifier = "Modifier"
        self.creer = "Créer"
        self.doc_courant: Union[Livre, None] = None
        # alias vers mediatheque
        self.mediatheque = self.master.master.master.mediatheque
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
        self.b1 = ttk.Button(self, text=self.creer, command=self.creerLivre)
        self.b1.grid(row=2, column=1, padx=5, pady=5)

        # second Button: Cancel modify
        self.b2 = ttk.Button(self, text="Annuler", command=self.annuler)

    def creerLivre(self):
        # selection de l'onglet Liste des documents
        self.master.select(3)
        if self.doc_courant is None:
            # création
            self.master.master.master.mediatheque.add(Livre(self.titre.get(), self.auteur.get()))
        else:
            # modification
            self.doc_courant.setTitle(self.titre.get())
            self.doc_courant.setAuthor(self.auteur.get())
            self.doc_courant = None
            self.b1['text'] = self.creer
        self.master.ld.data.reload_data(self.master.master.master.mediatheque.to_csv())

    def annuler(self):
        self.b2.grid_forget()
        self.b1['text'] = self.creer


class CreerCD(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # For Title
        self.parent = parent
        self.modifier = "Modifier"
        self.creer = "Créer"
        self.doc_courant: Union[CD, None] = None
        self.mediatheque = self.master.master.master.mediatheque

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
        self.b1.grid(row=3, column=1, padx=5, pady=5)

        # second Button: Cancel modify
        self.b2 = ttk.Button(self, text="Annuler", command=self.annuler)

    def annuler(self):
        self.b2.grid_forget()
        self.b1['text'] = self.creer

    def createCD(self):
        self.master.select(3)
        if self.doc_courant is None:
            self.master.master.master.mediatheque.add(
                CD(self.title.get(), self.interprete.get(), self.compositor.get()))
        else:
            self.doc_courant.setTitle(self.title.get())
            self.doc_courant.setCompositor(self.compositor.get())
            self.doc_courant.setInterprete(self.interprete.get())
            self.doc_courant = None
            self.b1['text'] = self.creer
        self.master.ld.data.reload_data(self.mediatheque.to_csv())


class ListeDocs(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.mediatheque = self.master.master.master.mediatheque
        self.med_csv = self.mediatheque.to_csv()
        self.data = Datagrid(self, self.med_csv)
        self.data.pack()

    def OnClick(self, event):
        select = self.data.identify('item', event.x, event.y)
        # recuperation du document (Livre ou CD) selectionné
        doc: Union[CD, Livre] = self.mediatheque.getDocument(int(self.data.item(select, "value")[0]))

        if isinstance(doc, Livre):
            if askokcancel(title="Modifier un Livre",
                           message=f"Voulez-vous modifier\n{doc.getTitle()} de {doc.getAuthor()}"):
                self.master.select(0)  # sélection de l'onglet créerLivre
                self.master.creerl.doc_courant: Livre = doc
                self.master.creerl.b1['text'] = self.master.creerl.modifier
                self.master.creerl.titre.delete(0, "end")
                self.master.creerl.titre.insert(0, doc.getTitle())
                self.master.creerl.auteur.delete(0, "end")
                self.master.creerl.auteur.insert(0, doc.getAuthor())
                self.master.creerl.b2.grid(row=2, column=2, padx=5, pady=5)
        else:
            if askokcancel(title="Modifier un CD",
                           message=f"Voulez-vous modifier\n{doc.getTitle()} de {doc.getCompositor()}"):
                self.master.select(1)  # sélection de l'onglet créerCD
                self.master.creercd.doc_courant: CD = doc
                self.master.creercd.b1['text'] = self.master.creercd.modifier
                self.master.creercd.title.delete(0, "end")
                self.master.creercd.title.insert(0,  doc.getTitle())
                self.master.creercd.compositor.delete(0, "end")
                self.master.creercd.compositor.insert(0, doc.getCompositor())
                self.master.creercd.interprete.delete(0, "end")
                self.master.creercd.interprete.insert(0, doc.getInterprete())
                self.master.creercd.b2.grid(row=3, column=2, padx=5, pady=5)



class SearchCD(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.mediatheque = self.master.master.master.mediatheque
        font = Font(family="courier")

        ttk.Label(self, text="Titre du document").grid(row=0, column=0, padx=12, pady=5)
        self.title = ttk.Entry(self)
        self.title.grid(row=0, column=1)

        self.search = ttk.Button(self, text="Rechercher", command=self.searchLivre)
        self.search.grid(row=1, column=1, padx=12, pady=7)

        self.list_doc = ttk.Label(self, text="", font=font)
        self.list_doc.grid(row=2, column=0, padx=0, pady=25, columnspan=10)

    def searchLivre(self):
        index: int = self.mediatheque.search_to_list(self.title.get())
        s = ""
        for i in index:
            s += str(self.mediatheque.getDocument(i)) + "\n"
        self.list_doc["text"] = s
        print(s)


class Adherents(ttk.Notebook):
    def __init__(self, fenetre):
        super().__init__(fenetre)
        self.pack()
        self.add(CreerAdherents(self), text="creer un Adherent")
        self.add(SupprimeAdherents(self), text="suprimer un Adherent")
        self.list_Ad = ListeAdherent(self)
        self.add(self.list_Ad, text="Liste des Adherents")


class CreerAdherents(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        # For Title
        ttk.Label(self, text="Nom").grid(row=0, column=0, padx=12, pady=5)
        self.name = ttk.Entry(self)
        self.name.grid(row=0, column=1)

        # For the Button
        self.b1 = ttk.Button(self, text="Créer", command=self.createAdherent)
        self.b1.grid(row=5, column=1, padx=5, pady=5)

    def createAdherent(self):
        if self.name.get() in Adherent:
            messagebox.showerror(title=None, message="cet utilisateur n'existe pas")
            if messagebox.askquestion(title=None, message="creer cet utilisateur") == "yes":
                self.master.master.master.adherents.add(Adherent(self.name.get()))
                self.master.list_Ad.data.reload_data(self.master.master.master.adherents.to_csv())
                print(self.master.master.master.adherents)


class SupprimeAdherents(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        # For Nom
        ttk.Label(self, text="Nom").grid(row=0, column=0, padx=12, pady=5)
        self.name = ttk.Entry(self)
        self.name.grid(row=0, column=1)

        # For the Button
        self.b1 = ttk.Button(self, text="Supprimer", command=self.supprimeAdherent)
        self.b1.grid(row=5, column=1, padx=5, pady=5)

    def supprimeAdherent(self):
        ad: Adhesions = self.master.master.master.adherents
        ad.supprime(ad.get_by_name(self.name.get()))
        self.master.list_Ad.data.reload_data(self.master.master.master.adherents.to_csv())
        print(self.master.master.master.adherents)

        if self.name.get() not in Adherent:
            messagebox.showerror(title=None, message="cet utilisateur n'existe pas")
            if messagebox.askquestion(title=None, message="supprimer cet utilisateur", icon="warning") == "yes":
                ad: Adhesions = self.master.master.master.adherents
                ad.supprime(ad.get_by_name(self.name.get()))
                self.master.list_Ad.data.reload_data(self.master.master.master.adherents.to_csv())
                print(self.master.master.master.adherents)


class ListeAdherent(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        ad: Adhesions = self.master.master.master.adherents
        self.ad_csv = ad.to_csv()
        self.data = Datagrid(self, self.ad_csv)
        self.data.pack()


def main():
    f = Fenetre()

    f.mainloop()


if __name__ == '__main__':
    main()
