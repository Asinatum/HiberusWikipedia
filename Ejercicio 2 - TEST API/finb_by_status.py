import requests

url = 'https://petstore.swagger.io/v2/pet/findByStatus'
params = {"status": "sold"}
response = requests.get(url, params=params)
response_json = response.json()
print(response_json)


lista_mascotas_vendidas = []
for mascota in response_json:
    try:
        id_mascota = mascota["id"]
        nombre_mascota = mascota["name"]
        lista_mascotas_vendidas.append((id_mascota, nombre_mascota))
    except KeyError:
        pass


print('** ** ** *'*20)
print(lista_mascotas_vendidas)


