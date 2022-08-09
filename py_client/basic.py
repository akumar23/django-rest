import requests

endpoint = "https://httpbin.org/status/200"
endpoint = "https://httpbin.org/anything"

response = requests.get(endpoint)
print(response.text)