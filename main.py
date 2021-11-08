import cx_Oracle

connection = cx_Oracle.connect("system", "Tardes", "localhost/XE")

cursor = connection.cursor()
try:

    apeDoctor = input("Apellido Doctor:")
    resultado = cursor.var(cx_Oracle.NUMBER)

    args = (apeDoctor,resultado)
    cursor.callproc('BORRAR_DOCTOR', args)

    print(f"Doctores borrados:{int(resultado.getvalue())}")

except connection.Error as error:
    print("Error: ", error)
cursor.close()
connection.close()
