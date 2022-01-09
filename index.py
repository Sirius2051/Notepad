from tkinter import *
from tkinter import filedialog as FileDialog
from io import open

class Notepad:
    def __init__(self):
        self.path = ""
        
        self.root = Tk()
        self.root.title("Notepad")

        self.menubar = Menu(self.root)
        self.filemenu = Menu(self.menubar, tearoff = 0)

        self.filemenu.add_command(label="New", command = self.NewFile )
        self.filemenu.add_command(label="Open", command = self.OpenFile)
        self.filemenu.add_command(label="Save", command = self.SaveFile)
        self.filemenu.add_command(label="Save as", command = self.SaveAs)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Quit", command = self.root.quit)

        self.menubar.add_cascade(menu = self.filemenu, label = "File")

        self.text = Text(self.root)
        self.text.pack(fill = "both", expand = 1)
        self.text.config(bd = 0, padx = 6, pady = 4, font = ("Consolas", 12), bg="#19232D", foreground="#06DE19")

        self.message = StringVar()
        self.message.set("Welcome")

        self.display = Label(self.root, textvar = self.message, justify = 'left')
        self.display.pack(side = "left")

        self.root.config(menu = self.menubar)
        
        self.root.mainloop()
    
    def NewFile(self):
        self.message.set("New File")
        self.path = ""
        self.text.delete(1.0, END)
        self.root.title("Notepad")
    
    def OpenFile(self):
        self.message.set("Open File")
        self.path = FileDialog.askopenfilename(initialdir = ".", filetype = (("Text File", "*.txt"),), title = "Open Text File")
        
        if self.path != "":
            file = open(self.path, 'r')
            content = file.read()
            self.text.delete(1.0, "end-1c")
            self.text.insert('insert', content)
            file.close()
            self.root.title(self.path + " - Notepad")
    
    def SaveFile(self):
        if self.path != "":
            content = self.text.get(1.0, "end-1c" )
            file = open(self.path, 'w+')
            file.write(content)
            file.close()
            self.message.set("File Saved Successfully")
        else:
            self.SaveAs()
    
    def SaveAs(self):
        file = FileDialog.asksaveasfile(title = "Save As", mode = "w", defaultextension = ".txt")
        if file is not None:
            self.path = file.name
            content = self.text.get(1.0, "end-1c" )
            file = open(self.path, 'w+')
            file.write(content)
            file.close()
            self.message.set("File Saved Successfully")
        else:
            self.message.set("Saved Failed")
            self.path = ""

notepad = Notepad()