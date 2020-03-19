import requests
import json
import time
import discord
import config

information = config.information

class RiotAPI:

    def __init__(self):
        self.count = 0
        self.call_limit = 100
        self.time_to_sleep = 120
        self.kdas = []

    ### GET FUNCTIONS ###

    ### CHAMPION-MASTERY-V4 ###

    def get_mastery_points(self, summoner_ID):
        self.count = self.count + 1
        if(self.count==self.call_limit):
            time.sleep(self.time_to_sleep)
            self.count = 0
        URL = "https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + summoner_ID + "?api_key=" + information["api key"]
        ret_data = requests.get(URL)
        ret_data = json.loads(ret_data.text)
        return ret_data

    def get_mastery_points_by_char_ID(self, summoner_ID, champion_ID):
        self.count = self.count + 1
        if(self.count==self.call_limit):
            time.sleep(self.time_to_sleep)
            self.count = 0
        URL = "https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + summoner_ID + "/by-champion/" + champion_ID + "?api_key=" + information["api key"]
        ret_data = requests.get(URL)
        ret_data = json.loads(ret_data.text)
        return ret_data

    def get_mastery_score(self, summoner_ID):
        self.count = self.count + 1
        if(self.count==self.call_limit):
            time.sleep(self.time_to_sleep)
            self.count = 0
        URL = "https://na1.api.riotgames.com/lol/champion-mastery/v4/scores/by-summoner/" + summoner_ID + "?api_key=" + information["api key"]
        ret_data = requests.get(URL)
        ret_data = json.loads(ret_data.text)
        return ret_data

    ### END CHAMPION-MASTERY-V4 ###

    ### LEAGUE V4 ###
    
    def get_account_details(self, summoner_ID):
        self.count = self.count + 1
        if(self.count==self.call_limit):
            time.sleep(self.time_to_sleep)
            self.count = 0
        URL = "https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + summoner_ID + "?api_key=" + information["api key"]
        ret_data = requests.get(URL)
        ret_data = json.loads(ret_data.text)
        return ret_data

    ### END LEAGUE V4 ###

    ### MATCH V4 ###

    def get_match_details(self, match_ID):
        self.count = self.count + 1
        if(self.count==self.call_limit):
            time.sleep(self.time_to_sleep)
            self.count = 0
        URL = "https://na1.api.riotgames.com/lol/match/v4/matches/" + str(match_ID) + "?api_key=" + information["api key"]
        ret_data = requests.get(URL)
        ret_data = json.loads(ret_data.text)
        return ret_data

    def get_match_history(self, account_ID):
        self.count = self.count + 1
        if(self.count==self.call_limit):
            time.sleep(self.time_to_sleep)
            self.count = 0
        URL = "https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/" + str(account_ID) + "?queue=420&queue=430&queue=440&queue=400&api_key=" + information["api key"]
        ret_data = requests.get(URL)
        ret_data = json.loads(ret_data.text)
        return ret_data

    def get_match_timeline(self, match_ID):
        self.count = self.count + 1
        if(self.count==self.call_limit):
            time.sleep(self.time_to_sleep)
            self.count = 0
        URL = "https://na1.api.riotgames.com/lol/match/v4/timelines/by-match/" + match_ID + "?api_key=" + information["api key"]
        ret_data = requests.get(URL)
        ret_data = json.loads(ret_data.text)
        return ret_data

    def get_match_ID_by_tournament_code(self, tournament_code):
        self.count = self.count + 1
        if(self.count==self.call_limit):
            time.sleep(self.time_to_sleep)
            self.count = 0
        URL = "https://na1.api.riotgames.com/lol/match/v4/matches/by-tournament-code/" + tournament_code + "/ids?api_key=" + information["api key"]
        ret_data = requests.get(URL)
        ret_data = json.loads(ret_data.text)
        return ret_data

    def get_match_by_match_ID_and_tournament_code(self, match_ID, tournament_Code):
        self.count = self.count + 1
        if(self.count==self.call_limit):
            time.sleep(self.time_to_sleep)
            self.count = 0
        URL = "https://na1.api.riotgames.com/lol/match/v4/matches/" + match_ID + "/by-tournament-code/" + tournament_code + "?api_key=" + information["api key"]
        ret_data = requests.get(URL)
        ret_data = json.loads(ret_data.text)
        return ret_data

    ### END MATCH V4 ###

    ### SUMMONER V4 ###

    def get_summoner_by_account_ID(self, account_ID):
        self.count = self.count + 1
        if(self.count==self.call_limit):
            time.sleep(self.time_to_sleep)
            self.count = 0
        URL = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-account/" + account_ID + "?api_key=" + information["api key"]
        ret_data = requests.get(URL)
        ret_data = json.loads(ret_data.text)
        return ret_data
    
    def get_summoner_by_name(self, summoner_name):
        self.count = self.count + 1
        if(self.count==self.call_limit):
            time.sleep(self.time_to_sleep)
            self.count = 0
        URL = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner_name + "?api_key=" + information["api key"]
        ret_data = requests.get(URL)
        ret_data = json.loads(ret_data.text)
        return ret_data

    def get_summoner_by_summoner_ID(self, summoner_ID):
        self.count = self.count + 1
        if(self.count==self.call_limit):
            time.sleep(self.time_to_sleep)
            self.count = 0
        URL = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/" + summoner_ID + "?api_key=" + information["api key"]
        ret_data = requests.get(URL)
        ret_data = json.loads(ret_data.text)
        return ret_data

    ### END SUMMONER V4 ###

    ### END OF GET FUNCTIONS ###

    ### CUSTOM GET FUNTIONS ###

    def get_summoner_info(self, account_id):
        info = session.get_summoner_by_account_ID(account_id)
        print(json.dumps(info, indent=4))
        account_details = {
            "name" : info["name"],
            "account id" : info["accountId"],
            "summoner id" : info["id"],
            "summoner level" : info["summonerLevel"]
        }
        return account_details

    def player_ranked_details(self, summoner_ID, summoner_name):
        ranked_info = session.get_account_details(summoner_ID)
        ranked_data = {}
        
        for i in range(0, len(ranked_info)):
            if(ranked_info[i]["queueType"]=="RANKED_SOLO_5x5"):
                ranked_data = {
                    "name": summoner_name,
                    "tier": ranked_info[i]["tier"],
                    "rank": ranked_info[i]["rank"],
                    "lp": ranked_info[i]["leaguePoints"]
                }
        return ranked_data

    def kda_from_name(self, account_id, summoner_name):
        match_history = session.get_match_history(account_id)

        kills = 0
        deaths = 0
        assists = 0
        games_played = 0
        wins = 0

        #len(match_history["matches"])
        
        for i in range(0, len(match_history["matches"])):
            if(match_history["matches"][i]["queue"]==420 or match_history["matches"][i]["queue"]==430 or match_history["matches"][i]["queue"]==440 or match_history["matches"][i]["queue"]==400):
                test_match = session.get_match_details(match_history["matches"][i]["gameId"])
                participant_num = 1
                
                for k in range(0, len(test_match["participantIdentities"])):
                    if(test_match["participantIdentities"][k]["player"]["summonerName"]==summoner_name):
                        participant_num = test_match["participantIdentities"][k]["participantId"]
                kills = kills + test_match["participants"][participant_num-1]["stats"]["kills"]
                deaths = deaths + test_match["participants"][participant_num-1]["stats"]["deaths"]
                assists = assists + test_match["participants"][participant_num-1]["stats"]["assists"]
                games_played = games_played + 1
                if(test_match["participants"][participant_num-1]["stats"]["win"]==True):
                    wins = wins + 1

        kills_and_assists = kills + assists
        kda = kills_and_assists/deaths
        win_percent = round((wins/games_played)*100)
        data = {
            "kda": kda,
            "summoner name": summoner_name,
            "games played": games_played,
            "wins": wins,
            "win%":win_percent,
            "match history":match_history
        }
        return data

    def highest_mastery_champ(self, summoner_ID, summoner_name):
        mastery_info = self.get_mastery_points(summoner_ID)
        data = {
            "summoner name": summoner_name,
            "champion name":"",
            "champion points":0            
        }
        data["champion name"] = self.get_champions_name(str(mastery_info[0]["championId"]))
        data["champion points"] = mastery_info[0]["championPoints"]
        return data

    ### END CUSTOM GET FUNCTIONS ###

    ### SORTING ALGORITHMS ###

    def sort_mastery_score(self, mastery_scores):
        n = len(mastery_scores) 
  
        # Traverse through all array elements 
        for i in range(n): 
      
            # Last i elements are already in place 
            for j in range(0, n-i-1): 
      
                # traverse the array from 0 to n-i-1 
                # Swap if the element found is greater 
                # than the next element 
                if mastery_scores[j]["champion points"] < mastery_scores[j+1]["champion points"] : 
                    mastery_scores[j], mastery_scores[j+1] = mastery_scores[j+1], mastery_scores[j]

        return mastery_scores

    def sort_kda(self, kdas):
        n = len(kdas) 
  
        # Traverse through all array elements 
        for i in range(n): 
      
            # Last i elements are already in place 
            for j in range(0, n-i-1): 
      
                # traverse the array from 0 to n-i-1 
                # Swap if the element found is greater 
                # than the next element 
                if kdas[j]["kda"] < kdas[j+1]["kda"] : 
                    kdas[j], kdas[j+1] = kdas[j+1], kdas[j]

        return kdas

    def sort_summoner_level(self, summoner_info):
        n = len(summoner_info) 
  
        # Traverse through all array elements 
        for i in range(n): 
      
            # Last i elements are already in place 
            for j in range(0, n-i-1): 
      
                # traverse the array from 0 to n-i-1 
                # Swap if the element found is greater 
                # than the next element 
                if summoner_info[j]["summoner level"] < summoner_info[j+1]["summoner level"] : 
                    summoner_info[j], summoner_info[j+1] = summoner_info[j+1], summoner_info[j]

        return summoner_info

    def sort_win_percent(self, win_percent):
        n = len(win_percent) 
  
        # Traverse through all array elements 
        for i in range(n): 
      
            # Last i elements are already in place 
            for j in range(0, n-i-1): 
      
                # traverse the array from 0 to n-i-1 
                # Swap if the element found is greater 
                # than the next element 
                if win_percent[j]["win%"] < win_percent[j+1]["win%"] : 
                    win_percent[j], win_percent[j+1] = win_percent[j+1], win_percent[j]

        return win_percent

    ### END SORTING ALGORITHMS ###
        

    def get_champions_name(self, _id):
        """
        this functions takes an _id and returns the associate champions name
        :param _id: any integer from 1 to 555. if there is a champion, it will return the name.
        :return: champions name
        """
        all_champion_id = {
            "266": "Aatrox",
            "103": "Ahri",
            "84": "Akali",
            "12": "Alistar",
            "32": "Amumu",
            "34": "Anivia",
            "1": "Annie",
            "523": "Aphelios",
            "22": "Ashe",
            "136": "AurelionSol",
            "268": "Azir",
            "432": "Bard",
            "53": "Blitzcrank",
            "63": "Brand",
            "201": "Braum",
            "51": "Caitlyn",
            "164": "Camille",
            "69": "Cassiopeia",
            "31": "Chogath",
            "42": "Corki",
            "122": "Darius",
            "131": "Diana",
            "119": "Draven",
            "36": "DrMundo",
            "245": "Ekko",
            "60": "Elise",
            "28": "Evelynn",
            "81": "Ezreal",
            "9": "Fiddlesticks",
            "114": "Fiora",
            "105": "Fizz",
            "3": "Galio",
            "41": "Gangplank",
            "86": "Garen",
            "150": "Gnar",
            "79": "Gragas",
            "104": "Graves",
            "120": "Hecarim",
            "74": "Heimerdinger",
            "420": "Illaoi",
            "39": "Irelia",
            "427": "Ivern",
            "40": "Janna",
            "59": "JarvanIV",
            "24": "Jax",
            "126": "Jayce",
            "202": "Jhin",
            "222": "Jinx",
            "145": "Kaisa",
            "429": "Kalista",
            "43": "Karma",
            "30": "Karthus",
            "38": "Kassadin",
            "55": "Katarina",
            "10": "Kayle",
            "141": "Kayn",
            "85": "Kennen",
            "121": "Khazix",
            "203": "Kindred",
            "240": "Kled",
            "96": "KogMaw",
            "7": "Leblanc",
            "64": "LeeSin",
            "89": "Leona",
            "127": "Lissandra",
            "236": "Lucian",
            "117": "Lulu",
            "99": "Lux",
            "54": "Malphite",
            "90": "Malzahar",
            "57": "Maokai",
            "11": "MasterYi",
            "21": "MissFortune",
            "62": "MonkeyKing",
            "82": "Mordekaiser",
            "25": "Morgana",
            "267": "Nami",
            "75": "Nasus",
            "111": "Nautilus",
            "518": "Neeko",
            "76": "Nidalee",
            "56": "Nocturne",
            "20": "Nunu",
            "2": "Olaf",
            "61": "Orianna",
            "516": "Ornn",
            "80": "Pantheon",
            "78": "Poppy",
            "555": "Pyke",
            "246": "Qiyana",
            "133": "Quinn",
            "497": "Rakan",
            "33": "Rammus",
            "421": "RekSai",
            "58": "Renekton",
            "107": "Rengar",
            "92": "Riven",
            "68": "Rumble",
            "13": "Ryze",
            "113": "Sejuani",
            "235": "Senna",
            "875": "Sett",
            "35": "Shaco",
            "98": "Shen",
            "102": "Shyvana",
            "27": "Singed",
            "14": "Sion",
            "15": "Sivir",
            "72": "Skarner",
            "37": "Sona",
            "16": "Soraka",
            "50": "Swain",
            "517": "Sylas",
            "134": "Syndra",
            "223": "TahmKench",
            "163": "Taliyah",
            "91": "Talon",
            "44": "Taric",
            "17": "Teemo",
            "412": "Thresh",
            "18": "Tristana",
            "48": "Trundle",
            "23": "Tryndamere",
            "4": "TwistedFate",
            "29": "Twitch",
            "77": "Udyr",
            "6": "Urgot",
            "110": "Varus",
            "67": "Vayne",
            "45": "Veigar",
            "161": "Velkoz",
            "254": "Vi",
            "112": "Viktor",
            "8": "Vladimir",
            "106": "Volibear",
            "19": "Warwick",
            "498": "Xayah",
            "101": "Xerath",
            "5": "XinZhao",
            "157": "Yasuo",
            "83": "Yorick",
            "350": "Yuumi",
            "154": "Zac",
            "238": "Zed",
            "115": "Ziggs",
            "26": "Zilean",
            "142": "Zoe",
            "143": "Zyra"
        }
        return all_champion_id[_id]        

