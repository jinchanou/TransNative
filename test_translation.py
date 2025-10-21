import requests

url = 'http://localhost:8000/translate'
headers = {'Content-Type': 'application/json'}
data = {'text': '你好'}

response = requests.post(url, json=data, headers=headers)
print(response.status_code)
print(response.text)