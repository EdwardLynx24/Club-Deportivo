import pymongo
from datetime import datetime

class MongoDB:
    def __init__(self):
        #LocalHost
        self.Mongo_Host="cluster0.0fjcd.mongodb.net"
        self.Mongo_Port="27017"
        self.Mongo_User="user"
        self.Mongo_Password="user"
        self.Mongo_TimeOut=1000
    
    def mongoConexion(self):
        self.Mongo_URI="mongodb+srv://user:user@cluster0.0fjcd.mongodb.net/test"
        #self.Mongo_URI="mongodb://"+self.Mongo_Host+":"+self.Mongo_Port+"/"
        try:
            #self.cliente = pymongo.MongoClient(self.Mongo_URI)
            self.cliente = pymongo.MongoClient(self.Mongo_URI)
            self.cliente.server_info()
            return "Conexion a MongoDB Exitosa"
        except pymongo.errors.ConnectionFailure as errorConexion:
           return "No se pudo realizar la conexion a MongoDB "+errorConexion

    def createDataBase(self,nombre):
        try:
            self.mydb=self.cliente[nombre]
            return "Base de datos creada"
        except:
            return "No se pudo crear la base de datos"

    def crearTabla(self,nombre):
        try:
            self.tabla = self.mydb[nombre]
        except:
            return "nel, no ser armo la tabla"

    def insertDatosPersona(self,id,nombre,apellidoP, apellidoM,correoP,telefonoP, edad):
        try:
            self.datos = {"ID": id,"Nombre": nombre,"Apellido Paterno": apellidoP, "Apellido Materno": apellidoM,"Correo": correoP,"Telefono":telefonoP, "Edad": edad}
            self.datosIns = self.tabla.insert_one(self.datos)
            return "Persona insertada a MongoDB"
        except:
            return "No se inserto nada"

    def insertDatosPrestamos(self,id,name,correo,fPre,fDev):
        try:
            self.datos = {"ID": id, "Nombre_Persona":name,"Correo_Persona":correo,"Fecha_Prestamo":fPre,"Fecha_Devolucion":fDev}
            self.datosIns = self.tabla.insert_one(self.datos)
            return "Prestam insertado a MongoDB"
        except:
            return "No se inserto nada"

    def insertDatosMateriales(self,cantidad,material):
        try:
            self.datos = {"Material Prestado":material,"Cantidad de Material":cantidad}
            self.datosIns = self.tabla.insert_one(self.datos)
            return "Materiales registrados en MongoDB"
        except:
            return "No se inserto nada."

    def actualizarFecha(self,id):
        try:
            self.myquery = {"ID": str(id)}
            self.ahora = datetime.now()
            self.fecha = self.ahora.strftime("%Y-%m-%d %H:%M:%S")
            self.newValue = {"$set":{"Fecha_Devolucion":self.fecha}}
            self.tabla.update_one(self.myquery,self.newValue)
            return "Actualizacion exitosa"
        except:
            return "no se actualizo"
        