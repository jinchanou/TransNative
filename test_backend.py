import requests

url = 'http://localhost:8000/translate'
headers = {'Content-Type': 'application/json'}
data = {'text': '你好'}

response = requests.post(url, json=data, headers=headers)
print(f'Status Code: {response.status_code}')
print(f'Response: {response.text}')