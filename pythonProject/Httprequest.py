import requests
payload={'username':'Samran','Pass':'testing'}

response = requests.post('http://httpbin.org/post', data=payload)
print(response.json())