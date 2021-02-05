from mysql.connector.connection import MySQLConnection
from datetime import datetime
class MySQL:
    def __init__(self):
        self.host="localhost"
        self.user="root"
        self.password=""
        self.database="Examen"
        self.listaPersonas = []
        self.listaPrestamos = []
        self.listaMateriales = []

    def Conexion(self):
        self.mydb = MySQLConnection(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        return "Conexion a MySQL exitosa"
#MySQL Personas--------------------------------------------------------------------
    def createTablePerson(self):
        self.mycursor = self.mydb.cursor()
        try:
            self.mycursor.execute("create table Personas (id int primary key, nombre varchar(25) not null, apellidoPaterno varchar(25) not null, apellidoMaterno varchar(25) not null,correo varchar(50) not null, telefono bigInt not null, edad int not null)")
        except: "No se pudo crear"
        return "Tabla creada"

    def getMaxID(self):
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute("select max(id) from Personas")
        self.myresult = self.mycursor.fetchall()
        for x in self.myresult:
            self.y = x[0]
        return self.y

    def insertarPersonas(self,datos):
        self.sql = "insert into Personas (id, nombre, apellidoPaterno, apellidoMaterno,correo,telefono, edad) values (%s,%s,%s,%s,%s,%s,%s)"
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(self.sql,datos)
        self.mydb.commit()
        return "Persona insertada correctamente a MySQL"
#---------------------------------------------------------------------------------------
#MySQL Prestamos--------------------------------------------------------------------
    def createTablePrestamos(self):
        self.mycursor = self.mydb.cursor()
        try:
            self.mycursor.execute("create table Prestamos (id int primary key, id_persona int not null, nombre_persona varchar(25) not null,correo_persona varchar(25) not null, fechaPrestamo varchar(50) not null, fechaDevolucion varchar(50)")
        except: "No se pudo crear la tabla"
        return "tabla prestamos creada"

    def insertarPrestamos(self,datos):
        self.sql = ("insert into Prestamos (id, id_persona, nombre_persona, correo_persona, fechaPrestamo, fechaDevolucion) values (%s,%s,%s,%s,%s,%s)")
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(self.sql,datos)
        self.mydb.commit()
        return "Prestamo insertado en MySQL"

    def getMaxIDPrestamo(self):
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute("select max(id) from Prestamos")
        self.myresult = self.mycursor.fetchall()
        for x in self.myresult:
            self.y = x[0]
        return self.y
#---------------------------------------------------------------------------------------
#MySQL Materiales--------------------------------------------------------------------
    def createTablaMateriales(self):
        self.mycursor = self.mydb.cursor()
        try:
            self.mycursor.execute("create table Materiales (id_prestamo int not null,cantidad int not null, nombreMaterial varchar(25) not null)")
        except: "No se pudo crear la tabla"
        return "Tabla Materiales creada"

    def insertarMateriales(self,datos):
        self.sql = "insert into Materiales (id_prestamo, cantidad, nombreMaterial) values (%s,%s,%s)"
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(self.sql,datos)
        self.mydb.commit()
        return "Material registrado en MongoDB"
#---------------------------------------------------------------------------------------
#MySQL Consultas--------------------------------------------------------------------
    def verPersonas(self):
        self.sql = "SELECT *FROM Personas"
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(self.sql)
        self.myresult = self.mycursor.fetchall()
        self.listaPersonas.append(self.myresult)
        for self.personas in self.listaPersonas:
            return self.personas
#---------------------------------------------------------------------------------------
    def verPrestamos(self):
        self.sql = "SELECT *FROM Prestamos"
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(self.sql)
        self.myresult = self.mycursor.fetchall()
        self.listaPrestamos.append(self.myresult)
        for self.prestamos in self.listaPrestamos:
            return self.prestamos
#---------------------------------------------------------------------------------------
    def verMateriales(self):
        self.sql = "SELECT *FROM Materiales"
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(self.sql)
        self.myresult = self.mycursor.fetchall()
        self.listaMateriales.append(self.myresult)
        for self.materiales in self.listaMateriales:
            return self.materiales
#Devolucion-------------------------------------------------------------------------
    def registrarDevolucion(self,id_persona):
        self.ahora = datetime.now()
        self.fecha = self.ahora.strftime("%Y-%m-%d %H:%M:%S")
        #self.sql = "update prestamos set fechaDevolucion ="+self.fecha+"where prestamos.id_persona ="+str(id_persona)
        self.sql = "UPDATE prestamos SET fechaDevolucion = %s WHERE id_persona = %s"
        self.update = (self.fecha, id_persona)
        #self.sql = "update prestamos set fechaDevolucion ='devuelto' where id_persona=1"
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(self.sql,self.update)
        self.mydb.commit()
#---------------------------------------------------------------------------------------
