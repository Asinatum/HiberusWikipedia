import requests

url = 'https://petstore.swagger.io/v2/user'
payload = {
  "id": 25251717,
  "username": "LucasSosa",
  "firstName": "Lucas",
  "lastName": "Sosa",
  "email": "lucassosa83@gmail.com",
  "password": "123456123456",
  "phone": "44556677",
  "userStatus": 1
}  #Los datos que quiero enviar. Me los colola dentro del atributo DATA y del atributo JSON.

response = requests.post(url, json=payload)  #Si enviamos los parametros dentro de json, internamente POST se encarga de serializarlos (los convierte a un json).


print(response.status_code)
print(response.content)

url = 'https://petstore.swagger.io/v2/user/LucasSosa'

response = requests.get(url)
content = response.content
print(response.status_code)
print(content)


