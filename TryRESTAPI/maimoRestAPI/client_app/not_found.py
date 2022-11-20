import requests

endpoint = "http://localhost:8000/api/32245458754787/"

response = requests.get(endpoint)
print(response.json())