session = RiotAPI()

summoner_info = []
ranked_data = []
highest_kda = []
highest_masteries = []
highest_win_percent = []
for j in range(0, len(information["summoners"])):
    summoner_info.append(session.get_summoner_info(information["accountIds"][j]))
    ranked_data.append(session.player_ranked_details(summoner_info[j]["summoner id"], summoner_info[j]["name"]))
    
    try:
        highest_kda.append(session.kda_from_name(summoner_info[j]["account id"], summoner_info[j]["name"]))
        highest_win_percent = highest_kda
    except:
        print(summoner_info[j]["name"] + " account did not work and has been discluded from the kda and win% leaderboard.")
        
    highest_masteries.append(session.highest_mastery_champ(summoner_info[j]["summoner id"], summoner_info[j]["name"]))

session.sort_mastery_score(highest_masteries)
session.sort_kda(highest_kda)
session.sort_summoner_level(summoner_info)

from discord import Webhook, RequestsWebhookAdapter

WEBHOOK_ID = 635878642160893952
WEBHOOK_TOKEN = "n9OdCx1WqvUQfddB-lbJBjVxwP7Cnt30N4fPqeSMDlbTU7uUPYutZeW98z2Jk0q642x5"

webhook = Webhook.partial(WEBHOOK_ID, WEBHOOK_TOKEN, \
adapter = RequestsWebhookAdapter())

