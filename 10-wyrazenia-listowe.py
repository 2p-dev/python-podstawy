import requests
import json

# poprzednio omawiany przykład 

x = requests.get('https://danepubliczne.imgw.pl/api/data/synop/format/json')
python_list = json.loads(x.text)
for dane_stacji in python_list:
    if dane_stacji['stacja'] == 'Kielce':
        print(dane_stacji['temperatura'])

# pętla zapisane jako wyrażenie listowe:

lista_stacji_kielce = [dane_stacji for dane_stacji in python_list if dane_stacji['stacja'] == 'Kielce']
print(lista_stacji_kielce[0]['temperatura']) # założenie że przynajmniej jedna stacja Kielce zawsze istnieje