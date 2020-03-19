import requests
import json
import time
import custom_config

information = custom_config.information

class RiotAPI:
    def __init__(self):
        self.count = 0
        self.call_limit = 100
        self.time_to_sleep = 120
        
    def get_summoner_by_name(self, summoner_name):
        self.count = self.count + 1
        if(self.count==self.call_limit):
            time.sleep(self.time_to_sleep)
            self.count = 0
        URL = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner_name + "?api_key=" + information["api key"]
        ret_data = requests.get(URL)
        ret_data = json.loads(ret_data.text)
        return ret_data


session = RiotAPI()

for i in range(0, len(information["summoners"])):
    info = session.get_summoner_by_name(information["summoners"][i])
    print(info["accountId"])