stringMastery = "__**Top 5 Mastery Points**__\n"
stringKDA = "__**Top 5 KDAs**__\n"
stringLevels = "__**Top 5 Summoner Levels**__\n"
stringWins = "__**Top 5 Win Percentages**__\n"
stringJoin = "**If you would like to be added to the leaderboard click the link below** \nhttps://forms.gle/oKWoX9PirYDFD6fA7"

    
for i in range(0, 5):
    stringMastery = stringMastery + ("" + str(i+1) + ". " + highest_masteries[i]["summoner name"] + " with " + str(highest_masteries[i]["champion points"]) + " mastery points on " + highest_masteries[i]["champion name"] + "\n")

stringMastery = stringMastery + "\u200B" + "\u200B" + "\u200B"
webhook.send(stringMastery)


for i in range(0, 5):
    stringKDA = stringKDA + ("" + str(i+1) + ". " + highest_kda[i]["summoner name"] + " with a kda of " + str(round(highest_kda[i]["kda"], 3)) + "\n")

stringKDA = stringKDA + "\u200B" + "\u200B" + "\u200B"
webhook.send(stringKDA)


for i in range(0, 5):
    stringLevels = stringLevels + (str(i+1) + ". " + summoner_info[i]["name"] + " with a summoner level of " + str(summoner_info[i]["summoner level"]) + "\n")

stringLevels = stringLevels + "\u200B" + "\u200B" + "\u200B"
webhook.send(stringLevels)


session.sort_win_percent(highest_win_percent)
for i in range(0, 5):
    stringWins = stringWins + (str(i+1) + ". " + highest_win_percent[i]["summoner name"] + " with a win percent of " + str(highest_win_percent[i]["win%"]) + "%" + "\n")

stringWins = stringWins + "\u200B" + "\u200B" + "\u200B"
webhook.send(stringWins)

stringChip = "__**Lowest Ranked Winrate**__\n"
stringChip = stringChip + ("Chipper with a win percent of 21%" + "\n")

webhook.send(stringChip)
webhook.send(stringJoin)

#print(stringMastery)
#print(stringKDA)
#print(stringLevels)
#print(stringWins)
#print(stringChip)
