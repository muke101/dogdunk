import requests
import json
server = 'http://36f5229b.ngrok.io/'
payload = json.JSONEncoder().encode({'userName':'muke','level':3,'experiance':15})
r = requests.put(server+'muke', data=payload)
print(r.status_code)
payload = json.JSONEncoder().encode({'userName':'bikeboi','level':2,'experiance':20})
r = requests.put(server+'bikeboi', data=payload)
print(r.status_code)