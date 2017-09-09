import json, sys, random

API_URL = "http://stats.nba.com/stats/commonallplayers/?LeagueID=00&Season=2016-17&IsOnlyCurrentSeason=1"
PLAYERS_FILE = "players.json"
TEAM_SIZE = 1

def parse_players_json_file():
    with open(PLAYERS_FILE) as data_file:
        return json.load(data_file)

def parse_player_array_from_json(json):
    return json["resultSets"][0]['rowSet']

def get_valid_players_list(json):
    players = []
    for entry in json:
        if(is_valid_entry(entry)):
            players.append(entry[2] + " - " + entry[9]) #name - team
    return players

def is_valid_entry(entry):
    return len(entry[8]) > 0 #team name is not empty

def get_team(players):
    team = []
    for i in range(0, TEAM_SIZE):
        selected_player = random.choice(players)
        players.remove(selected_player)
        team.append(selected_player)
    return team

def print_team(team):
    for player in team:
        print player

if(len(sys.argv) < 3):
    print 'ARGS: num_teams team_size'
else:
    NUM_TEAMS = int(sys.argv[1])
    TEAM_SIZE = int(sys.argv[2])
    json = parse_player_array_from_json(parse_players_json_file())
    players = get_valid_players_list(json)
    for i in range (0, NUM_TEAMS):
        team = get_team(players)
        print 'Team #'+str(i+1)+':'
        print_team(team)
        print