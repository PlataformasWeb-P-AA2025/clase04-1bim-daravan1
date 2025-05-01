import requests
import csv

lista_datos = []
# Leer el archivo CSV y cargar los datos en una lista de diccionarios
with open('atp_tennis.csv', newline='', encoding='latin1') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        lista_datos.append(row)

base_datos = "personas005"
# Configurar el acceso a la base de datos
url = f"http://127.0.0.1:5984/{base_datos}"
headers = {'Content-Type': 'application/json'}

# Enviar datos

for doc in lista_datos:
    response = requests.post(
        url,
        headers=headers,
        json=doc
    )
    # Comprobar la respuesta del servidor
    print(f"{doc['Date']} | {doc['Player_1']} vs {doc['Player_2']} | {response.status_code}")

