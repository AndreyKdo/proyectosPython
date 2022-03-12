#Elaborado por: Sara Segura, Andrey Picado
#Fecha de creación: 31‎ de ‎julio‎ de ‎2020, ‏‎04:27:51 p. m.
#Ultima modificación: 05/08/2020
#Version: 3.8.5
#Importación de librerías
from datetime import date
import re
from archivo import * #módulo archivo contiene las funciones para el manejo de archivos
#$-$-$-$-$-$-$-$-$-$-Definición de Funciones$-$-$-$-$-$-$-$-$-$-
#-*-*-*-*-*-*-*-*-*INICIO DE FUNCIONES PARA REGISTRAR-*-*-*-*-*-*-*-*-*# 
"""
Funciones que se encargan de devolver los cantones y los distritos según corresponda al número de provincia y nombre de cantón
El número de provincia se da como tipo entero
El nombre de cantón se da en formato string obligatoriamente en mayúsculas
"""
#Investigacion tkinter para interfaces graficas (formularios redireccionables RETO 2)
#Fecha de creación de las funciones de obtención de los cantones y provincias: 26/03/2020
def ObtenerCantones(nProvincia):
    """
    F: retorna los cantones pertenecientes a un número de provincia dado
    E: nProvincia(int) número de provincia a evaluar
    S: lista con los cantones respectivos      
    """
    if nProvincia==1:
            return ["SAN JOSE","ESCAZU","DESAMPARADOS","PURISCAL","TARRAZU","ASERRI","MORA","GOICOECHEA","SANTA ANA","ALAJUELITA","VAZQUEZ DE CORONADO","ACOSTA","TIBAS","MORAVIA","MONTES DE OCA","TURRUBARES","DOTA","CURRIDABAT","PEREZ ZELEDON","LEON CORTES"]
    elif nProvincia==2:
            return ["ALAJUELA","SAN RAMON","GRECIA","SAN MATEO","ATENAS","NARANJO","PALMARES","POAS","OROTINA","SAN CARLOS","ALFARO RUIZ","VALVERDE VEGA","UPALA","LOS CHILES","GUATUSO","RIO CUARTO"]
    elif nProvincia==3:
            return ["CARTAGO","PARAISO","LA UNION","JIMENEZ","TURRIALBA","ALVARADO","OREAMUNO"]
    elif nProvincia==4:
            return ["HEREDIA","BARVA","SANTO DOMINGO","SANTA BARBARA","SAN RAFAEL","SAN ISIDRO","BELEN","FLORES","SAN PABLO","SARAPIQUI"]
    elif nProvincia==5:
            return ["LIBERIA","NICOYA","SANTA CRUZ","BAGACES","CARRILLO","CAÑAS","ABANGARES","TILARAN","NANDAYURE","LA CRUZ","HOJANCHA"]	
    elif nProvincia==6:
            return ["PUNTARENAS","ESPARZA","BUENOS AIRES","MONTES DE ORO","OSA","AGUIRRE","GOLFITO","COTO BRUS","PARRITA","CORREDORES","GARABITO"]
    elif nProvincia==7:
            return ["LIMON","POCOCI","SIQUIRRES","TALAMANCA","MATINA","GUACIMO"]
    return ["Elija un cantón"]
def obtenerDistritos(pProvincia,pcanton):
    """
    F: retorna los cantones pertenecientes a un número de provincia dado
    E: nProvincia(int) número de provincia a evaluar
    S: lista con los cantones respectivos      
    """
