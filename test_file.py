import requests
import json
import time
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
        URL = "https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/" + account_ID + "?api_key=" + information["api key"]
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
            if(match_history["matches"][i]["queue"]!=840):
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
            "1": "Annie",
           "2": "Olaf",
           "3": "Galio",
           "4": "TwistedFate",
           "5": "XinZhao",
           "6": "Urgot",
           "7": "LeBlanc",
           "8": "Vladimir",
           "9": "Fiddlesticks",
           "10": "Kayle",
           "11": "Master Yi",
           "12": "Alistar",
           "13": "Ryze",
           "14": "Sion",
           "15": "Sivir",
           "16": "Soraka",
           "17": "Teemo",
           "18": "Tristana",
           "19": "Warwick",
           "20": "Nunu",
           "21": "MissFortune",
           "22": "Ashe",
           "23": "Tryndamere",
           "24": "Jax",
           "25": "Morgana",
           "26": "Zilean",
           "27": "Singed",
           "28": "Evelynn",
           "29": "Twitch",
           "30": "Karthus",
           "31": "Cho'Gath",
           "32": "Amumu",
           "33": "Rammus",
           "34": "Anivia",
           "35": "Shaco",
           "36": "Dr.Mundo",
           "37": "Sona",
           "38": "Kassadin",
           "39": "Irelia",
           "40": "Janna",
           "41": "Gangplank",
           "42": "Corki",
           "43": "Karma",
           "44": "Taric",
           "45": "Veigar",
           "48": "Trundle",
           "50": "Swain",
           "51": "Caitlyn",
           "53": "Blitzcrank",
           "54": "Malphite",
           "55": "Katarina",
           "56": "Nocturne",
           "57": "Maokai",
           "58": "Renekton",
           "59": "JarvanIV",
           "60": "Elise",
           "61": "Orianna",
           "62": "Wukong",
           "63": "Brand",
           "64": "LeeSin",
           "67": "Vayne",
           "68": "Rumble",
           "69": "Cassiopeia",
           "72": "Skarner",
           "74": "Heimerdinger",
           "75": "Nasus",
           "76": "Nidalee",
           "77": "Udyr",
           "78": "Poppy",
           "79": "Gragas",
           "80": "Pantheon",
           "81": "Ezreal",
           "82": "Mordekaiser",
           "83": "Yorick",
           "84": "Akali",
           "85": "Kennen",
           "86": "Garen",
           "89": "Leona",
           "90": "Malzahar",
           "91": "Talon",
           "92": "Riven",
           "96": "Kog'Maw",
           "98": "Shen",
           "99": "Lux",
           "101": "Xerath",
           "102": "Shyvana",
           "103": "Ahri",
           "104": "Graves",
           "105": "Fizz",
           "106": "Volibear",
           "107": "Rengar",
           "110": "Varus",
           "111": "Nautilus",
           "112": "Viktor",
           "113": "Sejuani",
           "114": "Fiora",
           "115": "Ziggs",
           "117": "Lulu",
           "119": "Draven",
           "120": "Hecarim",
           "121": "Kha'Zix",
           "122": "Darius",
           "126": "Jayce",
           "127": "Lissandra",
           "131": "Diana",
           "133": "Quinn",
           "134": "Syndra",
           "136": "AurelionSol",
           "141": "Kayn",
           "142": "Zoe",
           "143": "Zyra",
           "145": "Kai'sa",
           "150": "Gnar",
           "154": "Zac",
           "157": "Yasuo",
           "161": "Vel'Koz",
           "163": "Taliyah",
           "164": "Camille",
           "201": "Braum",
           "202": "Jhin",
           "203": "Kindred",
           "222": "Jinx",
           "223": "TahmKench",
           "236": "Lucian",
           "238": "Zed",
           "240": "Kled",
           "245": "Ekko",
           "246": "Qiyana",
           "254": "Vi",
           "266": "Aatrox",
           "267": "Nami",
           "268": "Azir",
           "350": "Yuumi",
           "412": "Thresh",
           "420": "Illaoi",
           "421": "Rek'Sai",
           "427": "Ivern",
           "429": "Kalista",
           "432": "Bard",
           "497": "Rakan",
           "498": "Xayah",
           "516": "Ornn",
           "517": "Sylas",
           "518": "Neeko",
           "555": "Pyke"
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
    highest_kda.append(session.kda_from_name(summoner_info[j]["account id"], summoner_info[j]["name"]))
    highest_win_percent = highest_kda
    highest_masteries.append(session.highest_mastery_champ(summoner_info[j]["summoner id"], summoner_info[j]["name"]))

session.sort_mastery_score(highest_masteries)
session.sort_kda(highest_kda)
session.sort_summoner_level(summoner_info)

print("__**Top 5 Mastery Points**__")
for i in range(0, 5):
    print("" + str(i+1) + ". " + highest_masteries[i]["summoner name"] + " with " + str(highest_masteries[i]["champion points"]) + " mastery points on " + highest_masteries[i]["champion name"])

print("\n")
print("__**Top 5 KDAs**__")
for i in range(0, 5):
    print("" + str(i+1) + ". " + highest_kda[i]["summoner name"] + " with a kda of " + str(round(highest_kda[i]["kda"], 3)))

print("\n")
print("__**Top 5 Summoner Levels**__")
for i in range(0, 5):
    print(str(i+1) + ". " + summoner_info[i]["name"] + " with a summoner level of " + str(summoner_info[i]["summoner level"]))

print("\n")
session.sort_win_percent(highest_win_percent)
print("__**Top 5 Win Percentages**__")
for i in range(0, 5):
    print(str(i+1) + ". " + highest_win_percent[i]["summoner name"] + " with a win percent of " + str(highest_win_percent[i]["win%"]) + "%")

