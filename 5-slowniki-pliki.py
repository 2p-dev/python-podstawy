# utworzyc liste slownikow z wartosciami,
# zapisac ją do pliku, wczytać z pliku
import json
import io

dane = [
    {'imie': 'Bogdan', 'wiek': 55},
    {'imie': 'Jagoda', 'wiek': 48},
]
dane.append({'imie': 'Piotr', 'wiek': 30})
print(dane)
print(dane[-1]['imie'])

dane_txt = json.dumps(dane)
print(dane_txt)

with open('plik-dane.txt', 'w') as f:
    f.write(dane_txt)

with open('plik-dane.txt', 'r') as f2:
    dane2_txt = f2.read()
    dane_wczytane = json.loads(dane2_txt)

print('wczytane z pliku: ', dane_wczytane)
print(dane_wczytane[1]['wiek'])

