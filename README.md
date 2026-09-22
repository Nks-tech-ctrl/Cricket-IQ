# Cricket IQ

Cricket IQ is a command-line application for storing and analysing cricket-player statistics. It keeps player profiles and format-specific performance data in a local JSON file.

## Features

- Add player profiles with a role and statistics for T20, ODI, or Test cricket.
- View all stored players in a format comparison table.
- Search, update, and delete players by player ID.
- View statistics for every player in a chosen format.
- View a selected player's statistics for a chosen format.
- Compare two players side by side.
- Create format-specific leaderboards for runs, wickets, averages, strike rate, and economy.

## Requirements

- Python 3.8 or later

The project uses only Python's standard library, so no package installation is required.

## Run the application

From the project directory, run:

```powershell
python main.py
```

Choose an option from the interactive menu to manage players or explore their statistics. Enter `10` to exit.

## Data storage

Player records are saved in `Data/player.json`. Each record has this shape:

```json
{
  "player_id": "P002",
  "name": "Player Name",
  "role": "BATTER",
  "stats": {
    "T20": {
      "matches": 100,
      "innings": 95,
      "runs": 3500,
      "bat_avg": 42.5,
      "strike_rate": 138.2,
      "wickets": 0,
      "bowl_avg": 0.0,
      "economy": 0.0
    }
  }
}
```

The same structure supports `ODI` and `TEST` statistics. Player IDs are generated sequentially in the form `P001`, `P002`, and so on.

## Project structure

```text
Cricket IQ/
├── main.py             # Interactive application menu
├── player.py           # Player management and statistics functions
└── Data/player.json    # Persistent player data
```

## Note for macOS and Linux

The code currently refers to the data directory as `data/player.json`, while the repository directory is named `Data`. Windows treats these names as equivalent, but case-sensitive file systems do not. Before running there, rename `Data` to `data`, or update the paths in `player.py` to `Data/player.json`.
