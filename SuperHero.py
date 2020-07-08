import requests
import json

def heroes_iq(heroes):
	heroes_list = dict()
	for hero in heroes:
		heroes_list[hero] = 'iq'

	for hero in heroes_list.keys():
		response = requests.get(f'https://superheroapi.com/api/2765171893766865/search/{hero}')
		hero_data = response.json()
		heroes_list[hero]  = int(hero_data['results'][0]['powerstats']['intelligence'])

	print(heroes_list)

	for hero in heroes_list.keys():
		if heroes_list[hero] == max(heroes_list.values()):
			print(hero)

heroes_iq(['Hulk', 'Captain America', 'Thanos'])