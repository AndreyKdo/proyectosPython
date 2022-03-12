#Elaborado por Sara Segura, Andrey Picado
#Fecha de creación: 31/07/2020 11:50am
#Ultima modificación: 05/08/2020
#Versión: 3.8.5
#-$-$-$-$-$-$-$-$-$-$-Módulo con las funciones de la interfaz-$-$-$-$-$-$-$-$-$-$-#
#Importación de librerías
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from funciones import *
from clase import *
#-*-*-*-*-*-*-*-*-*Verificación del archivo-*-*-*-*-*-*-*-*-*#
nombreArchivo = "archivoRegistro.dat"
ref = verificarArchivo(nombreArchivo)#verificar la existencia del archivo
if type(ref)==bool:
    listaRegistros = []#lista de registros vacía
else:
    listaRegistros = ref#cargar los elementos ya guardados
#-*-*-*-*-*-*-*-*-*Definición de Funciones por ventana-*-*-*-*-*-*-*-*-*#
##################Configuración de la ventana Certificado########################
def ventanaCertificado():
    """
    F: muestra la ventana para realizar el certificado de nacimiento de un usuario
    E:-
    S: creación del html y xml según la persona encontrado
    """
    vCertificado = tk.Tk()
    ancho,alto= 600,320
    color = "#FFFFFF" 
    anchoPantalla= vCertificado.winfo_screenwidth()
    largoPantalla= vCertificado.winfo_screenheight()
    posVentanaX= int((anchoPantalla/2)-(ancho/2))
    posVentanaY= int((largoPantalla/2)-(alto/2))
    vCertificado.overrideredirect(1)
    vCertificado.geometry("{}x{}+{}+{}".format(ancho,alto,posVentanaX,posVentanaY))
    vCertificado.resizable(width=False, height=False)#Bloquea para que no se pueda cambia el tamaño de la vRegistrar
    vCertificado.config(bg="#cb3234",bd=3)#Le pone color a la vRegistrar
    framePrin=tk.Frame(vCertificado,width=ancho, height=alto)
    framePrin.pack(fill='both')
    framePrin.config(bg=color)
    framePrin.config(bd=15)
    ftitulo = tk.Frame(master=framePrin,width=ancho,height=100,bg=color)
    ftitulo.pack()
    fFormulario = tk.Frame(master=framePrin,bg=color)
    fFormulario.pack()
    fbtn = tk.Frame(master=framePrin,bg=color)
    fbtn.pack()
    lTitulo=tk.Label(ftitulo, text="Certificado de Nacimiento", bg=color, fg="#000000", font=("Times New Roman", 24))
    lTitulo.place(x=ancho/5,y=0)
    lSub=tk.Label(ftitulo, text="Digite una cédula a buscar:", bg=color, fg="#000000", font=("Times New Roman", 16))
    lSub.place(x=ancho/5,y=70)
    provincia = tk.StringVar()#número de provincia
    tomo = tk.StringVar()
    asiento = tk.StringVar()
    def limpiar():
        """
        F: elimina la información que poseen las variables de control de los entrys de certificado
        Sin entradas ni salidas, solo la llamada
        """
        provincia.set("")#número de provincia
        tomo.set("")
        asiento.set("")
        return ""
    def limitador(widget,entryTexto,num):
        """
        Se encarga de delimitar el número de caracteres del entry Cita.
        E: entryTexto(texto del entry string) num(número de caracteres int)
        S: return
        """
        if len(entryTexto.get()) == num:
            widget.tk_focusNext().focus() #línea para cambiar de entry automáticamente
        if len(entryTexto.get()) > 0:
            if re.search("\D$",entryTexto.get()):#Valida que no contenga letras(o que digite algo distinto a dígitos)
                entryTexto.set(entryTexto.get()[:-1])#setea el entry hasta donde no hay letras
            #donde esta el :num se limita la cantidad d caracteres
            elif num == 1:#si es 1 está poniendo el número de provincia en la cita
                if re.search("0$",entryTexto.get()):#valida que no sea 0
                    entryTexto.set(entryTexto.get()[:-1])#setea el entry hasta donde no hay letras
                else:
                    entryTexto.set(entryTexto.get()[-1])#al texto le asigna el último número ingresado
            else:
                entryTexto.set(entryTexto.get()[:num])
            return ""
    def regresar():
        'Funcionalidad: Destruye la ventana actual y vuelve al menú'
        vCertificado.destroy()
        ventanaMenu()
    def definirSexo(psexo):
        """
        Se encarga de definir el sexo según el caracter recibido entre M ó F (solo debe recibir uno de estos)
        psexo(string): caracter M o F
        Salidas: Masculino si el caracter es M, Femenino si el caracter es F
        """
        if psexo=="M":
            return "Masculino"
        return "Femenino"
    def crearXml(datos):
        """
        F: se encarga de crear el archivo XML en base a los datos recibidos
        E: datos(objeto) objeto Persona del cual realizar el archivo
        S: archivo xml creado en el directorio actual       
        """
        #El archivo se guarda como "Certificado de Nacimiento 1-1111-1111".xml (según la cédula)
        archivoXML = open("Certificado de Nacimiento "+datos.obtenerCedula()+".xml","w",encoding="UTF-8")
        #contenido del xml:
        mensaje="""<?xml version="1.0" encoding='UTF-8'?>
        <certificado>
            <titulo>Certificado de Nacimiento</titulo>
            <tomo>"""+datos.obtenerCedula()[2:6]+"""</tomo>
            <asiento>"""+datos.obtenerCedula()[7:]+"""</asiento>
            <cita>"""+datos.obtenerCedula()+"""</cita>
            <nombre>"""+datos.obtenerNombre()+"""</nombre>
            <sexo>"""+definirSexo(datos.obtenerSexo())+"""</sexo>
            <ubicacion>"""+datos.obtenerUbicacion()+"""</ubicacion>
            <dia>"""+datos.obtenerFechaN()+"""</dia>
            <padre>"""+datos.obtenerPadre()+"""
                <nacionalidad>"""+datos.obtenerNacionalidadP()+"""</nacionalidad>
            </padre>
            <madre>"""+datos.obtenerMadre()+"""
                <nacionalidad>"""+datos.obtenerNacionalidadM()+"""</nacionalidad>
            </madre>
        </certificado>
        """
        archivoXML.write(mensaje)#escribe el contenido del xml
        archivoXML.close()
        return ""
    def crearHtml(persona):
        """Funcionalidad: Crea el archivo html con toda la información y la inserta en una tabla
        Entradas: persona (objeto) a mostrar
        Salidas: Crea un archivo"""
        html=open('HTML Certificado de nacimiento'+ str(persona.obtenerCedula())+ persona.obtenerNombre()+'.html','w')
        mensaje='''
        <!DOCTYPE html>
        <html lang='es'>
        <head>
          <meta http-equiv="Content-Type" content="text/html; charset="utf-8"/>
          <title>Certificado de nacimiento</title>
        <style>
        table, th, td {
          border: 1px solid black;
          border-collapse: collapse;  
          margin: auto;
          width: 600px
        }
        th, td,tr {
          padding: 5px;
        }
        h4{
          font-weight: bold;
          text-align: center;
        }
        </style>
        </head>
        <body>
            <table>
                <tr>
                  <th colspan="2">
                    <h2> <span>Certificado de Nacimiento</span></h2>
                  </th>
                </tr>
                <tr>
                    <td>
                        <h4>Al tomo</h4>
                    </td>
                      <td>
                          <p>'''
        mensaje+= persona.obtenerCedula()[2:6]+'''</p>
                      </td>
                <tr>
                    <td>
                        <h4>Asiento</h4>
                  </td>
                  <td>
                      <p>'''+persona.obtenerCedula()[7:]+'''</p>
                  </td>
                </tr>
                <tr>
                    <td>
                        <h4>Cita:</h4>
                  </td>
                  <td>
                      <p>'''+persona.obtenerCedula()+'''</p>
                  </td>
                </tr>
                <tr>
                    <td>
                        <h4>Dice que:</h4>
                  </td>
                  <td>
                      <p>'''+persona.obtenerNombre()+'''</p>
                  </td>
                </tr>
                <tr>
                    <td>
                        <h4>Sexo:</h4>
                  </td>
                  <td>
                      <p>'''+definirSexo(persona.obtenerSexo())+'''</p>
                  </td>
                </tr>
                <tr>
                    <td>
                        <h4>Nació en:</h4>
                  </td>
                  <td>
                      <p>'''+persona.obtenerUbicacion()+'''</p>
                  </td>
                </tr>
                <tr>
                    <td>
                        <h4>El día:</h4>
                  </td>
                  <td>
                      <p>'''+persona.obtenerFechaN()+'''</p>
                  </td>
                </tr>
                <tr>
                    <td>
                        <h4>Padre:</h4>
                  </td>
                  <td>
                      <p>'''+persona.obtenerPadre()+'''</p>
                  </td>
                </tr>
                <tr>
                    <td>
                        <h4>Nacionalidad:</h4>
                  </td>
                  <td>
                      <p>'''+persona.obtenerNacionalidadP()+'''</p>
                  </td>
                </tr>
                <tr>
                    <td>
                        <h4>Madre:</h4>
                  </td>
                  <td>
                      <p>'''+persona.obtenerMadre()+'''</p>
                  </td>
                </tr>
                <tr>
                    <td>
                        <h4>Nacionalidad:</h4>
                  </td>
                  <td>
                      <p>'''+persona.obtenerNacionalidadM()+'''</p>
                  </td>
                </tr>
            </table>
        </body>
        </html>'''
        html.write(mensaje)#escribe todo el codigo en un archivo tipo html
        html.close()   
    def verificarCedula(pcedula):
        """
        F: verifica que la cédula ingresada esté en el archivo de registro
        E: pcedula(string) unión de los entry que conforman las partes de la cédula
        S: objeto(booleano u objeto encontrado) False si no existe el objeto. En caso que exista, lo retorna como tal.
        """
        btnRegresar['state']="disabled"
        btnBuscar['state']="disabled"
        objeto = buscarCedula(pcedula)
        if type(objeto)!=bool:
            decision= tk.messagebox.askyesno(message="El registro existe como "+objeto.obtenerNombre()+"\n¿Desea realizar los archivos respectivos del certificado?", title="Confirmación")
            if decision:
                crearXml(objeto)
                crearHtml(objeto)
                tk.messagebox.showinfo(message="¡Se han creado los archivos de los certificados HTML y XML!",title="Operación exitosa.")
            limpiar()
            cita1.focus()
        else:
            tk.messagebox.showerror(message="La cédula "+pcedula+" no está registrada.",title="Error al buscar la cédula.")
        btnRegresar['state']="normal"
        btnBuscar['state']="normal"
        return objeto
    #Provincia
    cita1 = tk.Entry(fFormulario,bd=3,font=("Arial",14),textvariable=provincia,width=4,justify="center")
    cita1.grid(column=1,row=1)
    cita1.focus()
    provincia.trace("w", lambda *args: limitador(cita1,provincia,1))
    tk.Label(fFormulario,text="-",bg=color).grid(column=2,row=1)#separador
    #Tomo
    cita2 = tk.Entry(fFormulario,bd=3,font=("Arial",14),textvariable=tomo,width=10,justify="center")
    cita2.grid(column=3,row=1)
    tomo.trace("w", lambda *args: limitador(cita2,tomo,4))
    tk.Label(fFormulario,text="-",bg=color).grid(column=4,row=1)#separador
    #Asiento
    cita3 = tk.Entry(fFormulario,bd=3,font=("Arial",14),textvariable=asiento,width=10,justify="center")
    cita3.grid(column=5,row=1)
    asiento.trace("w", lambda *args: limitador(cita3,asiento,4))
    #Buscar
    btnBuscar=tk.Button(fbtn,text="Buscar",command=lambda:(verificarCedula(provincia.get()+"-"+tomo.get()+"-"+asiento.get())))
    btnBuscar.config(width=13,bg="#FFFFFF", fg="black",font=("Arial", 13)) 
    btnBuscar.grid(row=1,column=1,pady=80,padx=10)
    #Regresar
    btnRegresar=tk.Button(fbtn,text="Regresar",command= regresar)
    btnRegresar.config(width=13,bg="#FFFFFF", fg="black",font=("Arial", 13)) 
    btnRegresar.grid(row=1,column=2,pady=80,padx=10)

    vCertificado.mainloop()
