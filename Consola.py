from ArchivoMateriales import ArchivoMateriales
from ArchivoPrestamos import ArchivoPrestamos
from Persona import *
from Prestamo import *
from MySQL import *
from ListaMaterial import *
from datetime import datetime
from ArchivoPersonas import *
from MongoDB import *

print("-------Club Deportivo--------")
print("| 1 | Registrar Persona     |")
print("| 2 | Guardar Persona       |")
print("| 3 | Registrar prestamo    |")
print("| 4 | Registrar Productos   |")
print("| 5 | Guardar Prestamo      |")
print("| 6 | Registrar Devolución  |")
print("| 7 | Crear Excel Personas  |")
print("| 8 | Crear Excel Prestamos |")
print("| 9 | Crear Excel Materiales|")
print("| 10| Cerrar Aplicación     |")
print("-----------------------------")
#Conexion a base de datos
newdb = MySQL()
print(newdb.Conexion())
newdb.createTablePerson()
newdb.createTablaMateriales()
#------------------------------
#Conexion a MongoDB
newMongo = MongoDB()
print(newMongo.mongoConexion())
#------------------------------
numero = 0
respuesta = "s"
#--------------------------------------------------------------------------------------  
while numero != 10:
    numero = int(input("¿Que deseas realizar? "))
    if (numero == 1):
        while respuesta != "n":
            print("Has seleccionado Registrar persona.")
            newPersona = Persona()
            ide = newdb.getMaxID()
            print(ide)
            print("Ultimo ID:",newdb.getMaxID())
            if (ide==None):
                ide = 0
            newPersona.id = ide + 1
            newPersona.nombre = input("Ingresa el nombre: ")
            newPersona.apellidoP = input("Ingresa el apellido Paterno: ")
            newPersona.apellidoM = input("Ingresa el apellido Materno: ")
            newPersona.edad = input("Ingresa la edad: ")
            newPersona.correo = input("Ingresa el correo electronico: ")
            newPersona.telefono = input("Ingresa el numero telefonico: ")
            newPersona.addPerson(newPersona)
            print(newPersona.getLista())
            respuesta = input("¿Deseas registrar otra persona? (s/n): ")
#--------------------------------------------------------------------------------------       
    elif (numero==2):
#Guardar en MySQL----------------------------------------------------------------------
        print("Has seleccionado guardar personas.")
        datosPersonas = Persona()
        datos = datosPersonas.getLista()
        for registro in datos:
            idPe = str(registro.id)
            name = registro.nombre
            apellidoPat = registro.apellidoP
            apellidoMat = registro.apellidoM
            correoPe = registro.correo
            telePe = registro.telefono
            age = str(registro.edad)
            datosSend = (idPe, name, apellidoPat, apellidoMat, correoPe,telePe, age)
            newdb.insertarPersonas(datosSend)
            print(newdb.insertarPersonas,"Insertados")
#Guardar en MongoBD--------------------------------------------------------------------
        datosMongo = datosPersonas.getLista()
        newMongo.createDataBase(input("Ingresa el nombre de la base de Datos: "))
        newMongo.crearTabla(input("Ingresa el nombre de la Tabla: "))
        for registrosMongo in datosMongo:
            idPeM = str(registrosMongo.id)
            nameM = registrosMongo.nombre
            apellidoPM = registrosMongo.apellidoP
            apellidoMM = registrosMongo.apellidoM
            correoPeM = registrosMongo.correo
            telefonoPeM = registrosMongo.telefono
            ageM = str(registrosMongo.edad)
            newMongo.insertDatosPersona(idPeM, nameM, apellidoPM, apellidoMM,correoPeM,telefonoPeM, ageM)
            print(newMongo.insertDatosPersona)
#--------------------------------------------------------------------------------------  
    elif (numero==3):
        while respuesta != "n":
            print("Has seleccionado registrar prestamo.")
            newPrestamo = Prestamo()
            ide = newdb.getMaxIDPrestamo()
            print(ide)
            print("Ultimo ID:",newdb.getMaxIDPrestamo())
            if (ide==None):
                ide = 0
            newPrestamo.id = ide + 1
            newPrestamo.id_persona = input("Ingresa el id de la persona: ")
            newPrestamo.nombre_Persona = input("Ingresa el nombre de la persona: ")
            newPrestamo.correo_persona = input("Ingresa el correo de la persona: ")
            ahora = datetime.now()
            fecha = ahora.strftime("%Y-%m-%d %H:%M:%S")
            newPrestamo.fechaPrestamo = fecha
            newPrestamo.addPrestamos(newPrestamo)
            print(newPrestamo.getPrestamos())   
            respuesta = input("¿Deseas registrar otro prestamo? (s/n): ")
#--------------------------------------------------------------------------------------
    elif (numero == 4):
        materialesC = ListaMaterial()
        print("Has seleccionado registrar productos prestados.")
        cant = 0
        i = 0
        cant = int(input("¿Cuantos productos prestaras?: "))
        while i < cant:
            newMaterial = ListaMaterial()
            newMaterial.id_prestamo = int(input("Ingresa el ID del prestamo: "))
            newMaterial.nombreMaterial = input("Ingresa el nombre del producto: ")
            newMaterial.cantidad = int(input("¿Cuantas piezas?: "))
            materialesC.addMaterial(newMaterial)
            i += 1
        print(materialesC.getMaterial())
#-------------------------------------------------------------------------------------- 
    elif (numero == 5):
