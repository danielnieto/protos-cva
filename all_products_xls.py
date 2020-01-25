import xlrd
import pandas as pd
import zipfile
import requests
import os
import glob
import shutil

def descarga_zip():
    print('descargando zip')
    url = 'https://me.grupocva.com/me/descarga_listas/descarga_lista_excel.php?orden=1&fLista=33&fCliente=35701&fAlmacen=189'
    r = requests.get(url)
    os.makedirs('./tmp', exist_ok=True)
    with open('./tmp/lista.zip', 'wb') as f:
        f.write(r.content)

descarga_zip()

with zipfile.ZipFile('./tmp/lista.zip', 'r') as zip_ref:
    zip_ref.extractall('./tmp')

xls_file = glob.glob("./tmp/*.xls")[0]

wb = xlrd.open_workbook(xls_file, logfile=open(os.devnull, 'w'))
sheet = pd.read_excel(wb, engine='xlrd', header=1)

clave = sheet['Clave']
grupo = sheet['Grupo']
codigo_fabricante = sheet['Codigo de Fabricante']

total = 0

for i in sheet.index:

    if pd.isnull(clave[i]):
        break

    total = total + 1
    print(f"{clave[i]}, {grupo[i]}, {codigo_fabricante[i]}")

shutil.rmtree('./tmp')
print(f'el total de productos es {total}')
print('DONE!')
