import requests

#program to test delete function in API

prod_id = input("What id do you want to delete? ")

try:
    prod_id = int (prod_id)
except:
    print("ID should be an integer")

endpoint = f"http://localhost:8000/api/products/{prod_id}/update/"

get_response = requests.delete(endpoint)
print(get_response.status_code)