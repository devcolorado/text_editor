import tkinter as tk
from tkinter import filedialog
 
# Declaramos la variable global como un string vacio para posteriormente 
# guardar la ruta donde estará un archivo
ruta = ""

def nuevo():
    """Borra todo el texto del cuadro
       y vacia la ruta"""
    
    # Borramos el texto de la pantalla
    cuadro_texto.delete("1.0","end")

    # Llamamos a la variable global y la vaciamos
    global ruta 
    ruta = ""

def guardar():
    """Guarda el contenido del archivo actual,
       si este no existe, se llama a guardar_como
       para crear un nuevo archivo """
    
    # Llamamos a la variable global
    global ruta 

    # Comprobamos si existe alguna ruta guardada en la variable "ruta"
    if ruta != "":

        # Si ya hay una ruta guardada, abrimos el archivo y lo editamos 
        # para que guarde los cambios actuales
        archivo = open(ruta,"w+")
        texto = cuadro_texto.get("1.0","end")
        archivo.write(texto)
    else:
        # En caso contrario creamos un nuevo archivo con la funcion
        #"guardar_como"
        guardar_como()

def guardar_como():
    """Guarda el texto en un archivo dentro de la carpeta actual
       asi como la ruta de este"""
    
    # Llamamos a la funcion global y le asignamos la ruta con la 
    # que guardaremos el archivo
    global ruta
    archivo = filedialog.asksaveasfile(title="Guardar como",mode="w+",defaultextension=".txt")
    ruta = archivo.name

    if archivo is not None:
        # Comprobamos si se le a asiganado un nombre al archivo
        # si es asi, proseguimos
        texto = cuadro_texto.get("1.0","end")
        archivo.write(texto)

def abrir_archivo():
    """Busca los archivo en formato txt para
       despues abrirlo en la interfaz de texto"""
    archivo = filedialog.askopenfile(mode="r", filetypes=[("Archivos de texto", "*.txt"),("Archivos","*.*")])
   
    # llamamos a la variable global y se asignamos la ruta del archivo
    global ruta
    ruta = archivo.name
    contenido = archivo.read()
        
    # Borrarmos el contenido actual de la interfaz de texto
    # e insertamos el contenido del archivo
    cuadro_texto.delete("1.0","end") 
    cuadro_texto.insert("1.0",contenido) 

# Creamos la ventana principal
root = tk.Tk()
# Le indicamos el titulo asi como las dimensiones de esta
root.title("Editor de texto")
root.geometry("600x600")
# Creamos una barra de menú 
menuBar = tk.Menu(root)
# la insertamos en nuestra ventana principal 
root.config(menu=menuBar)

# Creamos un witget de cuadro de texto
cuadro_texto = tk.Text(root)
# Le indicamos que al witget que se expanda a lo largo y ancho de la ventana
cuadro_texto.pack(expand=True,fill="both")
# Cambiamos el tipo de letra y agregamos un relleno a lo largo y ancho
cuadro_texto.config(font="Arial 10",padx=10,pady=10)
# enfocamos el cuadro de texto para poder escribir apenas se inicie el programa
cuadro_texto.focus()

# Creamos un menú en nuestra barra de menú con "tearoff=false"
# para evitar que el menú se pueda desgarrar
archivoMenu = tk.Menu(menuBar,tearoff=0)

# Añadimos una barra desplegable al menú "archivoMenu" 
menuBar.add_cascade(label="Archivo",menu=archivoMenu)

# Añadimos los diferentes botones del menú con sus respectivas funciones 
archivoMenu.add_command(label="Nuevo",command=nuevo)
archivoMenu.add_command(label="Abrir",command=abrir_archivo)
archivoMenu.add_command(label="Guardar",command=guardar)
archivoMenu.add_command(label="Guardar como",command=guardar_como)
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir",command=root.quit)


root.mainloop()