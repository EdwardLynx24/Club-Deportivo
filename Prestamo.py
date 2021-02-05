from datetime import datetime
class Prestamo:
    prestamos = []

    def __init__(self):
        self.id = 0
        self.id_persona = 0
        self.nombre_Persona = ""
        self.correo_persona = ""
        self.fechaPrestamo = ""
        self.fechaDevolucion = ""
    
    def __repr__(self):
        return str(self.__dict__)
    
    def setDatos(self, id_persona,nombrePersona,correoPersona, fechaPrestamo,nombreMaterial,cantidad, material, fechaDevolucion):
        self.id_persona=id_persona
        self.fechaPrestamo=fechaPrestamo
        self.nombre_Persona=nombrePersona
        self.correo_persona=correoPersona
        self.nombreMaterial=nombreMaterial
        self.cantidad=cantidad
        self.material=material
        self.fechaDevolucion=fechaDevolucion

    def __str__(self):
        if(len(self.prestamos)>0):
            return str(len(self.prestamos)) + "registros"
    
    def addPrestamos(self, prestamo):
        self.prestamos.append(prestamo)
    '''
    def addMaterial(self,material):
        self.material.append(material)
    '''
    def getPrestamos(self):
        return self.prestamos
    '''
    def getMaterial(self):
        return self.material
    '''
    def devolver(self,ide=None):
        for x in self.prestamos:
            try:
                if(x.id==ide):
                    ahora = datetime.now()
                    x.fechaDevolucion = ahora.strftime("%Y-%m-%d %H:%M:%S")
            except:
                return "ID erroneo"
