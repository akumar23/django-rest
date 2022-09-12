import requests

#set endpoint to localhost server
endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    "title":"newest data here"
}

#get response with abc:123 as a param and hellow as a json query
response = requests.post(endpoint, json=data)
print(response.json())