import requests

#set endpoint to localhost server
endpoint = "http://127.0.0.1:8000/api/"

#get response with abc:123 as a param and hellow as a json query
response = requests.get(endpoint, json={"product_id": 123})
print(response.json())