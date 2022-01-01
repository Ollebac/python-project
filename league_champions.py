import requests
import pprint
import json

champion_request = requests.get('https://ddragon.leagueoflegends.com/cdn/11.24.1/data/en_US/champion.json')
championes = champion_request.json()
# champs = json.loads(championes)

if "key" in championes:
    print("key exists")

# for i in championes['data']:

# print(['data']['key'])

# print("Type: ", type(champs))

# print("hellooooo")

# champs = champion_request.json()

# name = 'Aatrox'
# def get_champ_id():
#     for i in champs:
#         if champs['data'] == 'Aatrox':
#             print('Helloooooo')
#             print(champs['data']['Aatrox']['key'])
#     print('Function was called.')

# get_champ_id()

# print(champs['data']['name'])

# print(champs["data"]['Aatrox'])

# print(champs['data']['Aatrox']['key'])

# file_object = open("sample_file.txt","a")
# file_object.write(champs['data'],['Aatrox']['key'])

# pprint.pprint(champs)


# pprint.pprint(champs)
# champion_list = json.loads(champs)

# print(champs['data']['Aatrox']['key'])

# print(champion_list['data'])
# print(champion_list[0]['key'])


# for i in champion_list['data']:
#     if champion_list['data']['key']

