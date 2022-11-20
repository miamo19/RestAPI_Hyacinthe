import requests

product_id = input('What is the Product ID you want to use?: \n')
try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} is not a valid ID')

if product_id:
    endpoint = f"http://localhost:8000/api/{product_id}/"

response = requests.get(endpoint)
print(response.json())