import sqlite3
import os

def conectar():
    conexion = sqlite3.connect("agenda.db")
    cursor = conexion.cursor()
    return  conexion,cursor

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

def modificar(id,nombre,apellido,telefono,email):
    conexion, cursor = conectar()
    sql = "UPDATE agenda SET Nombre = '"+nombre+"',Apellido= '"+apellido+"',Telefono= '"+telefono+"',Email= '"+email+"' WHERE id ="+str(id)         
    cursor.execute(sql)
    cursor.close()
    conexion.commit()
    conexion.close()

def borrar(ID):
    conexion, cursor = conectar()
    sql = "DELETE from agenda WHERE id="+str(ID)
    cursor.execute(sql)
    cursor.close()
    conexion.commit()
    conexion.close()
    
# def consultarId():
#     conexion, cursor = conectar()
#     cursor.execute("SELECT id,Nombre,Apellido,Telefono,mail from agenda")
#     print(type(cursor))
#     print(cursor)
#     conexion.close()
    
def contactoId(ID):
    conexion, cursor = conectar()
    sql="SELECT * from agenda WHERE id="+str(ID)
    cursor.execute(sql)
    contacto = cursor.fetchall()
    conexion.close
    return contacto
    