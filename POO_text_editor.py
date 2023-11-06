import tkinter as tk
from tkinter import filedialog

class editort(tk.Tk):
    def __init__(self):
        super().__init__()

        self.ruta = ""
        
        self.geometry("600x600")
        self.resizable(0,0)
        self.title("Editor de texto")
        self.crear_widgets()



    def crear_widgets(self):
        """Crea todos los widgets"""
        barra_menu = tk.Menu(self)
        self.config(menu=barra_menu)

        archivo_menu = tk.Menu(barra_menu,tearoff=0)
        barra_menu.add_cascade(label="Archivo",menu=archivo_menu)

        archivo_menu.add_command(label="Nuevo",command=self.nuevo_archivo)
        archivo_menu.add_command(label="Abrir",command=self.abrir_archivo)
        archivo_menu.add_command(label="Guardar",command=self.guardar_archivo)
        archivo_menu.add_command(label="Guardar como",command=self.guardar_como)
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Salir",command=self.quit)

        self.cuadroT = tk.Text(self)
        self.cuadroT.pack(expand=True,fill="both")
        self.cuadroT.config(font="Arial 12",padx=10,pady=10)
        self.cuadroT.focus()
        

    def nuevo_archivo(self):
        """Crea un documento vacio"""
        self.cuadroT.delete("1.0","end")    
        self.title("Editor de texto")
        self.ruta = ""

    def abrir_archivo(self):
        """Muestra el contenido de un archivo txt"""
        archivo = filedialog.askopenfile(initialdir=".",filetypes=[("Archivo de texto","*.txt")],title="Abrir archivo")
        self.ruta = archivo.name
        
        contenido = archivo.read()
        self.cuadroT.delete("1.0","end")
        self.cuadroT.insert("1.0",contenido)
    
    def guardar_archivo(self):
        """Guarda la edicion de un archivo y en caso
           de que el archivo no exista, redirecciona a 
            'guardar_como' para crearlo"""
        if self.ruta != "":
            contenido = self.cuadroT.get("1.0","end")
            archivo = open(self.ruta,"w+")
            archivo.write(contenido)
        else:
            self.guardar_como()
    
    def guardar_como(self):
        """Guarda el texto como un archivo .txt"""
        archivo = filedialog.asksaveasfile(title="Guardar como",mode="w+",defaultextension=".txt")
        self.ruta = archivo.name
        contenido = self.cuadroT.get("1.0","end")
        archivo.write(contenido)


if __name__ == "__main__":
    aplicacion = editort()
    aplicacion.mainloop()