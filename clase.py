#Elaborado por Sara Segura, Andrey Picado
#Fecha de creación: 06/08/2020 10:25am
#Ultima modificación: 06/08/2020
#Versión: 3.8.5
#$-$-$-$-$-$-$-$-$-$-Definición de la clase$-$-$-$-$-$-$-$-$-$-
class Persona:
    """
    Declaración de la clase de Persona
    Datos necesarios para la creación del objeto:
    cedula,nombre,sexo(M ó F),ubicacion(PROVINCIA,CANTON,DISTRITO),
    fechaN(fecha de nacimiento DD/MM/AA),
    padre,nacionalidadP (nombre y nacionalidad del padre)
    madre,nacionalidadM (nombre y nacionalidad de la madre)
    Todas como tipo string
    Métodos necesarios:
    obtener+[A-Z]tributo()
    """
    def __init__(self,cedula,nombre,sexo,ubicacion,fechaN,padre,nacionalidadP,madre,nacionalidadM):
        self.cedula=cedula
        self.nombre=nombre
        self.sexo=sexo
        self.ubicacion=ubicacion
        self.fechaN=fechaN
        self.padre=padre
        self.nacionalidadP=nacionalidadP
        self.madre=madre
        self.nacionalidadM=nacionalidadM       
    def obtenerCedula(self):
        return self.cedula
    def obtenerNombre(self):
        return self.nombre
    def obtenerSexo(self):
        return self.sexo
    def obtenerUbicacion(self):
        return self.ubicacion
    def obtenerFechaN(self):
        return self.fechaN
    def obtenerPadre(self):
        return self.padre
    def obtenerNacionalidadP(self):
        return self.nacionalidadP
    def obtenerMadre(self):
        return self.madre
    def obtenerNacionalidadM(self):
        return self.nacionalidadM
