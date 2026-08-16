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
        players = json.load(file)

    return players


def save_players(players):
    with open("data/player.json", "w") as file:
        json.dump(players, file, indent=4)


def generate_playerID():
    players = load_players()
    if not players:
        return "P001"
    last_id = players[-1]["player_id"]
    number = int(last_id[1:])

    return f"P{number + 1:03d}"


def add_player():

    player_id = generate_playerID()
    players = load_players()
    name = input("Enter player name:")
    role = input("Enter role of player:")
    bat_avg = float(input("Enter the batting average:"))
    strike_rate = float(input("Enter the strike rate of player:"))
    wickets = int(input("Enter the wickets of player:"))
    bowl_avg = float(input("Enter the the bowling average:"))
    economy = float(input("Enter the economy of player:"))

    player_details = Player(
        player_id, name, role, bat_avg, strike_rate, wickets, bowl_avg, economy
    )

    new_player = player_details.to_dict()
    players.append(new_player)

    save_players(players)


def view_players():
    players = load_players()
    print(
        f"{'ID':10}|{'Name':15}|{'Role':15}|{'Bat_Avg':10}|{'SR':10}|{'wickets':10}|{'bowl_avg':10}|{'economy':10}|"
    )
    print("-" * 110)
    for player in players:
        print(
            f"{player['player_id']:10}|{player['name']:15}|{player['role']:15}|{player['bat_avg']:10}|{player['strike_rate']:10}|{player['wickets']:10}|{player['bowl_avg']:10}|{player['economy']:10}|"
        )


def search_player():
    Playerid = input("Enter player id to searh Player: ")
    players = load_players()
    found = False
    for player in players:
        if player["player_id"] == Playerid:
            print("Player Found")
            print("-" * 105)
            print(
                f"{'ID':10}|{'Name':15}|{'Role':15}|{'Bat_Avg':10}|{'SR':10}|{'wickets':10}|{'bowl_avg':10}|{'economy':10}|"
            )
            print("-" * 105)
            print(
                f"{player['player_id']:10}|{player['name']:15}|{player['role']:15}|{player['bat_avg']:10}|{player['strike_rate']:10}|{player['wickets']:10}|{player['bowl_avg']:10}|{player['economy']:10}|"
            )
            print("-" * 105)
            found = True
    if not found:
        print("player doesnot exist!")


def update_player():
    PlayerId = input("Enter player Id to update:")
    players = load_players()
    found = False

    for player in players:
        if player["player_id"] == PlayerId:
            print("-" * 105)
            print(
                f"{'ID':10}|{'Name':15}|{'Role':15}|{'Bat_Avg':10}|{'SR':10}|{'wickets':10}|{'bowl_avg':10}|{'economy':10}|"
            )
            print("-" * 105)
            print(
                f"{player['player_id']:10}|{player['name']:15}|{player['role']:15}|{player['bat_avg']:10}|{player['strike_rate']:10}|{player['wickets']:10}|{player['bowl_avg']:10}|{player['economy']:10}|"
            )
            print("-" * 105)
            matching_player = player
            found = True

    if not found:
        print("Player does not exist")
    else:
        print("What do you wnat to update?")
        print("1.Name")
        print("2.Role")
        print("3.Batting average")
        print("4.Strike rate")
        print("5.Wickets")
        print("6.Bowling Average")
        print("7.Economy")

        choice = int(input("Enter the choice:"))

        field_map = {
            1: "name",
            2: "role",
            3: "bat_avg",
            4: "strike_rate",
            5: "wickets",
            6: "bowl_avg",
            7: "economy",
        }
        selected_field = field_map[choice]
        type_map = {
            "name": str,
            "role": str,
            "bat_avg": float,
            "strike_rate": float,
            "wickets": int,
            "bowl_avg": float,
            "economy": float,
        }

        converter = type_map[selected_field]
        new_value = converter(input("Enter New Value:"))

        Confirm_update = input("confirm update?(Yes/No):")
        if Confirm_update.lower() == "yes":
            matching_player[selected_field] = new_value
            save_players(players)
            print("Player updated successfully")
        else:
            print("Update cancelled")

def delete_player():
    Playerid=input("Enter player id to delete player:")
    Players=load_players()
    found=False

    for player in Players:
        if player["player_id"]==Playerid:
            print("-" * 105)
            print(
                f"{'ID':10}|{'Name':15}|{'Role':15}|{'Bat_Avg':10}|{'SR':10}|{'wickets':10}|{'bowl_avg':10}|{'economy':10}|"
            )
            print("-" * 105)
            print(
                f"{player['player_id']:10}|{player['name']:15}|{player['role']:15}|{player['bat_avg']:10}|{player['strike_rate']:10}|{player['wickets']:10}|{player['bowl_avg']:10}|{player['economy']:10}|"
            )
            print("-" * 105)
            found =True

            confirm_deletion = input("Are you sure  you wnat to delete player(Yes/No):")

            if confirm_deletion.lower() == "yes":
                Players.remove(player)
                save_players(Players)
                print("Player deleted successfully!")
            else:
                print("deletion cancelled")
    if not found:
        print("player id does not exist!")

