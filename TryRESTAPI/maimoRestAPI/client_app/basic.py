import requests

endpoint = "http://localhost:8000/api/"
response = requests.post(endpoint, params={"abc": 123}, json={'title': None, 'content': "The key to success"})   #params={"abc": 123}, 
#print(response.headers)
#print(response.text)
#print(response.status_code)
print(response.json())


