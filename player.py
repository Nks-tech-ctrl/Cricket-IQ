import json


class Player:
    def __init__(self, player_id, name, role, stats):
        self.player_id = player_id
        self.name = name
        self.role = role
        self.stats = stats

    def to_dict(self):
        return {
            "player_id": self.player_id,
            "name": self.name,
            "role": self.role,
            "stats": self.stats,
        }


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
    format = input("Enter Format (T20/ODI/Test):")
    matches = int(input("Enter the matches played by player:"))
    innings = int(input("Enter the innings:  "))
    runs = int(input("Enter total runs:"))
    bat_avg = float(input("Enter the batting average:"))
    strike_rate = float(input("Enter the strike rate of player:"))
    wickets = int(input("Enter the wickets of player:"))
    bowl_avg = float(input("Enter the the bowling average:"))
    economy = float(input("Enter the economy of player:"))

    stats = {
        format: {
            "matches": matches,
            "innings": innings,
            "runs": runs,
            "bat_avg": bat_avg,
            "strike_rate": strike_rate,
            "wickets": wickets,
            "bowl_avg": bowl_avg,
            "economy": economy,
        }
    }

    player_details = Player(player_id, name, role, stats)

    new_player = player_details.to_dict()
    players.append(new_player)

    save_players(players)


def view_players():
    players = load_players()

    for player in players:
        print("=" * 70)
        print(f"ID :{player['player_id']}")
        print(f"Name :{player['name']}")
        print(f"Role :{player['role']}")
        print("=" * 70)

        print(f"{'Statistics':15}|{'T20':12}|{'ODI':12}|{'Test':12}|")
        print("=" * 70)

        stat_fields = [
            ("Matches", "matches"),
            ("Innings", "innings"),
            ("Runs", "runs"),
            ("Bat Avg", "bat_avg"),
            ("Strike Rate", "strike_rate"),
            ("Wickets", "wickets"),
            ("Bowl Avg", "bowl_avg"),
            ("Economy", "economy"),
        ]

        for label, key in stat_fields:
            t20 = player["stats"].get("T20", {}).get(key, "-")
            odi = player["stats"].get("ODI", {}).get(key, "-")
            test = player["stats"].get("TEST", {}).get(key, "-")

            print(f"{label:15}|{t20:12}|{odi:12}|{test:12}|")
        print("=" * 70)


def search_player():

    player_id = input("Enter player ID to search: ")
    players = load_players()

    found = False

    for player in players:
        if player["player_id"] == player_id:
            print("\nPlayer Found")
            print("-" * 130)

            print(
                f"ID: {player['player_id']} | "
                f"Name: {player['name']} | "
                f"Role: {player['role']}"
            )

            print("-" * 130)

            print(f"{'Statistic':15}|{'T20':15}|{'ODI':15}|{'TEST':15}|")

            print("-" * 65)

            stats = player["stats"]

            fields = [
                ("Matches", "matches"),
                ("Innings", "innings"),
                ("Runs", "runs"),
                ("Bat Avg", "bat_avg"),
                ("Strike Rate", "strike_rate"),
                ("Wickets", "wickets"),
                ("Bowl Avg", "bowl_avg"),
                ("Economy", "economy"),
            ]

            for label, key in fields:
                t20 = stats.get("T20", {}).get(key, "-")
                odi = stats.get("ODI", {}).get(key, "-")
                test = stats.get("TEST", {}).get(key, "-")

                print(f"{label:15}|{str(t20):15}|{str(odi):15}|{str(test):15}|")

            print("-" * 65)

            found = True
            break

    if not found:
        print("Player does not exist!")


def update_player():

    player_id = input("Enter player ID to update: ")
    players = load_players()

    matching_player = None

    # Find player
    for player in players:
        if player["player_id"] == player_id:
            matching_player = player
            break

    if matching_player is None:
        print("Player does not exist!")
        return

    print("\nPlayer Found")
    print(f"ID: {matching_player['player_id']}")
    print(f"Name: {matching_player['name']}")
    print(f"Role: {matching_player['role']}")

    print("\nWhat do you want to update?")
    print("1. Name")
    print("2. Role")
    print("3. Format Statistics")

    choice = int(input("Enter your choice: "))

    
    if choice == 1:
        new_name = input("Enter new name: ")

        confirm = input("Confirm update? (Yes/No): ")

        if confirm.lower() == "yes":
            matching_player["name"] = new_name
            save_players(players)
            print("Player updated successfully!")
        else:
            print("Update cancelled.")

    
    elif choice == 2:
        new_role = input("Enter new role: ")

        confirm = input("Confirm update? (Yes/No): ")

        if confirm.lower() == "yes":
            matching_player["role"] = new_role
            save_players(players)
            print("Player updated successfully!")
        else:
            print("Update cancelled.")

    
    elif choice == 3:
        print("\nAvailable formats:")

        for format_name in matching_player["stats"]:
            print("-", format_name)

        format_name = input("Enter format to update (T20/ODI/TEST): ").upper()

        if format_name not in matching_player["stats"]:
            print("This format does not exist for this player.")
            return

        print("\nWhat do you want to update?")

        print("1. Matches")
        print("2. Innings")
        print("3. Runs")
        print("4. Batting Average")
        print("5. Strike Rate")
        print("6. Wickets")
        print("7. Bowling Average")
        print("8. Economy")

        stat_choice = int(input("Enter your choice: "))

        field_map = {
            1: "matches",
            2: "innings",
            3: "runs",
            4: "bat_avg",
            5: "strike_rate",
            6: "wickets",
            7: "bowl_avg",
            8: "economy",
        }

        type_map = {
            "matches": int,
            "innings": int,
            "runs": int,
            "bat_avg": float,
            "strike_rate": float,
            "wickets": int,
            "bowl_avg": float,
            "economy": float,
        }

        if stat_choice not in field_map:
            print("Invalid choice!")
            return

        selected_field = field_map[stat_choice]

        converter = type_map[selected_field]

        new_value = converter(input("Enter new value: "))

        confirm = input("Confirm update? (Yes/No): ")

        if confirm.lower() == "yes":
            matching_player["stats"][format_name][selected_field] = new_value

            save_players(players)

            print("Player statistics updated successfully!")

        else:
            print("Update cancelled.")

    else:
        print("Invalid choice!")


def delete_player():

    player_id = input("Enter player ID to delete: ")
    players = load_players()

    matching_player = None

    # Find player
    for player in players:
        if player["player_id"] == player_id:
            matching_player = player
            break

    if matching_player is None:
        print("Player ID does not exist!")
        return

    print("\nPlayer Found")
    print("-" * 50)

    print(f"ID: {matching_player['player_id']}")
    print(f"Name: {matching_player['name']}")
    print(f"Role: {matching_player['role']}")

    print("\nAvailable Formats:")
    for format_name in matching_player["stats"]:
        print("-", format_name)

    print("-" * 50)

    confirm_deletion = input(
        "Are you sure you want to delete this player? (Yes/No): "
    )

    if confirm_deletion.lower() == "yes":

        players.remove(matching_player)
        save_players(players)

        print("Player deleted successfully!")

    else:
        print("Deletion cancelled.")