######################Configuración de la ventana Árbol########################
def ventanaArbol():
    "Funcionalidad: Crea la ventana de Árbol genealógico y tiene sus respectivas funciones"
    def obtenerPersonas():
        """
        Funcionalidad: obtiene las personas
        Salidas: listaNom: lista de cédula y nombre de todas las personas registradas
        """
        lista = verificarArchivo(nombreArchivo)
        listaNom=[]
        for objeto in lista:
            listaNom.append(objeto.obtenerCedula()+" "+objeto.obtenerNombre())
        return listaNom
    def limpiarCampos():
        """Funcionalidad: Limpia los campos de entry y la selección del combobox
        Entradas: ----
        Salidas:------ """
        decision= tk.messagebox.askyesno(message='''Esto eliminará la información de la
    búsqueda actual de la pantalla\n ¿Desea continuar?''', title="Advertencia")
        if decision:
            mama.config(state='normal')#Al estar en disabled se deben activar para poder borrar 
            papa.config(state='normal')
            hijo.config(state='normal')
            mama.delete(0,tk.END)#borra todo
            papa.delete(0,tk.END)
            hijo.delete(0,tk.END)
            mama.config(state='disabled')#Vuelve a deshabilitar el cuadro para que no se escriba
            papa.config(state='disabled')
            hijo.config(state='disabled')
            combobox.set("")#Deja el combobox en blanco
    def buscarObjeto(cedula):
        """Funcionalidad: Busca a la persona en la lista de objetos por cédula
        Entradas: cédula
        Salidas: objeto"""
        lista = verificarArchivo(nombreArchivo)
        for objeto in lista:
            if objeto.obtenerCedula()==cedula:
                persona=objeto
        return persona
    def infoPadres():
        """Funcionalidad: Imprime la información de los padres en los entries 
        Entradas: ----
        Salidas: ----"""
        persona= combobox.get()[:11]#obtiene la cédula
        if persona=="": #Si está vacío la selección del combobox da error
            tk.messagebox.showerror(message='Por favor seleccione a una persona.', title="Error")
        else:
            persona=buscarObjeto(persona)
            if papa=='':#Si el campo de entry está vacío inserta información
                mama.config(state='normal')
                papa.config(state='normal')#Al estar en disabled se deben activar para poder borrar
                hijo.config(state='normal')
                mama.insert(0,persona.obtenerMadre())
                papa.insert(0,persona.obtenerPadre())
                hijo.insert(0,persona.obtenerNombre())
                mama.config(state='readonly')
                papa.config(state='readonly')
                hijo.config(state='readonly')
            else: #Si tiene algo de una búsqueda previa, borra el contenido anterior e inserta el nuevo
                mama.config(state='normal')
                papa.config(state='normal')
                hijo.config(state='normal')
                mama.delete(0,tk.END)
                papa.delete(0,tk.END)
                hijo.delete(0,tk.END)
                mama.insert(0,persona.obtenerMadre())
                papa.insert(0,persona.obtenerPadre())
                hijo.insert(0,persona.obtenerNombre())
                mama.config(state='readonly')
                papa.config(state='readonly')
                hijo.config(state='readonly')
    def regresar():
        'Funcionalidad: Destruye la ventana actual y vuelve al menú'
        ventana.destroy()
        ventanaMenu()           
    #Configuración de ventana
    ancho,alto=600, 400
    ventana= tk.Tk()#Crea la ventana 
    anchoPantalla= ventana.winfo_screenwidth()
    largoPantalla= ventana.winfo_screenheight()
    posVentanaX= int((anchoPantalla/2)-(ancho/2))
    posVentanaY= int((largoPantalla/2)-(alto/2))
    ventana.geometry("{}x{}+{}+{}".format(ancho,alto,posVentanaX,posVentanaY))
    ventana.resizable(width=False, height=False)#Bloquea para que no se pueda cambia el tamaño de la ventana
    ventana.config(bg="#cb3234", bd=3)
    frame=tk.Frame(ventana,width=ancho, height=alto)
    frame.pack(fill='both')
    frame.config(bg="#FFFFFF", bd=25)
    ventana.overrideredirect(1)
    #Lineas
    canvas = tk.Canvas(frame, width=ancho, height=alto, bg='#FFFFFF')
    canvas.pack()#Crea un canvas en toda la ventana para poner las líneas
    canvas.create_line(200,250,300,350,width=3)
    canvas.create_line(385, 250, 285, 350,width=3)
    #Combobox
    combobox = ttk.Combobox(canvas,font=("Arial",14),width=30,
                            values=obtenerPersonas(), state='readonly')
    combobox.place(x=100,y=50)
    #Botones
    botonMostrar=tk.Button(ventana, text="Mostrar", bg="#FFFFFF", fg="#000000",
                           font=("Times New Roman", 15), command= infoPadres)
    botonMostrar.place(x=150,y=150)
    botonbtnLimpiarArbol=tk.Button(ventana, text="Limpiar", bg="#FFFFFF", fg="#000000",
                           font=("Times New Roman", 15), command=limpiarCampos)
    botonbtnLimpiarArbol.place(x=250,y=150)
    botonRegresar=tk.Button(ventana, text="Regresar", bg="#FFFFFF", fg="#000000",
                           font=("Times New Roman", 15), command=regresar)
    botonRegresar.place(x=350,y=150)
    #Labels
    lbArbol=tk.Label(canvas,text='Mostrar Árbol Genealógico: ', bg='#FFFFFF',
                font=('Times New Roman', 20))
    lbArbol.place(x=130,y=5)
    lbPersona=tk.Label(ventana,text='Persona: ', bg='#FFFFFF', font=('Times New Roman',14))
    lbPersona.place(x=30,y=75)
    lbResultado=tk.Label(ventana,text='Resultado de la búsqueda: ', bg='#FFFFFF',
                         font=('Times New Roman',14))
    lbResultado.place(x=30,y=200)
    #Entries:
    papa=ttk.Entry(ventana,state='disabled',width=30, justify='center')
    papa.place(x=105,y=250)
    mama=ttk.Entry(ventana, state='disabled',width=30, justify='center')
    mama.place(x=320,y=250)
    hijo=ttk.Entry(ventana,state='disabled',width=30, justify='center')
    hijo.place(x=220,y=350)
    ventana.mainloop()
