#Elaborado por Andrey Picado Arias, Sara Segura Artavia
#Fecha de creación: 01/08/2020 7:50pm
#Ultima modificación: 04/08/2020
#Version de python: 3.8.5
import pickle #libreria para archivos
#Definición de funciones de archivos
#Todas deben recibir un nombre de archivo a manejar: nArchivo.
def leerArchivo(nArchivo):
    """
    F: se encarga de leer el contenido de un archivo(tomando en cuenta que es una lista)
    E: nArchivo(string) nombre del archivo a leer en el directorio actual
    S: lectura(lista) datos en tipo lista leídos
    """
    referencia = open(nArchivo,"rb")# abrir archivo para leer datos
    lectura = []#en caso que la lista esté creada pero no llena
    while True:
        try: #controlar EOF
            lectura=pickle.load(referencia)# leer datos
        except EOFError:
            break             
    referencia.close()
    return lectura
def crearArchivo(nArchivo):
    """
    Se encarga de crear el archivo según el nombre dado en caso que no exista
    E: nArchivo(string) nombre del archivo a crear
    S: referencia(<class '_io.TextIOWrapper'><_io.TextIOWrapper name='nArchivo' mode='w' encoding='cp1252'>) archivo creado
    """
    referencia = open(nArchivo,"w") # crear el archivo  
    referencia.close()# cerrar archivo
    return referencia
def actualizarArchivo(informacion,nArchivo):
    """
    Se encarga de actualizar el archivo según la información y el nombre dado
    E: nArchivo(string) nombre del archivo a crear, informacion(se asume lista) información a actualizar en el archivo
    S: referencia(<class '_io.BufferedWriter'><_io.BufferedWriter name='nArchivo'>) confirmación de actualización
    """
    referencia = open(nArchivo,"wb")
    pickle.dump(informacion,referencia)
    referencia.close()
    return referencia
def verificarArchivo(nArchivo):
    """
    Función: verifica que el archivo con el registra existe, si no, crea uno nuevo
    Entrada: nArchivo(string) nombre del archivo a verificar
    Salida: ref(lista): devuelve la lista si existe el archivo, retorna False si no existe el archivo
    """
    try:
        ref = leerArchivo(nArchivo)
        return ref
    except IOError:
        ref = crearArchivo(nArchivo)
        return False