#-*-*-*-*-*-*-DISTRITOS POR CANTON DE LA PROVINCIA DE "SAN JOSE"-*-*-*-*-*-*#
    if pProvincia ==1:
            if pcanton == "SAN JOSE":
                    return ["CARMEN","MERCED","HOSPITAL","CATEDRAL","ZAPOTE","SAN FRANCISCO DE DOS RIOS","LA URUCA","MATA REDONDA","PAVAS","HATILLO","SAN SEBASTIAN"]
            elif pcanton == "ESCAZU":
                    return ["ESCAZU","SAN ANTONIO","SAN RAFAEL"]			
            elif pcanton == "DESAMPARADOS":	
                    return ["DESAMPARADOS","SAN MIGUEL","SAN JUAN DE DIOS","SAN RAFAEL ARRIBA","SAN ANTONIO","FRAILES","PATARRA","SAN CRISTOBAL","ROSARIO","DAMAS","SAN RAFAEL ABAJO","GRAVILIAS","LOS GUIDO"]			
            elif pcanton == "PURISCAL":
                    return ["SANTIAGO","MERCEDES SUR","BARBACOAS","GRIFO ALTO","SAN RAFAEL","CANDELARIA","DESAMPARADITOS","SAN ANTONIO","CHIRES"]			
            elif pcanton == "TARRAZU":
                    return ["SAN MARCOS","SAN LORENZO","SAN CARLOS"]			
            elif pcanton == "ASERRI":
                    return ["ASERRI","TARBACA","VUELTA DE JORCO","SAN GABRIEL","LEGUA","MONTERREY","SALITRILLOS"]		
            elif pcanton == "MORA":
                    return ["CIUDAD COLON","GUAYABO","TABARCIA","PIEDRAS NEGRAS","PICAGRES","JARIS"]		
            elif pcanton == "GOICOECHEA":
                    return ["GUADALUPE","SAN FRANCISCO","CALLE BLANCOS","MATA DE PLATANO","IPIS","RANCHO REDONDO","PURRAL"]	
            elif pcanton == "SANTA ANA":
                    return ["SANTA ANA","SALITRAL","POZOS","URUCA","PIEDADES","BRASIL"]	
            elif pcanton == "ALAJUELITA":
                    return ["ALAJUELITA","SAN JOSECITO","SAN ANTONIO","CONCEPCION","SAN FELIPE"]		
            elif pcanton == "VAZQUEZ DE CORONADO":
                    return ["SAN ISIDRO","SAN RAFAEL","DULCE NOMBRE DE JESUS","PATALILLO","CASCAJAL"]		
            elif pcanton == "ACOSTA":
                    return ["SAN IGNACIO","GUAITIL","PALMICHAL","CANGREJAL","SABANILLAS"]
            elif pcanton == "TIBAS":
                    return ["SAN JUAN","CINCO ESQUINAS","ANSELMO LLORENTE","LEON XIII","COLIMA"]		
            elif pcanton == "MORAVIA":
                    return ["SAN VICENTE","SAN JERONIMO","TRINIDAD"]
            elif pcanton == "MONTES DE OCA":	
                    return ["SAN PEDRO","MERCEDES","SABANILLA","SAN RAFAEL"]
            elif pcanton == "TURRUBARES":
                    return ["SAN PABLO","SAN PEDRO","SAN JUAN DE MATA","SAN LUIS","CARARA"]
            elif pcanton == "DOTA":	
                    return ["SANTA MARIA","JARDIN","COPEY"]
            elif pcanton == "CURRIDABAT":	
                    return ["CURRIDABAT","GRANADILLA","SANCHEZ","TIRRASES"]
            elif pcanton == "PEREZ ZELEDON":
                    return ["SAN ISIDRO DE EL GENERAL","GENERAL","DANIEL FLORES","RIVAS","SAN PEDRO","PLATANARES","PEJIBAYE","CAJON","BARU","RIO NUEVO","PARAMO","LA AMISTAD"]	
            elif pcanton == "LEON CORTES":	
                    return ["SAN PABLO","SAN ANDRES","LLANO BONITO","SAN ISIDRO","SANTA CRUZ","SAN ANTONIO"]			
