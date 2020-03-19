import requests
import json
import time

response = requests.get("http://ddragon.leagueoflegends.com/cdn/10.3.1/data/en_US/champion.json")
response = response.content
response = json.loads(response)
#response = json.dumps(response, indent=4)
data = response["data"]

for key in data:
    print('"' + data[key]["key"] + '": "' + key + '",')
    


