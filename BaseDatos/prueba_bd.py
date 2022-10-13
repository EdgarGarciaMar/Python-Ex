import psycopg2

conexion = psycopg2.connect(
    user = "postgres",
    password = "1234",
    host = "localhost",
    port = "5432",
    database = "test_db"
)

try:
    with conexion:
        with conexion.cursor() as cursor: #abre y cierra el cursor


            #Sentencias preparadas
            sentencia2 = "SELECT * FROM persona WHERE id_persona = %s" # place holder
            #se debe pasar una tupla al place holder
            id_persona = 1 # A qui se pide el dato
            cursor.execute(sentencia2,(id_persona,))
            registroUnico = cursor.fetchone() # solo un registro

            #Insert
            insert = "INSERT INTO persona(nombre, apellido, email) VALUES (%s,%s,%s)"
            valores = ("carlos","lara", "carlos@gmail.com")
            cursor.execute(insert,valores)
            #conexion.commit() #sin usar manejo de recursos with

            registrosNuevos = cursor.rowcount
            print(f"Registros Insertados : {registrosNuevos}" )


            #update
            update = "UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s"
            valoresUpdate = ("carloszz", "Lorenzo", "carlos@gmail.com",2)
            cursor.execute(update, valoresUpdate)
            registrosUpdate = cursor.rowcount
            print(f"Registros Update : {registrosUpdate}" )


            #eliminar
            delete = "DELETE FROM persona WHERE id_persona = %s"
            ValorDelete = (5,)#Cambiar el valor
            cursor.execute(delete,ValorDelete)
            registrosdel = cursor.rowcount
            print(f"Registros Delete : {registrosdel}")

            # sentencia codigo duro
            sentencia = "SELECT * FROM persona"
            cursor.execute(sentencia)
            registros = cursor.fetchall()  # todos los registros

            #prints
            print(registros)
            print(registroUnico)
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    conexion.close() #Cerramos la conexion manualmente