#-*-*-*-*-*-*-DISTRITOS POR CANTON DE LA PROVINCIA DE "ALAJUELA"-*-*-*-*-*-*#
    elif pProvincia ==2:
            if pcanton == "ALAJUELA":
                    return ["ALAJUELA","SAN JOSE","CARRIZAL","SAN ANTONIO","GUACIMA","SAN ISIDRO","SABANILLA","SAN RAFAEL","RIO SEGUNDO","DESAMPARADOS","TURRUCARES","TAMBOR","GARITA","SARAPIQUI"]                
            elif pcanton == "SAN RAMON":	
                    return ["SAN RAMON","SANTIAGO","SAN JUAN","PIEDADES NORTE","PIEDADES SUR","SAN RAFAEL","SAN ISIDRO","ANGELES","ALFARO","VOLIO","CONCEPCION","ZAPOTAL","PENNAS BLANCAS"]              
            elif pcanton == "GRECIA":
                    return ["GRECIA","SAN ISIDRO","SAN JOSE","SAN ROQUE","TACARES","PUENTE DE PIEDRA","BOLIVAR"]              
            #ESTE CANTON ES EL NUEVO NUMERO 16 FUE INAUGURADO EN EL 2017:"#ESPACIO RIO CUARTO#" en la lista sería el indice 5 HTTPS://WWW.PRESIDENCIA.GO.CR/COMUNICADOS/2017/05/RIO-CUARTO-SE-CONVIERTE-EN-EL-CANTON-NUMERO-82-DE-COSTA-RICA/
            elif pcanton == "RIO CUARTO":
                    return ["RIO CUARTO"] #EL CODIGO POSTAL ES COMO SI AUN PERTENECIERA A GRECIA 20306
            elif pcanton == "SAN MATEO":
                    return ["SAN MATEO","DESMONTE","JESUS MARIA"]
            elif pcanton == "ATENAS":
                    return ["ATENAS","JESUS","MERCEDES","SAN ISIDRO","CONCEPCION","SAN JOSE","SANTA EULALIA","ESCOBAL"]             
            elif pcanton == "NARANJO":
                    return ["NARANJO","SAN MIGUEL","SAN JOSE","CIRRI SUR","SAN JERONIMO","SAN JUAN","EL ROSARIO","PALMITOS"]
            elif pcanton == "PALMARES":	
                    return ["PALMARES","ZARAGOZA","BUENOS AIRES","SANTIAGO","CANDELARIA","ESQUIPULAS","GRANJA"]
            elif pcanton == "POAS":	
                    return ["SAN PEDRO","SAN JUAN","SAN RAFAEL","CARRILLOS","SABANA REDONDA"]
            elif pcanton == "OROTINA":
                    return ["OROTINA","MASTATE","HACIENDA VIEJA","COYOLAR","CEIBA"]
            elif pcanton == "SAN CARLOS":
                    return ["QUESADA","FLORENCIA","BUENAVISTA","AGUAS ZARCAS","VENECIA","PITAL","LA FORTUNA","TIGRA","PALMERA","VENADO","CUTRIS","MONTERREY","POCOSOL"]
            elif pcanton == "ALFARO RUIZ":	
                    return ["ZARCERO","LAGUNA","TAPEZCO","GUADALUPE","PALMIRA","ZAPOTE","BRISAS"]
            elif pcanton == "VALVERDE VEGA":	
                    return ["SARCHÍ NORTE","SARCHÍ SUR","TORO AMARILLO","SAN PEDRO","RODRÍGUEZ"]
            elif pcanton == "UPALA":
                    return ["UPALA","AGUAS CLARAS","SAN JOSE","BIJAGUA","DELICIAS","DOS RÍOS","YOLYLLAL"]
            elif pcanton == "LOS CHILES":
                    return ["LOS CHILES","CAÑO NEGRO","EL AMPARO","SAN JORGE"]
            elif pcanton == "GUATUSO":
                    return ["SAN RAFAEL","BUENAVISTA","COTE","KATIRA"]
