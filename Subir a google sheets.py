import pandas as pd
import gspread
from df2gspread import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials

scope=["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]


creds=ServiceAccountCredentials.from_json_keyfile_name("Interprete.json",scope)
client=gspread.authorize(creds)

readSheet=client.open("Datos").worksheet("Hoja 2").get_all_records()

resultados=pd.DataFrame.from_dict(readSheet)

spreadSheetKey="1aFetOa0sMiLAWtnA2Y9zCDkuYK66bGYrMbCNELJTooQ"
writeSheet="sheet1"

d2g.upload(resultados,spreadSheetKey,writeSheet,credentials=creds,row_names=False)