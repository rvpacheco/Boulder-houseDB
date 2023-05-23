import pyodbc
from tkinter import ttk
from main import *
from tkinter import *




# funciones
primero = Tk()
primero.title("Boulder house")
primero.geometry("600x500")

UID = StringVar()
PWD = StringVar





#db = database()


marc = LabelFrame(primero, text="Base de datos de gimnasio de escalada")
marc.place(x=50, y=50, width=500, height=400)

# labels y entrys
lblUID = Label(marc, text="Usuario").grid(column=0, row=0)
txtUID = Entry(marc, textvariable=UID)
txtUID.grid(column=1, row=0)

lblPWD = Label(marc, text="Contraseña").grid(column=0, row=1)
txtPWD = Entry(marc, textvariable=PWD)
txtPWD.grid(column=1, row=1)
txtPWD.config(show="*")



# funciones
def confirmar():
    lblMensaje = Label(marc, text="El ingreso a sido exitoso", fg="green").grid(column=0, row=2, columnspan=4)



def entradas():
    ventana = Tk.winfo_toplevel(primero)
    ventana.title("Base de datos gimnasio")
    ventana.geometry("600x500")

    nombre = StringVar()
    apellido = StringVar()
    email = StringVar()
    CLIMB_ID = StringVar()
    db = database()

    marco = LabelFrame(ventana, text="Formulario escalador")
    marco.place(x=50, y=50, width=500, height=400)

    # labels y entrys

    lblNombre = Label(marco, text="nombre").grid(column=0, row=0, padx=5, pady=5)
    txtNombre = Entry(marco, textvariable=nombre)
    txtNombre.grid(column=1, row=0)

    lblApellido = Label(marco, text="Apellido").grid(column=0, row=1, padx=5, pady=5)
    txtApellido = Entry(marco, textvariable=apellido)
    txtApellido.grid(column=1, row=1)

    lblemail = Label(marco, text="email").grid(column=2, row=0, padx=5, pady=5)
    txtemail = Entry(marco, textvariable=email)
    txtemail.grid(column=3, row=0)

    lblclimb_Id = Label(marco, text="climb_Id").grid(column=2, row=1, padx=5, pady=5)
    txtclimb_Id = Entry(marco, textvariable=CLIMB_ID)
    txtclimb_Id.grid(column=3, row=1)

    lblMensaje = Label(marco, text="Aqui van los mensaje", fg="green")
    lblMensaje.grid(column=0, row=2, columnspan=4)

    # tabla

    tvEscalador = ttk.Treeview(marco)
    tvEscalador.grid(column=0, row=3, columnspan=4)
    tvEscalador["columns"] = ( "climb_Id","email", "nombre", "apellido")
    tvEscalador.column("#0", width=0, stretch=NO)
    tvEscalador.column("climb_Id", width=100, anchor=CENTER)
    tvEscalador.column("nombre", width=100, anchor=CENTER)
    tvEscalador.column("apellido", width=100, anchor=CENTER)
    tvEscalador.column("email", width=100, anchor=CENTER)

    tvEscalador.heading("#0", text="")
    tvEscalador.heading("climb_Id", text="climb_Id", anchor=CENTER)
    tvEscalador.heading("email", text="email", anchor=CENTER)
    tvEscalador.heading("apellido", text="apellido", anchor=CENTER)
    tvEscalador.heading("nombre", text="nombre", anchor=CENTER)


    # botones
    btnEliminar = Button(marco, text="eliminar", command=lambda: eliminar())
    btnEliminar.grid(column=1, row=4)
    btnNuevo = Button(marco, text="nuevo", command=lambda: nuevo())
    btnNuevo.grid(column=2, row=4)
    #btnActualizar = Button(marco, text="actualizar", command=lambda: actualizar())
    #btnActualizar.grid(column=3, row=4)


    def llenar():
        vaciar()
        sql = "select * from climber"
        db.cursor.execute(sql)
        filas = db.cursor.fetchall()
        for fila in filas:
            CLIMB_ID = fila[0]
            tvEscalador.insert("", END, CLIMB_ID, text=CLIMB_ID, values=fila)

    def validar():
        return len(CLIMB_ID.get()) and len(nombre.get()) and len(email.get()) and len(apellido.get())


    def limpiar():
        CLIMB_ID.set("")
        email.set("")
        nombre.set("")
        apellido.set("")
    def vaciar():
        filas = tvEscalador.get_children()
        for fila in filas:
            tvEscalador.delete(fila)


    def eliminar():
        CLIMB_ID = tvEscalador.selection()[0]
        if int(CLIMB_ID)>0:
            sql = "delete from Climber where CLIMB_ID= "+CLIMB_ID
            db.cursor.execute(sql)

            tvEscalador.delete(CLIMB_ID)
        else:
            lblMensaje.config(text="Se a eliminado el registro completamente")
        db.connection.commit()

    def nuevo():
        if validar():

            val= (CLIMB_ID.get(), email.get(), nombre.get(), apellido.get())
            sql="insert into Climber values (?,?,?,?)"
            db.cursor.execute(sql, val)
            db.connection.commit()
            lblMensaje.config(text="Se guardo un registro correctamente", fg="green")
            llenar()
            limpiar()

        else:
            lblMensaje.config(text="Los campos no deben estar vacios", fg="red")
    def actualizar():
        pass


    llenar()
    ventana.mainloop()

btnConfirmar = Button(marc, text="Confirmar", command=entradas)

btnConfirmar.grid(column=1, row=4)
primero.mainloop()
