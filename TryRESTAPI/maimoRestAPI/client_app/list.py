import requests

endpoint = "http://localhost:8000/api/list/"

response = requests.get(endpoint)
print(response.json())