import mysql.connector

miBD = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password="",
  database = "banda_rock"
)
mySQLcursor = miBD.cursor()

mySQLcursor.execute("ALTER TABLE bandas MODIFY COLUMN id_banda INT(10) UNSIGNED")
miBD.commit()
mySQLcursor.execute("ALTER TABLE bandas MODIFY COLUMN id_banda INT(10) UNSIGNED AUTO_INCREMENT")
miBD.commit()


def READ(nom):
    mySQLcursor.execute(("SELECT * FROM "+ str(nom)))
    resultado = mySQLcursor.fetchall()
    for x in resultado:
        print(x)

def CREATE(nom):
    mySQLcursor.execute("INSERT INTO `bandas` (`id_banda`, `Nombre_Banda`) VALUES (NULL, '"+str(nom)+"')")
    miBD.commit()
    print(str(nom)+" Ha sido agregado")

def DELETE(num):
    mySQLcursor.execute("DELETE FROM `bandas` WHERE `bandas`.`id_banda` = "+str(num))
    miBD.commit()
    print("El registro con Index "+str(num)+" Ha sido Eliminado")
    
def UPDATE(num,nom):
    mySQLcursor.execute("UPDATE `bandas` SET `Nombre_Banda` = '"+str(nom)+"' WHERE `bandas`.`id_banda` = "+str(num))
    miBD.commit()
    print("El registro con Index "+str(num)+" Ha sido Actualizada por: "+str(nom))

Op="R"
op=0
while(Op=="R"):
    READ("bandas")
    print("Seleccione una opcion: ")
    print("1. Create\n2. Delete\n3. Update\n4. Salir")
    op=int(input("Eleccion: "))
    if op<1 or op>4:
        print("Elija una opción valida")
    else:
        if op ==1:
            nom=str(input("Ponga el Nombre de la banda que desea agregar: "))
            CREATE(nom)
        if op ==2:
            num=int(input("Ponga el ID de la banda que desea Eliminar: "))
            DELETE(num)
        if op ==3:
            num=int(input("Ponga el ID de la banda que desea modificar: "))
            nom=str(input("Ponga el Nombre de la banda que desea poner en su lugar: "))
            UPDATE(num,nom)
        if op ==4:
            break
        



