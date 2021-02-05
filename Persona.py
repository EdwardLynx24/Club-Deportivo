class Persona:
    personas = []
    def __init__(self):
        self.id = 0
        self.nombre = ""
        self.apellidoP = ""
        self.apellidoM = ""
        self.correo = ""
        self.telefono = ""
        self.edad=0

    def __repr__(self):
        return str(self.__dict__)

    def setDatos(self,nombre,appelidoP,apellidoM,correo,telefono,edad):
        self.nombre=nombre
        self.apellidoP=appelidoP
        self.apellidoM=apellidoM
        self.edad=edad
        self.correo=correo
        self.telefono=telefono
        
    def __str__(self):
        if(len(self.personas)>0):
            return str(len(self.personas)) + "registros"
        return self.nombre + " " +str(self.edad)

    def getDatos(self):
        return self.nombre,self.apellidoP,self.apellidoM,self.edad

    def addPerson(self,newPersona):
        self.personas.append(newPersona)
        return len(self.personas)

    def deletePerson(self,index):
        self.personas.pop(index)
        return len(self.personas)

    def updatePerson(self,index,newPersona):
        self.personas[index]=newPersona
        return True
        
    def getPersonas(self,index=None,nombre=None):
        try:
            if(index!=None):
                return self.personas[index]
            else:
                if(nombre!=None):
                    for pers in self.personas:
                        if(pers.nombre==nombre):
                            return pers
        except:
            return "ID fuera del indice"
    def getLista(self):
        return self.personas