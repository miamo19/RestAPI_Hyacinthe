import requests
product_id = input("What is the Product ID you need to modify? ")
try:
    product_id = int(product_id)
except:
    product_id = None 
    print(f"{product_id} is not found!! ")

endpoint = f"http://localhost:8000/api/{product_id}/update/"
data ={
    'title': input("Enter your title: "),        #The Wedding of the year
    'content': input("Enter your content: "),        #Wedding of the Prince of Bandja
    'price': int(input("Enter your price: "))
}
response = requests.put(endpoint, json=data)
print(response.json())