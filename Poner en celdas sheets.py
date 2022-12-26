import pandas as pd
import gspread
from df2gspread import df2gspread as d2g
import gspread_dataframe as gd
from oauth2client.service_account import ServiceAccountCredentials

scope=['https://www.googleapis.com/auth/spreadsheets',
       'https://www.googleapis.com/auth/drive.file',
       'https://www.googleapis.com/auth/drive']

creds=ServiceAccountCredentials.from_json_keyfile_name("Interprete.json",scope)

client=gspread.authorize(creds)


miLista=client.open("Subir de Excel").worksheet("Hoja 1")


miLista.update_cell(2,2,"Buenas")
miLista.update_cell(2,3,"tardes")
miLista.update_cell(2,4,"Desayunemo")
miLista.update_cell(2,5,"en la")
miLista.update_cell(2,6,"noche")

