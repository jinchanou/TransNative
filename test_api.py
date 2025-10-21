import requests

def test_translation():
    url = "http://localhost:8000/translate"
    headers = {"Content-Type": "application/json"}
    data = {"text": "你好"}
    
    try:
        response = requests.post(url, json=data, headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_translation()