import sqlite3 # Inportamos el modulo de SQLite.
import os # Inportamos el modulo Con las funciones el sistema operativo .

#Establecemos la conexion con la abase de datos.
def conectar():
    conexion = sqlite3.connect("agenda.db")
    cursor = conexion.cursor()
    return  conexion,cursor

# Creamos la base de datos con las entidades. Si la base de datos no existe la crea.
def crearTabla():
    conexion, cursor = conectar()
    sql = """
        CREATE TABLE IF NOT EXISTS agenda(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            Nombre VARCHAR(20) NOT NULL,
            Apellido VARCHAR(20) NOT NULL,
            Telefono VARCHAR(14) NOT NULL,
            Email VARCHAR(20) NOT NULL
        )
    """
    if cursor.execute(sql):
        print("Tabla creada")
    else:
        print("No fue posible crear la tabla")
    conexion.close()

# Creramos el metodo para insertar datos.
def insertar(datos):
    conexion, cursor = conectar()
    sql = """
    INSERT INTO agenda(Nombre,Apellido,Telefono,Email) VALUES (?,?,?,?)
    """
    if (cursor.execute(sql,datos)):
        print("Datos guardados")
    else:
        print("No se pudieron guardar los datos")
    conexion.commit()
    conexion.close()
    
# Creramos el metodo para consultar o recuperar los datos.
def consultar():
    conexion, cursor = conectar()
    sql= "SELECT id,Nombre,Apellido,Telefono,Email from agenda"
    cursor.execute(sql)
    listado = []
    for fila in cursor:
        listado.append(fila)
    listado.sort()
    conexion.close()
    return listado

# Creramos el metodo para modificar los datos.
def modificar(id,nombre,apellido,telefono,email):
    conexion, cursor = conectar()
    sql = "UPDATE agenda SET Nombre = '"+nombre+"',Apellido= '"+apellido+"',Telefono= '"+telefono+"',Email= '"+email+"' WHERE id ="+str(id)         
    cursor.execute(sql)
    cursor.close()
    conexion.commit()
    conexion.close()

# Creramos el metodo para borrar datos.
def borrar(ID):
    conexion, cursor = conectar()
    sql = "DELETE from agenda WHERE id="+str(ID)
    cursor.execute(sql)
    cursor.close()
    conexion.commit()
    conexion.close()
    
# Creramos el metodo para borrar datos.   
def contactoId(ID):
    conexion, cursor = conectar()
    sql="SELECT * from agenda WHERE id="+str(ID)
    cursor.execute(sql)
    contacto = cursor.fetchall()
    conexion.close
    return contacto
    