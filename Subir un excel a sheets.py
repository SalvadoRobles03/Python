import pandas as pd
import gspread
from df2gspread import df2gspread as d2g
import gspread_dataframe as gd
import datetime
from oauth2client.service_account import ServiceAccountCredentials

scope=['https://www.googleapis.com/auth/spreadsheets',
       'https://www.googleapis.com/auth/drive.file',
       'https://www.googleapis.com/auth/drive']

creds=ServiceAccountCredentials.from_json_keyfile_name("Interprete.json",scope)

client=gspread.authorize(creds)


hoy=datetime.datetime.now()
fecha=hoy.strftime("%d%b")
resultados=pd.read_excel('Resultados1.xlsx',fecha)

spreadSheetKey = '1vJmie-Vvgk-SMsLc2lAoRp2VcQJgnU4Bp3wma5T7Jzo'
writeSheet = 'TABLA'

d2g.upload(resultados, spreadSheetKey, writeSheet, credentials=creds, row_names=False)



"""
Con esto modificas una celda específica

resultados=client.open("Datos").sheet1
#resultados=client.open("Datos").worksheet("Test")

resultados.update_cell(3,2,"Que pex3")

"""
   