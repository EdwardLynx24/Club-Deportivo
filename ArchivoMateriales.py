class ArchivoMateriales:
    def __init__(self):
        self.nombreArchivo = ''
        self.columnas = ""
        self.filas = ""
    
    def setNombre(self,nombre):
        self.nombreArchivo = nombre

    def crearArchivo(self):
        self.archivo = open(self.nombreArchivo,"w")

    def setColumnas(self,columnas):
        self.archivo.write(columnas)

    def setDatos(self, datos):
        self.archivo.write(datos)