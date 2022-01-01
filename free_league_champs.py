import requests

champion_list = requests.get('https://ddragon.leagueoflegends.com/cdn/11.24.1/data/en_US/champion.json')
champ_list = champion_list.json()

rotation = requests.get('https://na1.api.riotgames.com/lol/platform/v3/champion-rotations?api_key=RGAPI-2364cbfe-0ed2-463c-8398-363e28b7eedc')
rotation_data = rotation.json()

def get_champ_name(champ_id):
    for champion_name, value in champ_list["data"].items():
        if value["key"] == champ_id:
            return champion_name

for index, champion_id in enumerate(rotation_data['freeChampionIds']):
    champ_str = str(champion_id)
    # print(index + 1, ': ', get_champ_name(champ_str))
    print(f"{index + 1}: {get_champ_name(champ_str)}")