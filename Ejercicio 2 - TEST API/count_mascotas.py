import requests


class Mascotas:
    def _init_(self, lista_de_mascotas):
        self.lista_de_mascotas = lista_de_mascotas

    def count_mascot_names(self):
        """Esta función calcula cuántas veces aparece cada nombre de mascota en lista_de_mascotas y
        devuelve un diccionario donde las keys son los nombres de mascota y los valores son los recuentos
         de esos nombres."""

        contador_nombres = {}                            #Creo un diccionario vacio
        for _, name in self.lista_de_mascotas:          #El id es lo uso solo como placeholder, no lo uso en la funcion
            if name in contador_nombres:                 #Checkea si el name ya es (o aun no) una key del diccionario
                contador_nombres[name] += 1              #Si el nombre ya existe en el diccionario suma 1 a la cantidad
            else:
                contador_nombres[name] = 1               #Si aparece por primera vez en el diccionario, le asigna el valor 1

        return contador_nombres


url = 'https://petstore.swagger.io/v2/pet/findByStatus'
params = {"status": "sold"}
response = requests.get(url, params=params)
"""Trabajar con el JSON"""
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
contador_mascotas = obj.count_mascot_names()

for name, count in contador_mascotas.items():
    print(f'"{name}": {count}')

print('***'*20)

print(contador_mascotas)