class ArchivoPrestamos:
    def __init__(self):
        self.nombreArchivo = ''
        self.columnas = ""
        self.datos = ""

    def crearArchivo(self):
        self.archivo = open(self.nombreArchivo,"w")

    def setColumnas(self, columnas):
        self.archivo.write(columnas)

    def setNombre(self,nombre):
        self.nombreArchivo = nombre

    def setDatos(self, datos):
        self.archivo.write(datos)

    