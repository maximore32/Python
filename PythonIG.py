from tkinter import*
from tkinter import messagebox
import sqlite3 

#-------------------------Funciones---------------------------------------------------------------------#

def conexionBBDD():

    miconexion=sqlite3.connect("Max.db")
    
    micursor=miconexion.cursor()

    try:
         
         micursor.execute("""
         CREATE TABLE DATOSUSUARIO (
         ID INTEGER PRIMARY KEY AUTOINCREMENT,
         NOMBRE_USUARIO VARCHAR(50),
         APELLIDO VARCHAR(50),
         PASSWORD VARCHAR(50),
         DIRECCION VARCHAR(50),
         COMENTARIO VARCHAR(150))""")
                  
         messagebox.showinfo("BBDD","BBDD creada con exito!")
         miconexion.commit()
         
         miconexion.close()

    except:
        messagebox.showwarning("¡Atención!", "La BBDD ya existe.")



def Saliapp():
    consulta=messagebox.askquestion("Salir","¿Desea salir del programa?")
    if consulta=="yes":
        root.destroy()


def Limpiarcampos():
    miID.set("")
    miNombre.set("")
    miApellido.set("")
    miPass.set("")
    TextoComentario.delete(1.0, END)


def Creacion():
    miconexion=sqlite3.connect("Max.db")
    micursor=miconexion.cursor()
    misdatos=miID.get(),miNombre.get(),miApellido.get(),miPass.get(),miDireccion.get()
    try:

       micursor.execute('''
       INSERT INTO DATOSUSUARIO VALUES(NULL,?,?,?,?,?)''',(misdatos))
       miconexion.commit()
       miconexion.close()
       messagebox.showinfo("Informacíon","Registro creado con éxito!")

    except:
        messagebox.showwarning("Atención","Error al recopilar datos..")


def LeerFichero():
    miconexion=sqlite3.connect("Max.db")    
    micursor=miconexion.cursor()

    micursor.execute("SELECT * FROM DATOSUSUARIO WHERE ID="+ miID.get())
    Usuario=micursor.fetchall()

    for usuario in Usuario:
        miID.set(usuario[0])
        miNombre.set(usuario[1])
        miApellido.set(usuario[2])
        miPass.set(usuario[3])
        miDireccion.set(usuario[4])
        TextoComentario.insert(1.0, usuario[5])


def avisoLicencia():
        messagebox.showinfo("Licencia", "Producto bajo Licencia apache")


def Actualizacion():
    miconexion=sqlite3.connect("Max.db")    
    micursor=miconexion.cursor()

    misdatos=miID.get(),miNombre.get(),miApellido.get(),miPass.get(),miDireccion.get()

    try:

      micursor.execute('''UPDATE DATOSUSUARIO SET ID=?,NOMBRE_USUARIO=?,
                                PASSWORD=?,
                                APELLIDO=?,
                                DIRECCION=?,
                                COMENTARIO=? '''+ "WHERE ID="+miID.get(),(misdatos))
      miconexion.commit()
      miconexion.close()
      messagebox.showwarning("Actualización","Actualización realizada con éxito!")
            
    except:
       messagebox.showwarning("Atencion","Error en la actualización..")




#-----------------------------------Inicio de interfaz-----------------------------------------#

root=Tk()
root.title("Game Zone")
root.iconbitmap("dragon.ico")
root.resizable(True,False)
root.geometry("350x430")
root.config(bg="darkorange")


BarraMenu=Menu(root)
root.config(menu=BarraMenu, width=300, height=300)

bdMenu=Menu(BarraMenu, tearoff=0)
bdMenu.add_command(label="Conectar",command=conexionBBDD)
bdMenu.add_command(label="Salir", command=Saliapp)

borrarMenu=Menu(BarraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar", command=Limpiarcampos)

crudMenu=Menu(BarraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=Creacion)
crudMenu.add_command(label="Leer", command=LeerFichero)
crudMenu.add_command(label="Actualizar", command=Actualizacion)


ayudaMenu=Menu(BarraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de..", command= avisoLicencia)

BarraMenu.add_cascade(label="BBDD", menu=bdMenu)
BarraMenu.add_cascade(label="Borrar", menu=borrarMenu)
BarraMenu.add_cascade(label="CRUD", menu=crudMenu)
BarraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

#--------------------------inicio de campos-----------------------------------------#

iFrame=Frame(root)
iFrame.pack()


miID=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()

marcoID=Entry(iFrame,textvariable=miID)
marcoID.grid(row=0, column=1, padx=10, pady=10)

marcoNombre=Entry(iFrame, textvariable=miNombre)
marcoNombre.grid(row=1, column=1, padx=10, pady=10)
marcoNombre.config(justify="right")

marcoApellido=Entry(iFrame, textvariable=miApellido)
marcoApellido.grid(row=2, column=1, padx=10, pady=10)

marcoPass=Entry(iFrame, textvariable=miPass)
marcoPass.grid(row=3, column=1, padx=10, pady=10)
marcoPass.config(show="*", fg="red")

marcoDireccion=Entry(iFrame, textvariable=miDireccion)
marcoDireccion.grid(row=4, column=1, padx=10, pady=10)

TextoComentario=Text(iFrame, width=15, height=5)
TextoComentario.grid(row=5, column=1, pady=10, padx=10)
Scroll=Scrollbar(iFrame, command=TextoComentario.yview)
Scroll.grid(row=5, column=2, sticky=NSEW)

TextoComentario.config(yscrollcommand=Scroll.set)


#-------------------------Inicio de Label-----------------------------------------------------#

idLabel=Label(iFrame, text="ID:")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel=Label(iFrame, text="Nombre:")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(iFrame, text="Apellido:")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(iFrame, text="Password:")
passLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direcLabel=Label(iFrame, text="Direccion:")
direcLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentLabel=Label(iFrame, text="Comentario:")
comentLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

#------------------------Botones---------------------------------------------------------#

iFrame2=Frame(root)
iFrame2.pack()

botonCrear=Button(iFrame2, text="Create", command=Creacion)
botonCrear.grid(row=0, column=0, pady=10, padx=10, sticky="e")

botonBorrar=Button(iFrame2, text="Delete" ,command=Limpiarcampos)
botonBorrar.grid(row=0, column=1, pady=10, padx=10,sticky="e")

botonActualizar=Button(iFrame2, text="Update")
botonActualizar.grid(row=0, column=2, pady=10, padx=10, sticky="e")

botonLeer=Button(iFrame2, text="Read" , command=LeerFichero)
botonLeer.grid(row=0, column=2, pady=10, padx=10, sticky="e")


root.mainloop()