#-*-*-*-*-*-*-DISTRITOS POR CANTON DE LA PROVINCIA DE "CARTAGO"-*-*-*-*-*-*#
    elif pProvincia ==3:
            if pcanton == "CARTAGO":
                    return ["ORIENTAL","OCCIDENTAL","CARMEN","SAN NICOLAS","AGUA CALIENTE","GUADALUPE","CORRALILLO","TIERRA BLANCA","DULCE NOMBRE","LLANO GRANDE","QUEBRADILLA"]               
            elif pcanton == "PARAISO":
                    return ["PARAISO","SANTIAGO","OROSI","CACHI","LLANOS DE SANTA LUCIA"]
            elif pcanton == "LA UNION":
                    return ["TRES RIOS","SAN DIEGO","SAN JUAN","SAN RAFAEL","CONCEPCION","DULCE NOMBRE","SAN RAMON","RIO AZUL"]            
            elif pcanton == "JIMENEZ":
                    return ["JUAN VINNAS","TUCURRIQUE","PEJIBAYE"]            
            elif pcanton == "TURRIALBA":	
                    return ["TURRIALBA","LA SUIZA","PERALTA","SANTA CRUZ","SANTA TERESITA","PAVONES","TUIS","TAYUTIC","SANTA ROSA","TRES EQUIS","LA ISABEL","CHIRRIPO"]
            elif pcanton == "ALVARADO":
                    return ["PACAYAS","CERVANTES","CAPELLADES"]
            elif pcanton == "OREAMUNO":
                    return ["SAN RAFAEL","COT","POTRERO CERRADO","CIPRESES","SANTA ROSA"]
            elif pcanton == "EL GUARCO":
                    return ["TEJAR","SAN ISIDRO","TOBOSI","PATIO DE AGUA"]
#-*-*-*-*-*-*-DISTRITOS POR CANTON DE LA PROVINCIA DE HEREDIA-*-*-*-*-*-*#
    elif pProvincia ==4: 
            if pcanton == "HEREDIA":
                    return ["HEREDIA","MERCEDES","SAN FRANCISCO","ULLOA","VARABLANCA"]
            elif pcanton == "BARVA":
                    return ["BARVA","SAN PEDRO","SAN PABLO","SAN ROQUE","SANTA LUCIA","SAN JOSE DE LA MONTANNA"]               
            elif pcanton == "SANTO DOMINGO":	
                    return ["SANTO DOMINGO","SAN VICENTE","SAN MIGUEL","PARACITO","SANTO TOMAS","SANTA ROSA","TURES","PARA"]             
            elif pcanton == "SANTA BARBARA":
                    return ["SANTA BARBARA","SAN PEDRO","SAN JUAN","JESUS","SANTO DOMINGO","PURABA"]
            elif pcanton == "SAN RAFAEL":	
                    return ["SAN RAFAEL","SAN JOSECITO","SANTIAGO","ANGELES","CONCEPCION"]
            elif pcanton == "SAN ISIDRO":
                    return ["SAN ISIDRO","SAN JOSE","CONCEPCION","SAN FRANCISCO"]
            elif pcanton == "BELEN":
                    return ["SAN ANTONIO","RIBERA","ASUNCION"]
            elif pcanton == "FLORES":
                    return ["SAN JOAQUIN","BARRANTES","LLORENTE"]
            elif pcanton == "SAN PABLO":
                    return ["SAN PABLO","RINCON DE SABANILLA"]
            elif pcanton == "SARAPIQUI":
                    return ["PUERTO VIEJO","LA VIRGEN","HORQUETAS","LLANURAS DEL GASPAR","CURENNA"]
