from tkinter import ttk
from tkinter import Scrollbar
class Datagrid(ttk.Treeview):
    def __init__(self, parent, data_csv: str):
        dic_align = {"<": "w", ">": "e", "^": "center"}
        table = data_csv.split("\n")
        if table[-1] == "":
            table = table[:-1]
        header = table[0].split(";")
        wcol = []
        align = []
        for i in range(len(header)):
            h1 = header[i].split(":")
            print('header',h1)
            if len(h1) == 1:
                wcol.append(len(h1[0]) * 10)
                align.append("w")
            else:
                h1[1] = h1[1].replace(" ", "")
                if h1[1][0] in "<>^":
                    wcol.append(int(h1[1][1:]))
                else:
                    wcol.append(int(h1[1]))
                align.append(dic_align.get(h1[1][0], "e"))
                header[i] = header[i][:header[i].find(":")]
        super().__init__(parent, selectmode="browse", show="headings", columns=header)
        self.pack(side='left', fill='both', expand=1)
        self.bind('<ButtonRelease-1>', self.OnClick)
        scrollbar_y = Scrollbar(parent, command=self.yview)
        scrollbar_y.pack(side='right', fill='y')
        for i, h in enumerate(header):
            self.column(h, width=wcol[i], anchor=align[i])
            self.heading(h, text=h, anchor="center")
        if len(table) > 1:
            for i in range(1, len(table)):
                print(i, table[i])
                t = table[i].split(";")
                self.insert('', 'end', text="", values=t)

    def reload_data(self,data_csv:str):
        table = data_csv.split("\n")
        self.delete(*self.get_children())
        if table[-1] == "":
            table = table[:-1]
        for i in range(1, len(table)):
            print(i, table[i])
            t = table[i].split(";")
            self.insert('', 'end', text="", values=t)

    def OnClick(self, event):
        try:
            self.master.OnClick(event)
        except:
            pass


def main():
    pass


if __name__ == '__main__':
    main()