import requests

url = 'https://petstore.swagger.io/v2/pet/findByStatus'
params = {"status": "sold"}
response = requests.get(url, params=params)
"""Trabajar con el JSON"""
response_json = response.json()           #Es un diccionario y lo puedo trabajar como tal. Lo parseo
print(response_json)

lista_mascotas_vendidas = []
for mascota in response_json:
    id_mascota = mascota["id"]
    nombre_mascota = mascota["name"]
    lista_mascotas_vendidas.append((id_mascota, nombre_mascota))

print(lista_mascotas_vendidas)