#-*-*-*-*-*-*-DISTRITOS POR CANTON DE LA PROVINCIA DE "GUANACASTE"-*-*-*-*-*-*#
    elif pProvincia ==5:
            if pcanton == "LIBERIA":
                    return ["LIBERIA","CAÑAS DULCES","MAYORGA","NACASCOLO","CURUBANDE"]             
            elif pcanton == "NICOYA":	
                    return ["NICOYA","MANSION","SAN ANTONIO","QUEBRADA HONDA","SAMARA","NOSARA","BELEN DE NOSARITA"]  
            elif pcanton == "SANTA CRUZ":
                    return ["SANTA CRUZ","BOLSON","VEINTISIETE DE ABRIL","TEMPATE","CARTAGENA","CUAJINIQUIL","DIRIA","CABO VELAS","TAMARINDO"]
            elif pcanton == "BAGACES":	
                    return ["BAGACES","LA FORTUNA","MOGOTE","RIO NARANJO"]
            elif pcanton == "CARRILLO":
                    return ["FILADELFIA","PALMIRA","SARDINAL","BELEN"]
            elif pcanton == "CAÑAS":
                    return ["CAÑAS","PALMIRA","SAN MIGUEL","BEBEDERO","POROZAL"] 
            elif pcanton == "ABANGARES":	
                    return ["LAS JUNTAS","SIERRA","SAN JUAN","COLORADO"]
            elif pcanton == "TILARAN":
                    return ["TILARAN","QUEBRADA GRANDE","TRONADORA","SANTA ROSA","LIBANO","TIERRAS MORENAS","ARENAL"]
            elif pcanton == "NANDAYURE":
                    return ["CARMONA","SANTA RITA","ZAPOTAL","SAN PABLO","PORVENIR","BEJUCO"]
            elif pcanton == "LA CRUZ":	
                    return ["LA CRUZ","SANTA CECILIA","GARITA","SANTA ELENA"]
            elif pcanton == "HOJANCHA":
                    return ["HOJANCHA","MONTE ROMO","PUERTO CARRILLO","HUACAS","MATAMBU"]
#-*-*-*-*-*-*-DISTRITOS POR CANTON DE LA PROVINCIA DE "PUNTARENAS"-*-*-*-*-*-*#
    elif pProvincia == 6:
            if pcanton == "PUNTARENAS":
                    return ["PUNTARENAS","PITAHAYA","CHOMES","LEPANTO","PAQUERA","MANZANILLO","GUACIMAL","BARRANCA","MONTEVERDE","ISLA DEL COCO","COBANO","CHACARITA","CHIRA","ACAPULCO","EL ROBLE","ARANCIBIA"]
            elif pcanton == "ESPARZA":	
                    return ["ESPIRITU SANTO","SAN JUAN GRANDE","MACACONA","SAN RAFAEL","SAN JERONIMO"]
            elif pcanton == "BUENOS AIRES":
                    return ["BUENOS AIRES","VOLCAN","POTRERO GRANDE","BORUCA","PILAS","COLINAS","CHANGUENA","BRIOLLEY","BRUNKA"]
            elif pcanton == "MONTES DE ORO":
                    return ["MIRAMAR","UNION","SAN ISIDRO"]
            elif pcanton == "OSA":	
                    return ["PUERTO CORTES","PALMAR","SIERPE","BAHIA BALLENA","PIEDRAS BLANCAS"]
            elif pcanton == "AGUIRRE":
                    return ["QUEPOS","SAVEGRE","NARANJITO"]
            elif pcanton == "GOLFITO":
                    return ["GOLFITO","PUERTO JIMENEZ","GUAYCARA","PAVON"]              
            elif pcanton == "COTO BRUS":
                    return ["SAN VITO","SABALITO","AGUABUENA","LIMONCITO","PITTIER","GUTIERREZ BRAUN"]
            elif pcanton == "PARRITA":
                    return ["PARRITA"]
            elif pcanton == "CORREDORES":
                    return ["CORREDOR","LA CUESTA","PASO CANOAS","LAUREL"]               
            elif pcanton == "GARABITO":	
                    return ["JACO","TARCOLES"]
#-*-*-*-*-*-*-DISTRITOS POR CANTON DE LA PROVINCIA DE "LIMON"-*-*-*-*-*-*#
    elif pProvincia == 7:
            if pcanton == "LIMON":
                    return ["LIMON","VALLE LA ESTRELLA","RIO BLANCO","MATAMA"]
            elif pcanton == "POCOCI":	
                    return ["GUAPILES","JIMENEZ","RITA","ROXANA","CARIARI","COLORADO"]
            elif pcanton == "SIQUIRRES":
                    return ["SIQUIRRES","PACUARITO","FLORIDA","GERMANIA","CAIRO","ALEGRIA"]                
            elif pcanton == "TALAMANCA":
                    return ["BRATSI","SIXAOLA","CAHUITA","TELIRE"]                
            elif pcanton == "MATINA":
                    return ["MATINA","BATTAN","CARRANDI"]
            elif pcanton == "GUACIMO":	
                    return ["GUACIMO","MERCEDES","POCORA","RIO JIMENEZ","DUACARI"]
    return ["Sin distritos disponibles en la provincia #"+str(pProvincia)+",cantón:"+pcanton]
