import requests

endpoint = "http://localhost:8000/api/"

response = requests.get(endpoint)
print(response.json())