####################Configuración de ventana Registrar#########################
def ventanaRegistar():
    """
    F: Muestra la ventana de registrar 
    E: -
    S: Todos los datos de registrar
    """
    #Variable que almacena los registros
    vRegistrar = tk.Tk()
    ancho,alto= 600,620
    color = "#FFFFFF" 
    anchoPantalla= vRegistrar.winfo_screenwidth()
    largoPantalla= vRegistrar.winfo_screenheight()
    posVentanaX= int((anchoPantalla/2)-(ancho/2))
    posVentanaY= int((largoPantalla/2)-(alto/1.8))
    vRegistrar.overrideredirect(1)#Desactivar botones del titulo
    vRegistrar.geometry("{}x{}+{}+{}".format(ancho,alto,posVentanaX,posVentanaY))
    vRegistrar.resizable(width=False, height=False)#Bloquea para que no se pueda cambia el tamaño de la vRegistrar
    vRegistrar.config(bg="#cb3234",bd=3)#Le pone color a la vRegistrar
    framePrin=tk.Frame(vRegistrar,width=ancho, height=alto)
    framePrin.pack(fill='both')
    framePrin.config(bg=color)
    framePrin.config(bd=15)
    ftitulo = tk.Frame(master=framePrin,width=ancho,height=60,bg=color)
    ftitulo.pack(fill='both')
    fFormulario = tk.Frame(master=framePrin,width=ancho,height=alto,bg=color)
    fFormulario.pack(fill='both')
    fbtn = tk.Frame(master=framePrin,bg=color)
    fbtn.pack()
    lTitulo=tk.Label(ftitulo, text="Datos de la nueva persona", bg=color, fg="#000000", font=("Times New Roman", 24))
    lTitulo.place(x=ancho/4,y=0)
    ################################################-Variables de control-################################################
    provincia = tk.StringVar()#número de provincia
    tomo = tk.StringVar()
    asiento = tk.StringVar()
    nombre = tk.StringVar()
    apellidos = tk.StringVar()
    sexo = tk.StringVar()#la variable sexo: >M ó >F
    sexo.set("")
    tprovincia = tk.StringVar()#nombre de la provincia
    canton = tk.StringVar()
    distrito = tk.StringVar()
    tprovincia.set("Elija una provincia.")
    canton.set("Elija una provincia antes.")
    distrito.set("Elija una provincia antes.")
    diaN = tk.StringVar()
    diaN.set(obtenerDia())#setea el día actual
    mesN = tk.StringVar()
    mesN.set(obtenerMes())#setea el mes actual
    annoN = tk.StringVar()
    annoN.set(obtenerAnno())#setea el año actual
    padre = tk.StringVar()
    nacionalidadP = tk.StringVar()
    madre = tk.StringVar()
    nacionalidadM = tk.StringVar()
    #-*--*--*--*-Definición de funciones-*--*--*--*-
    def guardar():
        """
        F: se encarga de guardar lo registrado en la listaRegistros y de cerrar la ventana
        """
        try:            
            actualizarArchivo(listaRegistros,nombreArchivo)
            vRegistrar.destroy()
            ventanaMenu()
        except:
            tk.messagebox.showerror("Error al guardar los datos","Verifique que el archivo se encuentre en el directorio.")
    def activarBotones(bandera=True):
        """
        F: Se encarga de activar o desactivar los botones.
        E: bandera(bool) define si se activan o si no. Por defecto es True
        S: -
        """
        if bandera:
            btnRegresar["state"]="normal"
            btnRegistrar["state"]="normal"
            btnLimpiar["state"]="normal"
        else:#desactiva estos botones para evitar la ejecución de otras funciones en simultáneo 
            btnRegistrar["state"]="disabled"
            btnLimpiar["state"]="disabled"
            btnRegresar["state"]="disabled"
        return ""
    def mostrarError(titulo,mensaje):
        """
        Se encarga de mostrara los errores, desactivando y volviendo a activar los botones para evitar la repetición intencional
        E: titulo y mensaje (strings)
        S: -
        """
        activarBotones(bandera=False)
        tk.messagebox.showerror(message=mensaje,title=titulo)
        activarBotones()
        return
    def preguntarDecision(mensaje,titulo):
        """
        F: se encarga de preguntar alguna accion que requiera la decision del usuario
        E: mensaje y titulo (strings) del cuadro de messagebox
        S: True si la respuesta es afirmativa, False si no
        """
        activarBotones(False)
        pdecision= tk.messagebox.askyesno(message=mensaje, title=titulo)
        activarBotones()
        return pdecision
    def limpiar(preguntar=True):
        """Funcionalidad: Limpia el formulario completo, reiniciando las variables de control
        Entradas: preguntar(bool) si la accion requiere de confirmación. Por defecto es True
        Salidas: decision (bool) si se decidio limpiar o no"""
        if preguntar:
            decision =preguntarDecision("Esto eliminará los datos hasta ahora ingresados\n¿Desea continuar?","Advertencia")
        else:
            decision = True
        if decision:
            provincia.set("")
            tomo.set("")
            asiento.set("")
            nombre.set("")
            apellidos.set("")
            tprovincia.set("Elija una provincia.")
            canton.set("Elija una provincia antes.")
            distrito.set("Elija una provincia antes.")
            sexo.set("")#la variable sexo: True->M False->F
            diaN.set(obtenerDia())#setea el día actual
            mesN.set(obtenerMes())#setea el mes actual
            annoN.set(obtenerAnno())#setea el año actual
            padre.set("")
            nacionalidadP.set("")
            madre.set("")
            nacionalidadM.set("")
        return decision
    def registrar():
        """
        F: se encarga de validar e ir registrando en la memoria volátil los datos ingresados
        E: - funciona al presionar el botón de registrar
        S: mensajes respectivos; ya sea si validó algo erróneo o si la información ingresada es correcta
        valida(string) última validacion realiza o (bool=True) si validó correctamente 
        """
        pcedula = provincia.get()+"-"+tomo.get()+"-"+asiento.get()#"Formatea" la cédula
        valida = validarCedula(pcedula)#llama a validar la cédula "formateada"
        if valida==True:
    ###############################################Valida que no exista en el registro del archivo##########################################
            if type(buscarCedula(pcedula))!=bool:
                return mostrarError("El usuario ya existe.","El usuario ingresado ya está registrado.")
    ####################################Valida que los apellidos de los padres que coincidan con el hijo##################################
            valida = validarApellidos(apellidos.get(),padre.get(),madre.get())
            if  type(valida) != bool:
                return mostrarError("Error en los apellidos de los padres.",valida)
    ###############################################Valida el nombre ingresado del hijo############################################
            pnombre = nombre.get()+" "+apellidos.get()
            valida = validarNombre(pnombre)
            if type(valida)==bool:
    ###############################################Valida el sexo ingresado del hijo############################################
                psexo = sexo.get()
                valida = validarSexo(psexo)
                if type(valida)==bool:
    ###############################################Valida la ubicacion ingresada del hijo############################################
                    pUbicacion = distrito.get()+" "+canton.get()+" "+tprovincia.get()
                    valida = validarUbicacion(pUbicacion)
                    if type(valida)==bool:
    ###############################################Valida la fecha de nacimiento del hijo############################################
                        pfechaN = diaN.get()+"/"+mesN.get()+"/"+annoN.get()
                        valida = validarFecha(pfechaN)
                        if type(valida)==bool:
    ###############################################Valida el nombre ingresado del padre############################################
                            pPadre,nacionalP = validarPadre(padre.get())
                            if nacionalP=="NER":
                                decision= preguntarDecision(pPadre+" no está registrado.\n¿Desea continuar?", "Advertencia")
                                if decision==False:
                                    return decision
                                nacionalP=True
                            if type(nacionalP)!=int:
    ###############################################Valida el nombre ingresado de la madre############################################
                                pMadre,nacionalM = validarPadre(madre.get())
                                if nacionalM=="NER":
                                    decision= preguntarDecision(pMadre+" no está registrado.\n¿Desea continuar?", "Advertencia")
                                    if decision==False:
                                        return decision
                                    nacionalM=True
    ###############################################Valida que el nombre de la madre y del padre no sean los mismos###########################################                                
                                if pMadre==pPadre:
                                    return tk.messagebox.showerror("Error al registrar.","Los datos del padre y de la madre no pueden ser iguales")
                                if type(nacionalM)!=int:
    ###########################################Valida la nacionalidad del padre######################################################
                                    nacionalidadPadre = nacionalidadP.get()
                                    valida = validarNacionalidad(nacionalidadPadre,nacionalP)
                                    if type(valida)==bool:
    ###########################################Valida la nacionalidad de la madre######################################################
                                        nacionalidadMadre = nacionalidadM.get()
                                        valida = validarNacionalidad(nacionalidadMadre,nacionalM)
                                        if type(valida)==bool:
                                            #Agrega los datos a la clase
                                            persona = Persona(pcedula,pnombre,psexo,pUbicacion,pfechaN,pPadre,nacionalidadPadre,pMadre,nacionalidadMadre)#setea en la clase
                                            #valida el objeto insertado en la clase que no exista en los registros hasta ahora almacenados
                                            valida = buscarCedula(persona.obtenerCedula(),listaRegistros)
                                            if type(valida)==bool:
                                                decision= preguntarDecision("¿Seguro que desea ingresar a "+persona.obtenerNombre()+" con los datos ingresados?","Confirmación.")
                                                if decision:
                                                    listaRegistros.append(persona)#agrega en la lista a guardar después 
                                                    limpiar(False)#no pregunta limpiar
                                                return decision
                                            else:
                                                mostrarError("Error al registrar","La persona ya está registrada como"+valida.obtenerNombre())#el caso principal es si ya existe el registro                                    else:
                                        else:
                                            mostrarError("La nacionalidad de la madre no es correcta",valida)
                                    else:
                                        mostrarError("La nacionalidad del padre no es correcta",valida)
                                else:
                                    mostrarError("El nombre de la madre no es correcto",pMadre)
                            else:
                                mostrarError("El nombre del padre no es correcto",pPadre)
                        else:
                            mostrarError("La fecha no es correcta",valida)
                    else:
                        mostrarError("La ubicación no es correcta",valida)
                else:
                    mostrarError("El sexo no es correcto",valida)
            else:
                mostrarError("El nombre no es correcto",valida)
        else:
            mostrarError("La cédula no es correcta.","La cédula del nuevo usuario debería ser otra.")
        return valida
    def definirProvincia(numProvincia):
        """
        F: define la provincia automáticamente según el primer dígito de la cita o cédula ingresado
        E: numProvincia(string): número de provincia del número de cita
        S: num-1(int) número de provincia
        Asigna el valor automáticamente a la variable de control tprovincia y al combobox de provinciaCombo
        """
        num=int(numProvincia)
        if num>0:
            provinciasL=["SAN JOSE","ALAJUELA","CARTAGO","HEREDIA","GUANACASTE","PUNTARENAS","LIMON","NACIONALIZADO","CASO ESPECIAL"]                
            tprovincia.set(provinciasL[num-1])
        else:
            tprovincia.set("Sin provincia definida")
        return num
    def obtenerCantonesAux(event):
        """
        F: asigna los valores al combobox de cantonCombo de la lista de cantones según la provincia ingresada
        E: funciona por el evento que se genera al seleccionar un valor del combobox de provinciaCombo
        S: cantones(lista de los cantones según el número de provincia obtenido)
        valores a poner en el combobox de cantonCombo
        """
        canton.set("Elija un cantón de la lista.")
        distrito.set("Elija un cantón antes.")
        numProvincia = provinciaCombo.current()+1#obtiene el indice de la opcion seleccionada en el combobox
        cantones = ObtenerCantones(numProvincia)#obtiene la lista de los cantones respecto al número de provincia
        cantonCombo['values']= cantones
        return cantones
    def setearListas(numProvincia):
        """
        Setea los valores de la lista de cantones en base al número de la provincia brindada por el usuario
        E: numProvincia(string) número en cadena de la provincia brindada por el usuario en el entry respectivo
        S: cantones(lista) lista con los cantones disponibles
        """
        try:
            numProvincia = int(numProvincia)
            assert numProvincia <= 9 or numProvincia >= 1
            cantonCombo['values']=""
            distritoCombo['values']=""
            #provinciaCombo['state']="readonly"
            if numProvincia == 8:#En caso de Nacionalización
                canton.set("Nacionalización.")
                distrito.set("Nacionalización.")
                return ""
            elif numProvincia == 9:#En caso especial de nacimiento
                canton.set("Caso especial de nacimiento.")
                distrito.set("Caso especial de nacimiento.")
                return ""
            else:
                canton.set("Elija un cantón de la lista")
                distrito.set("Elija un cantón primero")            
                cantones = ObtenerCantones(numProvincia)#obtiene la lista de los cantones respecto al número de provincia
                provinciaCombo['state']="enabled"
                cantonCombo['values']= cantones
                return cantones
        except ValueError:
            return ""        
        except AssertionError:
            return "" 
    def obtenerDistritosAux(event): #en caso de los distritos
        """
        F: función auxiliar para elegir los distritos en caso que detecte que se ingresó algo en canton
        E: variable 'event' que detecta un evento en la selección del cantón
        S: setea los valores a la lista de distritos. retorna la lista de los distritos de acuerdo a las variables de control
        de canton y provincia
        """
        try:
            distritos = []
            nProvincia = provinciaCombo.current()+1
            assert nProvincia < 8
            distrito.set("Elija un distrito de la lista")
            nomCanton = canton.get()
            distritos = obtenerDistritos(nProvincia,nomCanton)
            distritoCombo["values"]= distritos
            return distritos
        except ValueError:
            distrito.set("Elija una provincia primero.")
            return ""
        except AssertionError:
            return ""
    def setearDias(event):
        """
        F: pone los días automáticamente en la lista de días según el mes cambiado y el año ya puesto
        E: - (funciona por medio del evento de selección del combobox de mesCombo)
        S: diasL(lista de días a poner en el combobox de diaCombo)
        Salidas al combobox de dias de parte de la función obtenerDiasMes()
        """
        diasL=obtenerDiasMes(mesN.get(),annoN.get())
        diaCombo["values"]=diasL
        if int(diaN.get()) > int(diasL[-1]):#Si los días anteriormente puestos son más de los que hay que poner
            diaN.set(diasL[-1])
        return diasL
    def limitarAnno(entryAnno):
        """
        Se encarga de delimitar el número de caracteres del entry anno.
        Define los valores de ciertos widgets en base al dato de la provincia.
        E: entryTexto(texto del entry string) num(número de caracteres int)
        S: return
        """
        if len(entryAnno.get()) > 0:
            if re.search("\D$",entryAnno.get()):#Valida que no contenga letras(o que digite algo distinto a dígitos)
                entryAnno.set(entryAnno.get()[:-1])#setea el entry hasta donde no hay letras
            else:
                va = validarAnno(entryAnno.get()[:4])
                if type(va) != bool:#cambia de color si el año no cumple el formato
                    annoCombo['foreground']="red"
                else:
                    annoCombo['foreground']="black"
                    setearDias(True)
                entryAnno.set(entryAnno.get()[:4])
                annoN.set(entryAnno.get()[:4])
        return ""             
    def obtenerNacionalidadAux(mama,cedula):
        """
        F: asigna la nacionalidad de forma automática si se elige una cédula ya registrada
        E: mama(booleano) True si es la madre, False si es del padre
        S: -
        """
        valida = validarCedula(cedula[:11])
        if type(valida)==bool:
            valida = buscarCedula(cedula[:11],listaRegistros)
            if type(valida)!=bool:
                if mama:
                    nacionalidadM.set("COSTARRICENSE")
                else:
                    nacionalidadP.set("COSTARRICENSE")
        else:
            if mama:
                madre.set(cedula)
            else:
                padre.set(cedula)
        return ""
    def aMayusculas(var):
        """
        F: convierte a mayúsculas una variable de un entry
        S: -
        E: var(variable string del entry)
        """
        var.set(var.get().upper())
        return ""
    def limitador(widget,entryTexto,num):
        """
        Se encarga de delimitar el número de caracteres del entry Cita.
        Define los valores de ciertos widgets en base al dato de la provincia
        E: entryTexto(texto del entry string) num(número de caracteres int)
        S: return
        """
        if len(entryTexto.get()) == num:
            #línea para cambiar de entry automáticamente encontrada en https://stackoverrun.com/es/q/275998:
            widget.tk_focusNext().focus()
        if len(entryTexto.get()) > 0:
            if re.search("\D$",entryTexto.get()):#Valida que no contenga letras(o que digite algo distinto a dígitos)
                entryTexto.set(entryTexto.get()[:-1])#setea el entry hasta donde no hay letras
            #donde esta el :num se limita la cantidad d caracteres
            elif num == 1:#si es 1 está poniendo el número de provincia en la cita
                if re.search("0$",entryTexto.get()):#valida que no sea 0
                    entryTexto.set(entryTexto.get()[:-1])#setea el entry hasta donde no hay letras                
                else:
                    definirProvincia(entryTexto.get()[-1])#definir la provincia a mostrar en el entry
                    setearListas(entryTexto.get()[-1])#definir la lista de cantones a mostrar en la lista de cantones
                    entryTexto.set(entryTexto.get()[-1])#al texto le asigna el último número ingresado              
            else:
                entryTexto.set(entryTexto.get()[:num])
            return ""
    #-*Etiquetas*-#
    apartados = ["Cita:","Nombre:","Apellidos:","Sexo:","Provincia:","Cantón:","Distrito:","Día:","Mes:","Año:","Padre:","Nacionalidad:","Madre:","Nacionalidad:"]
    fila = 1
    for opcion in apartados:
        label = tk.Label(fFormulario,text=opcion,font=("Arial", 13),bg=color,width=16,pady=5,padx=5,anchor="w")
        label.grid(column=0,row=fila)
        fila+=1
    #-*Opción Cita (cédula)*-#
    #Provincia
    cita1 = tk.Entry(fFormulario,bd=3,font=("Arial",14),textvariable=provincia,width=4,justify="center")
    cita1.grid(column=1,row=1)
    cita1.focus()
    provincia.trace("w", lambda *args: limitador(cita1,provincia,1))
    tk.Label(fFormulario,text="-",bg=color).grid(column=2,row=1)#separador
    #Tomo
    cita2 = tk.Entry(fFormulario,bd=3,font=("Arial",14),textvariable=tomo,width=10,justify="center")
    cita2.grid(column=3,row=1)
    tomo.trace("w", lambda *args: limitador(cita2,tomo,4))
    tk.Label(fFormulario,text="-",bg=color).grid(column=4,row=1)#separador
    #Asiento
    cita3 = tk.Entry(fFormulario,bd=3,font=("Arial",14),textvariable=asiento,width=10,justify="center")
    cita3.grid(column=5,row=1)
    asiento.trace("w", lambda *args: limitador(cita3,asiento,4))
    #-*Opción Nombre*-#
    nombreE = tk.Entry(fFormulario,bd=3,font=("Arial",14),textvariable=nombre,width=30)
    nombreE.grid(row=2,column=1,columnspan=5)
    nombre.trace("w", lambda *args: aMayusculas(nombre))#convierte a mayúsculas lo ingresado
    #-*Opción Apellidos*-#
    apellidosE = tk.Entry(fFormulario,bd=3,font=("Arial",14),textvariable=apellidos,width=30)
    apellidosE.grid(row=3,column=1,columnspan=5)
    apellidos.trace("w", lambda *args: aMayusculas(apellidos))
    #-*Opción Sexo*-#
    sexoM = tk.Radiobutton(fFormulario,variable=sexo,text="Masculino",value="M",bg=color)
    sexoM.grid(row=4,column=2,columnspan=2)
    sexoM.config(bg=color,font=("Arial",13))
    sexoF = tk.Radiobutton(fFormulario,variable=sexo,text="Femenino",value="F",bg=color)
    sexoF.grid(row=4,column=4,columnspan=2)
    sexoF.config(bg=color,font=("Arial",13))
    #-*Opción Provincia*-#
    provinciaCombo = ttk.Combobox(fFormulario,textvariable=tprovincia,state="enabled",font=("Arial",14),width=29,values=["SAN JOSE","ALAJUELA","CARTAGO","HEREDIA","GUANACASTE","PUNTARENAS","LIMON"])
    provinciaCombo.grid(row=5,column=1,columnspan=5)
    #-*Opción Cantón*-#
    cantonCombo=ttk.Combobox(fFormulario,textvariable=canton,state="readonly",font=("Arial",14),width=29)
    cantonCombo.grid(row=6,column=1,columnspan=5)
    #-*Opción Distrito*-#
    distritoCombo=ttk.Combobox(fFormulario,textvariable=distrito,state="readonly",font=("Arial",14),width=29)
    distritoCombo.grid(row=7,column=1,columnspan=5)
    #Eventos de la escogencia de provincia y canton
    provinciaCombo.bind("<<ComboboxSelected>>",obtenerCantonesAux)#en caso de los distritos
    cantonCombo.bind("<<ComboboxSelected>>",obtenerDistritosAux)#en caso de los distritos
    #-*Opción Día*-#
    diaCombo = ttk.Combobox(fFormulario,textvariable=diaN,state="readonly",font=("Arial",14),width=10,values=obtenerDiasMes(mesN.get(),annoN.get()))
    diaCombo.grid(row=8,column=1,columnspan=5,sticky="W")
    #-*Opción Mes*-#
    mesCombo = ttk.Combobox(fFormulario,textvariable=mesN,state="readonly",font=("Arial",14),width=10,values=obtenerMeses())
    mesCombo.grid(row=9,column=1,columnspan=5,sticky="W")
    mesCombo.bind("<<ComboboxSelected>>",setearDias)
    #-*Opción Año*-#
    annoCombo = tk.Entry(fFormulario,textvariable=annoN,state="normal",font=("Arial",14),width=10)
    annoCombo.grid(row=10,column=1,columnspan=5,sticky="W")
    annoN.trace("w", lambda *args: limitarAnno(annoN))
    #-*Opción Padre y Nacionalidad*-#
    padreCombo = ttk.Combobox(fFormulario,textvariable=padre,state="normal",font=("Arial",11),width=40,values=obtenerPadres(listaRegistros,"M"))
    padreCombo.grid(row=11,column=1,columnspan=5)
    padre.trace("w", lambda *args: aMayusculas(padre))
    nacionPCombo = ttk.Combobox(fFormulario,textvariable=nacionalidadP,state="readonly",font=("Arial",14),width=29,values=["COSTARRICENSE","NICARAGUENSE","ARGENTINO","ESTADOUNIDENSE","CHINO"])
    nacionPCombo.grid(row=12,column=1,columnspan=5)
    padreCombo.bind("<<ComboboxSelected>>",lambda *args:obtenerNacionalidadAux(False,padre.get()))
    nacionPCombo.bind("<<ComboboxSelected>>",lambda *args:obtenerNacionalidadAux(False,padre.get()))
    #-*Opción Madre y Nacionalidad*-#
    madreCombo = ttk.Combobox(fFormulario,textvariable=madre,state="normal",font=("Arial",11),width=40,values=obtenerPadres(listaRegistros,"F"))
    madreCombo.grid(row=13,column=1,columnspan=5)
    madre.trace("w", lambda *args: aMayusculas(madre))
    nacionMCombo = ttk.Combobox(fFormulario,textvariable=nacionalidadM,state="readonly",font=("Arial",14),width=29,values=["COSTARRICENSE","NICARAGUENSE","ARGENTINA","ESTADOUNIDENSE","CHINA"])
    nacionMCombo.grid(row=14,column=1,columnspan=5)
    nacionMCombo.bind("<<ComboboxSelected>>",lambda *args:obtenerNacionalidadAux(True,madre.get()))
    madreCombo.bind("<<ComboboxSelected>>",lambda *args:obtenerNacionalidadAux(True,madre.get()))
    #*-*-*-*-*-*-Botones-*-*-*-*-*-*-#
    #Registrar
    btnRegistrar=tk.Button(fbtn,text="Registrar",command=registrar)
    btnRegistrar.config(width=13,bg="#FFFFFF", fg="black",font=("Arial", 13))
    btnRegistrar.grid(row=1,column=1,pady=15,padx=10)
    #Limpiar
    btnLimpiar=tk.Button(fbtn,text="Limpiar",command=limpiar)
    btnLimpiar.config(width=13,bg="#FFFFFF", fg="black",font=("Arial", 13)) 
    btnLimpiar.grid(row=1,column=2,pady=15,padx=10)
    #Regresar
    btnRegresar=tk.Button(fbtn,text="Regresar",command=guardar)
    btnRegresar.config(width=13,bg="#FFFFFF", fg="black",font=("Arial", 13))
    btnRegresar.grid(row=1,column=3,pady=15,padx=10)
    vRegistrar.mainloop()
    return ""
