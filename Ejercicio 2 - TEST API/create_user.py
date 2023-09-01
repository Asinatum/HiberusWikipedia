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
}

response = requests.post(url, json=payload)


print(response.status_code)
print(response.content)

url = 'https://petstore.swagger.io/v2/user/LucasSosa'

response = requests.get(url)
content = response.content


print(response.status_code)
print(content)


