import requests

#testing how API handles if id doesn't exist 
endpoint = "http://localhost:8000/api/products/1999055"

get_response = requests.get(endpoint)
print(get_response.json())