from tkinter import * # Inportamos el modulo de Tkinter para crear ventanas de escritorio.
from tkinter import messagebox # Inportamos de Tkinter el modulo messagebox para utilizar mensajes dinamicos.
from baseDatos import *

# Variables de configuracion de la ventana
alto = 560
ancho = 620
posx = 400
posy = 400
anchoAlto = str(ancho)+"x"+str(alto)
posicionX = "+"+str(posx)
posiciony = "+"+str(posy)
colorVentana = "blue"
colorFondo = "blue"
colorLetra = "white"


def mostrarMensaje(titulo, mensaje):
    messagebox.showinfo(titulo,mensaje)

# Utilizamos un metodo paras limpiar las cajas de input.
def limpiarDatos():
    nombre.set("")
    apellido.set("")
    telefono.set("")
    email.set("")
    ID.set("")
    text.delete(1.0,END)

# Creamos el metodo para incertar datos. 
def guardarDatos():
    crearTabla()
    if((nombre.get() == "") or (apellido.get() == "")):
        mostrarMensaje("Datos vacios", "Debes rellenar todos los datos")
    else:
        datos = nombre.get(), apellido.get(), telefono.get(), email.get()
        mostrarMensaje("Guardar","Contacto guardado") 
        insertar(datos)
        limpiarDatos()

# Creamos el metodo para actulizar datos. 
def actualizar():
    crearTabla()
    if(ID.get() == "") or (ID.get() == 0) or (nombre.get() == ""):
        mostrarMensaje("Error","Debes rellenar los datos")
    else:
        try:
            modificar(ID.get(),nombre.get(),apellido.get(),telefono.get(),email.get())
            mostrarMensaje("Modificar","Contacto modificado")
            limpiarDatos()
            mostrar()
        except:
            mostrarMensaje("Error","ID no encontrado")
            
# Creamos el metodo para eliminar datos.            
def eliminar():
    if(ID.get() == "") or (ID.get() == 0):
        mostrarMensaje("Error","Debes insertar un identificador 'ID'")
    else:
        try:
            borrar(ID.get())
            mostrarMensaje("Borrar","Contacto borrado")
            limpiarDatos()
            mostrar()
        except:
            mostrarMensaje("Error","ID no encontrado")

# Creamos el metodo para mostra datos. 
def mostrar():
    listado = consultar()    
    text.delete(1.0,END)
    text.insert(INSERT,"id\tNombre\tApellido\t\ttelefono\t\tEmail\n")
    for elemento in listado:
        id = elemento[0]
        nombre = elemento[1]
        apellido = elemento[2]
        telefono = elemento[3]
        email = elemento[4]
        text.insert(INSERT, id)
        text.insert(INSERT, "\t")
        text.insert(INSERT, nombre)
        text.insert(INSERT, "\t")
        text.insert(INSERT, apellido)
        text.insert(INSERT, "\t\t")
        text.insert(INSERT, telefono)
        text.insert(INSERT, "\t\t")
        text.insert(INSERT, email)
        text.insert(INSERT, "\n")

# Creamos el metodo para buscar datos. 
def buscar():
    if((ID.get()=="") or (ID.get()==0)):
        mostrarMensaje("Error","Debes insertar un identificador 'ID'")
        
    else:
        contactos = contactoId(ID.get())
        for contacto in contactos:
            ID.set(contacto[0])
            nombre.set(contacto[1])
            apellido.set(contacto[2])
            telefono.set(contacto[3])
            email.set(contacto[4])
        mostrarMensaje("Buscar","Contacto encontrado")
        
# ventana
ventana = Tk()
ventana.config(bg=colorVentana)
ventana.geometry(anchoAlto+posicionX+posiciony)
ventana.title("Agenda")
# marco dentro de la ventana
frame = Frame()
frame.config(width=ancho,height=alto)
frame.config(bg=colorVentana)
frame.pack()
# variables de entrada
ID = IntVar()
nombre = StringVar()
apellido = StringVar()
telefono = StringVar()
email = StringVar()
contacto = StringVar()
# widgets
etiquetaID = Label(frame,text="ID: ").place(x=50,y=50)
cajaID = Entry(frame,textvariable=ID).place(x=130,y=50)
etiquetaNombre = Label(frame,text="Nombre: ").place(x=50,y=90)
cajaNombre = Entry(frame,textvariable=nombre).place(x=130,y=90)
etiquetaApellido = Label(frame,text="Apellido: ").place(x=50,y=130)
cajaApellido = Entry(frame,textvariable=apellido).place(x=130,y=130)
etiquetaTelefono = Label(frame,text="Telefono: ").place(x=50,y=170)
cajaTelefono = Entry(frame,textvariable=telefono).place(x=130,y=170)
etiquetaEmail = Label(frame,text="Email: ").place(x=50,y=210)
cajaEmail = Entry(frame,textvariable=email).place(x=130,y=210)
text= Text(frame) #caja de texto
text.place(x=50, y=240, width=540,height=200) # posicion y medidas interiores. 
botonAñadir = Button(frame,text="Añadir", command=guardarDatos).place(x=150,y=500)
botonborrar = Button(frame,text="Borrar", command=eliminar).place(x=200,y=500)
botonConsultar = Button(frame, text="Consultar", command=mostrar).place(x=250,y=500)
botonModificar = Button(frame, text="Actualizar", command=actualizar).place(x=320,y=500)
botonBuscar = Button(frame, text="Buscar", command=buscar).place(x=390,y=500)
# al final de todo
ventana.mainloop()