import xlsxwriter

workbook = xlsxwriter.Workbook("TC1028GP3.xlsx")

worksheet = workbook.add_worksheet()

worksheet.write("B2","Las")
worksheet.write("B3","vacas")
worksheet.write("B4","ganaron")
worksheet.write("B5","pero")
worksheet.write("B6","en diciembre hay barbacoa")

workbook.close()