import pandas as pd
import gspread
import numpy as np
from df2gspread import df2gspread as d2g
import gspread_dataframe as gd
from oauth2client.service_account import ServiceAccountCredentials

#Sección para googlesheets
scope=['https://www.googleapis.com/auth/spreadsheets',
       'https://www.googleapis.com/auth/drive.file',
       'https://www.googleapis.com/auth/drive']

creds=ServiceAccountCredentials.from_json_keyfile_name("Keys.json",scope)

client=gspread.authorize(creds)

miLista=client.open("Datos").worksheet("RetoFinal")

#inicia tu código

renglon=30
columna=2

miLista.update_cell(renglon,columna,"Qué pex Tributos?")

   