#Guardar en MySQL----------------------------------------------------------------------
        print("Has seleccionado guardar prestamos y materiales.")
        datosPrestamos = Prestamo()
        datos = datosPrestamos.getPrestamos()
        for registro in datos:
            idPr = str(registro.id)
            id_Pe = str(registro.id_persona)
            name_Pe = registro.nombre_Persona
            correo = registro.correo_persona
            fPre = registro.fechaPrestamo
            fDev = registro.fechaDevolucion
            datosPrestamosSend = (idPr, id_Pe, name_Pe,correo, fPre, fDev)
            newdb.insertarPrestamos(datosPrestamosSend)
            print(newdb.insertarPrestamos,"Insertados")
#Guardar en MongoDB----------------------------------------------------------------------
        newMongo.createDataBase(input("Ingresa el nombre de la base de Datos: "))
        newMongo.crearTabla(input("Ingresa el nombre de la Tabla: "))
        datosMongo = datosPrestamos.getPrestamos()
        for registrosMongo in datosMongo:
            idPrM = str(registrosMongo.id)
            nameM = registrosMongo.nombre_Persona
            mailto = registrosMongo.correo_persona
            fPreM = registrosMongo.fechaPrestamo
            fDevM = registrosMongo.fechaDevolucion
            newMongo.insertDatosPrestamos(idPrM,nameM,mailto,fPreM,fDevM)
            print(newMongo.insertDatosPrestamos)

#---------------------------------------------------------------------------------------
#Guardar en MySQL----------------------------------------------------------------------
        datosMateriales = ListaMaterial()
        materiales = datosMateriales.getMaterial()
        for registros in materiales:
            idPres = str(registros.id_prestamo)
            nameMat = registros.nombreMaterial
            cantidad = registros.cantidad
            datosMaterialesSend = (idPres, cantidad, nameMat)
            newdb.insertarMateriales(datosMaterialesSend)
            print(newdb.insertarMateriales,"Insertados")
#Guardar en MongoDB----------------------------------------------------------------------
        newMongo.createDataBase(input("Ingresa el nombre de la base de Datos: "))
        newMongo.crearTabla(input("Ingresa el nombre de la Tabla: "))
        datosMongo = datosMateriales.getMaterial()
        for registrosMongo in datosMongo:
            nameM = registrosMongo.nombreMaterial
            cantidad = registrosMongo.cantidad
            newMongo.insertDatosMateriales(cantidad,nameM)
            print(newMongo.insertDatosMateriales)
#--------------------------------------------------------------------------------------  
    elif (numero == 6):
        devolucion = Prestamo()
        x = int(input("Ingresa el id: "))
        devolucion.devolver(x)
        print(devolucion.getPrestamos())
#--------------------------------------------------------------------------------------
    elif (numero == 7):
        PersonasArchivo = Persona()
        print("Has seleccionado crear archivo Personas.")
        archivo = ArchivoPersonas()
        archivo.nombreArchivo = 'Registro_Personas.csv'
        archivo.crearArchivo()
        columnas = ("id, nombre, apellidoPaterno, apellidoMaterno, correo, telefono edad\n")
        archivo.setColumnas(columnas)
        datos = PersonasArchivo.getLista()
        for registros in datos:
            idPe = str(registros.id)
            name = registros.nombre
            paterno = registros.apellidoP
            materno = registros.apellidoM
            correo = registros.correo
            telefono = registros.telefono
            age = str(registros.edad)
            filas = (idPe+","+name+","+paterno+","+materno+","+correo+","+telefono+","+age)
            archivo.setDatos(filas)
#--------------------------------------------------------------------------------------
    elif (numero == 8):
        print("Has seleccionado crear el archivo Prestamos.")
        PrestamoArchivo = Prestamo()
        archivo = ArchivoPrestamos()
        archivo.nombreArchivo = 'Registro_Prestamos.csv'
        archivo.crearArchivo()
        columnas = ("id, id_persona, nombre_persona, correo_Personas, fechaPrestamo, fechaDevolucion\n")
        archivo.setColumnas(columnas)
        datos = PrestamoArchivo.getPrestamos()
        for registros in datos:
            idPre = str(registros.id)
            id_Pe = str(registros.id_persona)
            name = registros.nombre_Persona
            correoPPres = registros.correo_Persona
            prestamo = str(registros.fechaPrestamo)
            devolucion = str(registros.fechaDevolucion)
            filas = (idPre+","+id_Pe+","+name+","+correoPPres+","+prestamo+","+devolucion)
            archivo.setDatos(filas)
#--------------------------------------------------------------------------------------
    elif (numero == 9):
        print("Has seleccionado crear el archivo Materiales.")
        MaterialesArchivo = ListaMaterial()
        archivo = ArchivoMateriales()
        archivo.nombreArchivo = 'Registro_Materiales.csv'
        archivo.crearArchivo()
        columnas = ("id_prestamo, cantidad, Material\n")
        archivo.setColumnas(columnas)
        datos = MaterialesArchivo.getMaterial()
        for registros in datos:
            id_Pre = str(registros.id_prestamo)
            cant = str(registros.cantidad)
            name = registros.nombreMaterial
            filas = (id_Pre+","+cant+","+name)
            archivo.setDatos(filas)
        pass
#--------------------------------------------------------------------------------------
    elif (numero == 10):
        print("Cerrando...")
#--------------------------------------------------------------------------------------
    else:
        print("Opción no valida.")