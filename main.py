import requests
param = {'results': '5', 'gender': 'male', 'nat':'us,dk' }
url = f'https://randomuser.me/api/'
response = requests.get(url, param)
data = response.json()
print(response.url)
# print(data)