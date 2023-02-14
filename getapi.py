# from urllib.request import urlopen
#
# import json
# url = 'https://api.exchangeratesapi.io'
# with open(urlopen(url)) as f :
#     data = f.read()
#
# print(data)


import json
import requests

url = "https://api.apilayer.com/number_verification/countries"

payload = {}
headers= {
  "apikey": "wsYMfvQlmZiYRoPpHvRtpoJgRCeg1b6V"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
print(response.json)
print(result)
print(type(result))
print(type(response))

py = json.loads(result)
print(type(py))
print(py)

