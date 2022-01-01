import requests
import pprint

# https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summonerName}
# https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion.json
# Current League Version: 11.24.1

champion_list = requests.get('https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion.json')

def define_champion(x):
    if x == 0:
        print('Galio')

my_key = 'RGAPI-2364cbfe-0ed2-463c-8398-363e28b7eedc'
username = input('Enter a Summoner name: ')


account = requests.get('https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + username + '?api_key=RGAPI-2364cbfe-0ed2-463c-8398-363e28b7eedc')
account_data = account.json()

print('Username: ', account_data['name'])
print('Summoner puuid: ', account_data['puuid'])
print('Summoner Level: ',account_data['summonerLevel'])