"""
Funciones para obtener más datos a rellenar en los campos adicionales del formulario de registrar
"""
"""Funciones para obtener el día, mes y año actual obtenidas de la tarea programada II"""
def obtenerDia():
    """
    Devuelve el día actual en string
    """
    hoy = date.today()#Día actual
    dia = hoy.day
    if dia < 9:
            dia = "0"+str(dia)#dia tipo int
    else:
            dia = str(dia)
    return dia#string dia en formato ## 
def obtenerMes():
    """
    F: devuelve el mes actual en tipo string
    """
    hoy = date.today()#Día actual
    mes = hoy.month #mes tipo int
    if mes < 9:
            mes = "0"+str(mes)#day tipo int
    else:
            mes = str(mes)    
    return mes
def obtenerAnno():
    """
    Devuelve el año actual en tipo entero
    """
    hoy = date.today()#fecha actual
    anno = hoy.year #año tipo int   
    return anno
def obtenerMeses():
    """
    F: devuelve los meses del año en una lista de strings para el combobox
    E: -
    s: mesesL(lista) de los meses del año
    """
    mesesL = []
    for i in range(1,13):
            if i < 10:
                    mesesL.append("0"+str(i))
            else:
                    mesesL.append(str(i))
    return mesesL
def obtenerDiasMes(mes,anno):
    """
    F: devuelve los días que tiene un mes respectivo, en un año sea bisiesto o no
    E: mes y anno (strings) como sus nombres dicen, funcionan para evaluar los días
    S: diasL(lista) de los días respectivos
    """
    mes = int(mes)
    #Array que almacenara los dias que tiene cada mes (si el ano es bisiesto, sumaremos +1 al febrero)
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #Comprobar si el ano es bisiesto y anadir dia en febrero en caso afirmativo
    if int(anno)%4 == 0:
            dias_mes[1] += 1
    #Agregar los días según el mes
    diasL = []
    for i in range(1,dias_mes[mes-1]+1):
            if i < 10:
                    diasL.append("0"+str(i))
            else:
                   diasL.append(str(i)) 
    return diasL
def validarAnno(panno):
    """
    F: valida un año ingresado, mientras no sea mayor al actual y menor a 100 años respecto al año actual
    E: panno(string) año a comparar
    S: True si está en el rango permitido. False si no
    """
    annoActual = obtenerAnno()
    if int(panno) > annoActual:
            return "El año ingresado es mayor que el actual."
    elif int(panno) < annoActual-100:
            return "El año ingresado es demasiado antigüo."
    else:
            return True
"""
Funciones para validar los datos
"""
def normalize(s):
    """
    F: se encargara de normalizar letras con acentos
    E: s(string) cadena de texto a normalizar
    S: s(string) cadena de texto ya normalizada
    Obtenida de: https://micro.recursospython.com/recursos/como-quitar-tildes-de-una-cadena.html
    """
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("ü", "u"),#agregada la ü->u
        ("ñ", "n"),#agregada la ñ->n
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s
def buscarCedula(cedula,lObjetos=[]):
    """
    F: se encarga de verificar la existencia de un objeto con la misma cédula
    E: cedula(string)cédula a buscar
    lObjetos(lista)de objetos donde se revisa la existencia del registro
    Puede recibir la lista que aún no está registrada(listaRegistros->RAM) o consultar en el archivo de registros
    S: objeto(objeto) registro encontrado
    False si no encontró nada
    """
    if lObjetos==[]:
            lObjetos = leerArchivo("archivoRegistro.dat")
    for objeto in lObjetos:
            if cedula == objeto.obtenerCedula():
                    return objeto
    return False
