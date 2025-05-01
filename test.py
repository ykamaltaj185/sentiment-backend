import requests

response = requests.post("http://127.0.0.1:5000/analyze", json={"text": "This is so cool!"})
print(response.json())
