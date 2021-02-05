class ArchivoPersonas:
    def __init__(self):
        self.nombreArchivo = ''
        self.columnas = ""
        self.datos = ""

    def setNombreArchivo(self,nombre):
        self.nombreArchivo = nombre

    def setColumnas(self,columnas):
        self.archivo.write(columnas)
        
    def crearArchivo(self):
        self.archivo = open(self.nombreArchivo,"w")
    
    def setDatos(self, datos):
        self.archivo.write(datos)

    