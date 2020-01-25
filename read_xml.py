import pandas as pd
import xlrd
import os

wb = xlrd.open_workbook('lista_de_precios.xls', logfile=open(os.devnull, 'w'))
sheet = pd.read_excel(wb, engine='xlrd', header=1)

clave = sheet['Clave']
grupo = sheet['Grupo']
codigo_fabricante = sheet['Codigo de Fabricante']

for i in sheet.index:

    if pd.isnull(clave[i]):
        break

    print(f"{clave[i]}, {grupo[i]}, {codigo_fabricante[i]}")

print('DONE!')