def validarCedula(pcedula):
    """
    F: se encarga de validar la cédula ingresada.
    E: pcedula(string) cédula a validar su formato
    S:
    True si la cédula cumple con su formato,
    False si no
    """
    try:
            if re.match("[1-9]{1}-[0-9]{4}-[0-9]{4}$",pcedula):
                    return True
            elif re.match("\d",pcedula):
                    return "INCOMPLETA"#en caso que la cédula esté incompleta
            return False#no cumple con el formato
    except TypeError:
            return "El dato no es cadena de texto."
def validarApellidos(apellidos,padre,madre):
    """
    F: valida que los apellidos del hijo concuerden con los apellidos de los padres
    E: (todas tipo string):
    apellidos: apellidos del hijo a comparar
    padre: nombre completo del padre del cual extraer su primer apellido
    madre: nombre completo de la madre del cual extraer su primer apellido
    S: True si los apellidos concuerdan. False en el caso contrario
    """
    try:
            apellPadre = padre.split(" ")
            apellMadre = madre.split(" ")
            apellHijo = apellidos.split(" ")
            if len(apellHijo)!=2:
                return "El hijo debe tener a lo sumo dos apellidos."
            elif apellHijo[-2]+" "+apellHijo[-1] != apellPadre[-2]+" "+apellMadre[-2]:
                    return "Los apellidos de los padres deben coincidir con los del hijo."
            return True
    except IndexError:
            return False
def validarNombre(pnombre):
    """
    F:
    Valida que los nombres cumplan con los estándares del registro civil costarricense:
    uno o dos nombres seguido por el apellido materno y paterno
    Los apellidos se validan conforme se ingresa la informacion en obtenerPadres()        
    E: pnombre(string) nombre del nacido
    S:
    True si pasó por por todos los filtros de validacion, en caso contrario
    devuelve el mensaje de validacion
    """
    if pnombre=="":
            return "Por favor ingrese el nombre en la casilla correspondiente."
    pnombre = normalize(pnombre)
    lpnombre = pnombre.split(" ")
    if len(lpnombre)>6 and len(lpnombre)<3:
            return "El nombre debe constituirse máximo por seis elementos y mínimo por tres.\nTodos separados por espacios."
    for i in lpnombre:
            if not re.match("[A-Z]{2,}$",i):
                   return "El nombre ingresado no posee los caracteres alfabéticos requeridos." 
    return True
def validarSexo(psexo):
    """
    F: valida que el tipo de sexo de la persona esté debidamente seleccionado
    E: psexo(string) ya sea M->Masculino ó F->Femenino
    S: True si está seleccionado debidamente, el mensaje de validacion en caso contrario
    """
    if not re.match("[M|F]{1}$",psexo):
            return "Presione el tipo de sexo al que pertenece la persona"
    return True
def validarUbicacion(pUbicacion):
    """
    F: valida que la ubicacion esté debidamente seleccionada por el usuario
    E: pUbicacion(string) posee el formato: PROVINCIA,CANTON,DISTRITO
    El formato se valida en el momento en que se selecciona una opcion del combobox.
    Por lo general, valida que pUbicacion no tenga las minúsculas que tienen las variables de los combobox
    cuando no tienen las ubicaciones debidamente seleccionadas.
    S: true si pUbicacion cumple con el formato, el mensaje de validacion en caso contrario
    """
    if re.search("[a-z]",pUbicacion):
            return "Por favor, ingrese una ubicación seleccionando el cantón o distrito según corresponda."
    return True
def validarFecha(pfecha):
    """
    Valida que la fecha contruida con el formato requerido(DD/MM/AA) esté en el rango permitido
    E: pfecha(fecha a validar)
    S: retorna True si logró pasar la validación, en caso contrario los mensaje correspondientes
    """
    lfecha = pfecha.split("/")
    dia,mes,anno = int(lfecha[0]),int(lfecha[1]),int(lfecha[2])
    mensaje = validarAnno(anno)#valida que el año esté en el rango permitido
    if type(mensaje)!=bool:
            return mensaje
    elif anno == obtenerAnno():
            if mes > int(obtenerMes()):
                    return "El mes es futuro al actual."
            elif mes == int(obtenerMes()):
                    if dia > int(obtenerDia()):
                            return "El día es futuro al actual"
    return True      
