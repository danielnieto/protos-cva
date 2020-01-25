import requests
from xml.etree import ElementTree

def fetch_and_parse(url):
    response = requests.get(url).text
    return ElementTree.fromstring(response)

print('Descargando todos los grupos')
grupos = fetch_and_parse('http://www.grupocva.com/catalogo_clientes_xml/grupos.xml')

diccionario_grupos = {}

for grupo in grupos:
    nombre_grupo = grupo.text

    if (nombre_grupo == 'PCS'):
        nombre_grupo = 'PC´S'
    print(f'Descargando Grupo: {nombre_grupo}')
    url_grupo = f'https://www.grupocva.com/catalogo_clientes_xml/lista_precios.xml?cliente=18016&marca=%&grupo={nombre_grupo}%&clave=%&codigo=%'
    articulos = fetch_and_parse(url_grupo)
    print(f'{nombre_grupo} tiene {len(articulos.findall("item"))} articulos')
    diccionario_grupos[nombre_grupo] = []
    for articulo in articulos.findall('item'):
        diccionario_grupos[nombre_grupo].append(articulo.find('clave').text)

print('TODOS LOS GRUPOS SE HAN DESCARGADO')

for grupo in diccionario_grupos:
    print(f'{grupo}: {len(diccionario_grupos[grupo])}')