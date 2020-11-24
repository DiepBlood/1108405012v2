import requests
import json
url = "http://5b74423ea5837400141908c3.mockapi.io/Demo?cat=10&dog=5"

payload  = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)
data = json.loads(response.text)
print(data)