def validarNacionalidad(nacion,nacional):
    """
    F: se encarga de validar que la nacionalidad esté de acuerdo a los parámetros recibidos
    E:
    nacion(string) nacionalidad ingresada por el usuario
    nacional(bool) True si es costarricense, False si no
    S: True si los parámetros establecidos concuerdan, El mensaje de validacion respectivo si no.
    """
    if nacion=="":
            return "Ingrese una nacionalidad en la casilla correspondiente."
    if nacional:
            if nacion=="COSTARRICENSE":
                    return True
            else: return "Por la cédula ingresada, debe ser costarricense."
    else:
            if nacion!="COSTARRICENSE":
                    return True
            else: return "Por los datos ingresados, debe ser de nacionalidad extranjera."
def obtenerPadres(lObjetos,sexo):
    """
    F: obtiene los padres a mostrar según el sexo
    E:
    lObjetos(lista) de objeto de donde extraer la información
    sexo(string) M->Masculino F->Femenino
    """
    lPadres = []
    for objeto in lObjetos:
            if objeto.obtenerSexo()==sexo:
                    lPadres.append(objeto.obtenerCedula()+" "+objeto.obtenerNombre())
    return lPadres
def validarPadre(nombre):
    """
    F: se encarga de validar la entrada del padre o madre, tanto si es antecedido con la cédula así como no.
    E: nombre(string) nombre a evaluar:
    puede venir con la cédula o sin ella
    S:
    -objeto.obtenerNombre()[string],True[bool] si escogió a alguien ya registrado
    -validar[string],0[int] si el nombre no es válido
    -nombre[12:],"NER" [strings] si el nombre no está registrado
    -nombre[string],False[bool] si el nombre es extranjero
    """
    validar = validarCedula(nombre[:11])
    if validar==True:
            if nombre[11]!=" ":#si no está el espacio entre la cédula y el nombre
                    return "El nombre junto con la cédula deben estar separados",0
            objeto = buscarCedula(nombre[:11])
            if type(objeto) != bool:
                    if nombre[12:]!=objeto.obtenerNombre():
                            return "El usuario ya está registrado como "+objeto.obtenerNombre(),0
                    #quiere decir que el nombre del padre está registrado y es costarricense
                    return objeto.obtenerNombre(),True
            else:
                    validar=validarNombre(nombre[12:])
                    if type(validar)!=bool:
                            #No pasó la validacion: si tiene una cédula tica, debe poseer el formato del nombre de un tico
                            return validar,0
                    #quiere decir que la cédula y el nombre es costarricense pero no está registrado                        
                    return nombre[12:],"NER"
    elif validar=="INCOMPLETA":
            return "El nombre comienza con dígitos sin sentido. Por favor, revise bien.",0
    else:
            #quiere decir que no es costarricense, devuelve el nombre ingresado
            return nombre,False
#-*-*-*-*-*-*-*-*-*FIN DE LAS FUNCIONES PARA REGISTRAR-*-*-*-*-*-*-*-*-*#               
def validarArchivo():
    """Funcionalidad: Valida que todo lo que está en el archivo esté en el formato correspondiente
    Entradas: ----
    Salidas: True si todo está correcto y False de lo contrario"""
    listaUsuarios=[]
    archivo= open ('usuarios.txt','r')
    for usuarios in archivo:
        if usuarios[-1:]=="\n":
            linea=usuarios[:-1]
            listaUsuarios.append(linea.split("_"))
        else:
            listaUsuarios.append(usuarios.split("_"))
    archivo.close()
    for registrados in listaUsuarios:
        if re.match("\w{5,}@\w",registrados[0]) and re.match('^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{5,15}$',registrados[1]):
            pass
        else:
            return False
    return True