###################Configuración ventana Menú###############################
def ventanaMenu():
    'Funcionalidad: Crea la ventana de menú y contiene sus funcionalidades '
    def salir():
        'Funcionalidad: Destruye la ventana si el usuario confirma'
        decision= tk.messagebox.askyesno(message='¿Realmente desea salir?',
                                         title="Confirmación")
        if decision:
            ventana.destroy()
    def abrirArbol():
        'Funcionalidad: Cierra la ventana actual y abre la de Árbol'
        ventana.destroy()
        ventanaArbol()
    def abrirRegistrar():
        'Funcionalidad: Cierra la ventana actual y abre la de registrar'
        ventana.destroy()
        ventanaRegistar()
    def abrirCertificado():
        'Funcionalidad: Cierra la ventana actual y abre la de certificado'
        ventana.destroy()
        ventanaCertificado()
    def obtenerNumPersonas():
        """Funcionalidad: Obtiene la cantidad de personas registradas
        Salidas: largo de la lista de objetos"""
        lista = verificarArchivo(nombreArchivo)
        return str(len(lista))
    #Configuración de ventana
    ancho,alto=540, 500
    ventana= tk.Tk()#Crea la ventana
    anchoPantalla= ventana.winfo_screenwidth()
    largoPantalla= ventana.winfo_screenheight()
    posVentanaX= int((anchoPantalla/2)-(ancho/2))
    posVentanaY= int((largoPantalla/2)-(alto/2))
    ventana.geometry("{}x{}+{}+{}".format(ancho,alto,posVentanaX,posVentanaY))
    ventana.resizable(width=False, height=False)#Bloquea para que no se pueda cambia el tamaño de la ventana
    frame=tk.Frame(ventana,width=600, height=500)
    frame.pack(fill='both')
    frame.config(bg="#FFFFFF")
    frame.config(bd=25)
    ventana.config(bg="#cb3234")
    ventana.config(bd=3)
    ventana.overrideredirect(1)
    #Labels
    lbltitulo= tk.Label(ventana, text="Tribunal Supremo de Elecciones", bg="#FFFFFF",
                    font=("Times New Roman", 30))
    lbltitulo.place(x=ancho//2, y=30, anchor="center")
    lbltit= tk.Label(ventana, text="Total de personas: "+obtenerNumPersonas(), bg="#FFFFFF",
                    font=("Times New Roman", 14))
    lbltit.place(x=440, y=80, anchor="center")
    #Botones
    btnRegistrar= tk.Button(ventana, text="Registrar Nacimiento",
                                bg="#FFFFFF",font=("Times New Roman", 16),
                            command= abrirRegistrar)
    btnRegistrar.place(x=ancho//2, y=150, anchor="center")

    btnMostrar= tk.Button(ventana, text="Mostrar Árbol Genealógico",
                                bg="#FFFFFF",font=("Times New Roman", 16), command= abrirArbol)
    btnMostrar.place(x=ancho//2, y=250, anchor="center")

    btnCertificado= tk.Button(ventana, text="Certificado de Nacimiento",
                                bg="#FFFFFF", font=("Times New Roman", 16),
                              command=abrirCertificado)
    btnCertificado.place(x=ancho//2, y=350, anchor="center")

    btnSalir= tk.Button(ventana, text="Salir", bg="#FFFFFF", command= salir,
                                font=("Times New Roman", 16))
    btnSalir.place(x=ancho//2, y=450, anchor="center")

    ventana.mainloop()    
######################Configuración ventana Ingreso###########################
def ventanaIngreso():
    'Funcionalidad: Crea la ventana de ingreso y tiene sus funcionalidades'
    def limpiar():
        'Funcionalidad: Limpia los campos de usuario y contraseña'
        decision= tk.messagebox.askyesno(message='''Esto eliminará lo ingresado en usuario
    y contraseña. \n ¿Desea continuar?''', title="Advertencia")
        if decision:
            usuario.delete(0,tk.END)
            contrasenna.delete(0,tk.END)
    def entrar():
        """Funcionalidad: Verifica si el usuario y contraseña están bien y entra o da error en caso
        contrario
        Salidas: Abre el menú si coincide y tira errores correspondientes en caso de que no"""
        listaUsuarios=[]#Crea una lista con sublistas que contienen los usuarios y contraseñas
        user=usuario.get()
        contra= contrasenna.get()
        archivo=open('usuarios.txt','r')
        for usuarios in archivo:
            if usuarios[-1:]=="\n":#Si hay un enter lo elimina
                linea=usuarios[:-1]
                listaUsuarios.append(linea.split("_"))#Divide si encuentra _
            else:
                listaUsuarios.append(usuarios.split("_"))
        archivo.close()
        for registrados in listaUsuarios:
            if registrados[0]==user and registrados[1]==contra:
                ventanaIngreso.destroy()
                return ventanaMenu()
            elif registrados[0]==user and registrados[1]!=contra or registrados[0]!=user and registrados[1]==contra:
                return tk.messagebox.showerror(message='''Error, usuario o contraseña incorrectos''',
                                        title="Error")
            elif registrados[0]!=user and registrados[1]!=contra and registrados==listaUsuarios[-1]:
                return tk.messagebox.showerror(message='''Error, usuario no registrado''',
                                        title="Error")
    #Configuración de la ventana
    ancho,alto=330, 140
    ventanaIngreso= tk.Tk()#Crea la ventana 
    anchoPantalla= ventanaIngreso.winfo_screenwidth()
    largoPantalla= ventanaIngreso.winfo_screenheight()
    posVentanaX= int((anchoPantalla/2)-(ancho/2))
    posVentanaY= int((largoPantalla/2)-(alto/2))
    ventanaIngreso.geometry("{}x{}+{}+{}".format(ancho,alto,posVentanaX,posVentanaY))
    ventanaIngreso.resizable(width=False, height=False)#Bloquea para que no se pueda cambia el tamaño de la ventana
    frame=tk.Frame(ventanaIngreso,width=330, height=140)
    frame.pack(fill='both')
    frame.config(bg="#FFFFFF")
    frame.config(bd=25)
    ventanaIngreso.config(bg="#cb3234")
    ventanaIngreso.config(bd=3)
    ventanaIngreso.overrideredirect(1)
    #Botones
    botonLimpiar=tk.Button(ventanaIngreso, text="Limpiar", bg="#FFFFFF", fg="#000000",
                           font=("Times New Roman", 10), command=limpiar)
    botonLimpiar.place(x=220,y=100)
    botonIngresar=tk.Button(ventanaIngreso, text="Ingresar", bg="#FFFFFF", fg="#000000",
                           font=("Times New Roman", 10),command=entrar)
    botonIngresar.place(x=130,y=100)
    #Labels
    lbUsuario=tk.Label(ventanaIngreso,text='Usuario: ', bg='#FFFFFF', fg='#000000',
                       font=('Times New Roman', 14))
    lbUsuario.place(x=0,y=30)
    lbContrasenna=tk.Label(ventanaIngreso,text='Contraseña: ', bg='#FFFFFF', fg='#000000',
                       font=('Times New Roman', 14))
    lbContrasenna.place(x=0,y=60)
    #Entry
    usuario=ttk.Entry(ventanaIngreso)
    usuario.place(x=120,y=30)
    contrasenna=ttk.Entry(ventanaIngreso, show='*')#remplaza lo ingresado por * para ocultar la clave
    contrasenna.place(x=120,y=60)
    ventanaIngreso.mainloop()
#PP
if validarArchivo():#Si el archivo está bien abre la ventana de ingreso
    ventanaIngreso()
else:#Muestra un mensaje de error
    root = tk.Tk()#Crea una ventana, para poder controlarla, si no se hace python la crea auto.
    root.withdraw()#Se minimiza la ventana para que no se muestre junto al error
    tk.messagebox.showerror(message='''Error, la información de alguno de los usuarios registrados
no cumple con el formato. Por favor arreglelo para continuar. ''', title="Error")
