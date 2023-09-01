import requests


class Mascotas():
    def __init__(self, lista_mascotas):
        self.lista_de_mascotas = lista_mascotas

    def count_nombre_mascota(self):
        contador_nombres = {}
        for _, name in self.lista_de_mascotas:
            if name in contador_nombres:
                contador_nombres[name] += 1
            else:
                contador_nombres[name] = 1
        return contador_nombres


url = 'https://petstore.swagger.io/v2/pet/findByStatus'
params = {"status": "sold"}
response = requests.get(url, params=params)
response_json = response.json()
lista_mascotas_vendidas = []
for mascota in response_json:
    try:
        id_mascota = mascota["id"]
        nombre_mascota = mascota["name"]
        lista_mascotas_vendidas.append((id_mascota, nombre_mascota))
    except KeyError:
        pass

obj = Mascotas(lista_mascotas_vendidas)
contador_mascotas = obj.count_nombre_mascota()

for name, count in contador_mascotas.items():
    print(f'"{name}": {count}')

print('***' * 20)
print(contador_mascotas)
