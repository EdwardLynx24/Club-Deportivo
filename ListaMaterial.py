class ListaMaterial:
    material = []
    def __init__(self):
        self.id_prestamo = 0
        self.nombreMaterial = ""
        self.cantidad = 0

    def __repr__(self):
        return str(self.__dict__)

    def setDatos(self, id_prestamo, nombreMaterial,cantidad):
        self.id_prestamo=id_prestamo
        self.nombreMaterial=nombreMaterial
        self.cantidad=cantidad
    
    def addMaterial(self,Materiales):
        self.material.append(Materiales)

    def getMaterial(self):
        return self.material