from tkinter import *
from tkinter import filedialog as FileDialog
from io import open
ruta = ""

def new_file():
    global ruta
    mensaje.set("New File")
    ruta= ""
    texto.delete(1.0, END)
    root.title("Notepad")

def open_file():
    global ruta
    mensaje.set("Open File")
    ruta = FileDialog.askopenfilename(initialdir = ".", filetype = (("Text File", "*.txt"),), title = "Open Text File")
    
    if ruta != "":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.delete(1.0, END)
        texto.insert('insert', contenido)
        fichero.close()
        root.title(ruta + " - Notepad")
        
def save_file():
    global ruta
    if ruta != "":
        contenido = texto.get(1.0, "end-1c" )
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("File Saved Successfully")
    else:
        save_as()

def save_as():
    global ruta
    # mensaje.set("Save as")
    fichero = FileDialog.asksaveasfile(title = "Save As", mode = "w", defaultextension = ".txt")
    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0, "end-1c" )
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("File Saved Successfully")
    else:
        mensaje.set("Saved Failed")
        ruta = ""

root = Tk()
root.title("Notepad")

# Menu
menubar = Menu(root)
filemenu = Menu(menubar, tearoff = 0)

filemenu.add_command(label="New", command = new_file)
filemenu.add_command(label="Open", command = open_file)
filemenu.add_command(label="Save", command = save_file)
filemenu.add_command(label="Save as", command = save_as)
filemenu.add_separator()
filemenu.add_command(label="Quit", command = root.quit)

menubar.add_cascade(menu = filemenu, label = "File")
                
# Caja de texto
texto = Text(root)
texto.pack(fill = "both", expand = 1)
texto.config(bd = 0, padx = 6, pady = 4, font = ("Consolas", 12), bg="#19232D", foreground="#06DE19")

#
mensaje = StringVar()
mensaje.set("Welcome")

monitor = Label(root, textvar = mensaje, justify = 'left')
monitor.pack(side = "left")



root.config(menu = menubar)
# Ejecucuion de la aplicacion
root.mainloop()
