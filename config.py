import tkinter
from tkinter import ttk


class config:
    def __init__(self, master=None, title="config", geometry=[400, 400], apply_label="apply"):
        if not master:  self.master = tkinter.Tk()
        self.master = master
        self.master.attributes("-disabled", 1)

        self.width, self.height = geometry

        self.row = 0
        self.column = 0
        self.down = 0.06
        self.table = []
        self.cards = False
        self.soncards = {}

        self.root = tkinter.Toplevel(master=self.master)
        self.root.protocol("WM_DELETE_WINDOW", lambda : [self.master.attributes("-disabled", 0), self.root.destroy()])
        self.root.title(title)
        self.root.transient(master=self.master)
        self.root.geometry(f"{self.width}x{self.height}")

        button = tkinter.Button(text=apply_label, master=self.root, command=self.apply_data)
        button.place(x=0, rely=(1 - self.down), relwidth=1)

    
    def initcards(self):
        self.cards = ttk.Notebook(master=self.root)
        self.cards.place(x=0, y=0, relwidth=1, relheight=(1 - self.down))
    
    
    def addsoncard(self, label="default label"):
        frame = tkinter.Frame(master=self.root)
        self.cards.add(frame, text=label)
        self.soncards[label] = frame
        

    def write(self, var, index="default label", label="default label"):
        mer = self.soncards[index] if self.cards else self.root  
        
        label = tkinter.Label(master=mer, text=label)
        label.grid(row=self.row, column=self.column)

        entry = tkinter.Entry(master=mer, width=20)
        entry.insert(0, var[0])
        entry.grid(row=self.row, column=self.column + 1)

        self.table.append((var, entry.get))
        
        self.row += 1


    def choose(self, var, choses=["default label 1", "default label 2"], index="default label", label="default label"):
        mer = self.soncards[index] if self.cards else self.root  
        
        label = tkinter.Label(master=mer, text=label)
        label.grid(row=self.row, column=self.column)

        if not var[0] in choses:  choses.append(var[0])
        intvar = tkinter.StringVar()
        intvar.set(var[0])

        n = 0
        for i in choses:
            n += 1
            
            rb = tkinter.Radiobutton(master=mer, text=i, variable=intvar, value=i)
            rb.grid(row=self.row, column = self.column + n)
        
        self.table.append((var, intvar.get))
        
        self.row += 1
        

    def apply_data(self):
         for i in self.table:
             v, g = i
             v[0] = g()
    

    def loop(self):
        self.root.wait_window()
    

def setting(root):
    cfg = config(master=root, title="设置", apply_label="应用")

    a, b, c, d, e, f, g = [[0]] * 7 

    cfg.initcards()
    for i in range(5):
        index = f"选项卡{i}"
        cfg.addsoncard(index)
        for l in range(5):
            cfg.write(var=a, label=f"数据{l}", index=index)
        for l in range(5):
            cfg.choose(var=a, label=f"数据{l}", index=index)


def main():
    root = tkinter.Tk()
    root.title("config test")

    label = tkinter.Label(master=root, text="按下按钮进行设置")
    label.pack()

    button = tkinter.Button(master=root, text="设置", command=lambda : setting(root))
    button.pack()

    root.mainloop()


if __name__ == "__main__":
    main()    
