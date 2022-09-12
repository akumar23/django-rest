import requests

#program to test update function in API

prod_id = input("What id do you want to update? ")

try:
    prod_id = int (prod_id)
except:
    print("ID should be an integer")

title = input("What do you want to change the title to? ")

endpoint = f"http://localhost:8000/api/products/{prod_id}/update/"

data = {
    "title": title,
    "price": 199.91
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())