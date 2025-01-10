import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

doi = "10.5072/zenodo.150047" 
url = "https://sandbox.zenodo.org/api/records/150047"

r = requests.get(url) 
print(r.status_code)

data = json.loads(r.text) 
print("DOI:",data['doi'])

# enlace de descarga del archivo
fileurl = data['files'][0]['links']['self']

# descargar el archivo
file_r = requests.get(fileurl)
file_name = data['files'][0]['key']

# guardar el archivo descargado
with open(file_name, 'wb') as f:
    f.write(file_r.content)

# leer el archivo CSV y mostrar la tabla de datos
df = pd.read_csv(file_name)
print(df.head())

# distribución de la columna 'y'
df['y'].hist(bins=20, color='skyblue', edgecolor='black')
plt.title('Distribución de la columna y')
plt.xlabel('Valores de y')
plt.ylabel('Frecuencia')
plt.grid(False)
plt.show()