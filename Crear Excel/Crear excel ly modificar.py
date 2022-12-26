import xlsxwriter

workbook = xlsxwriter.Workbook("TC1028GP3.xlsx")

worksheet = workbook.add_worksheet("Hola")

worksheet.write("B1","Mensajes")

for i in range(5):
    
    mensaje=input("Dime el mensaje: ")
    
    posicion="B"+str(int(2+i))
    
    worksheet.write(posicion,mensaje)


workbook.close()