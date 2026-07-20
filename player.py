import json


class Player:
    def __init__(
        self, player_id, name, role, bat_avg, strike_rate, wickets, bowl_avg, economy
    ):
        self.player_id = player_id
        self.name = name
        self.role = role
        self.batting_avg = bat_avg
        self.strike_rate = strike_rate
        self.wickets = wickets
        self.bowling_avg = bowl_avg
        self.economy = economy

    def to_dict(self):
        data = {
            "player_id": self.player_id,
            "name": self.name,
            "role": self.role,
            "bat_avg": self.batting_avg,
            "strike_rate": self.strike_rate,
            "wickets": self.wickets,
            "bowl_avg": self.bowling_avg,
            "economy": self.economy,
        }

        return data


def load_players():
    with open("data/player.json", "r") as file:
        players =json.load(file)
        
    return players

def save_players(players):
    with open("data/player.json","w") as file :
        json.dump(players,file)
        

def generate_playerID():
    player=load_players()