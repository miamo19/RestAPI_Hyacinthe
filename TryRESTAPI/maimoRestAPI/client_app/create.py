import requests

endpoint = "http://localhost:8000/api/list/"
data = {
    'title': input("Enter your title: "),
    'content': input("Enter Your Content: "),
    'Price': input('Enter your price: ')
    }

response = requests.post(endpoint, json=data)
print(response.json())