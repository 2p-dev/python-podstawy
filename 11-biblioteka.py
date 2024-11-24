import pyttsx3
import json

obsluga_mowy = False # można zmienić na True

if obsluga_mowy:
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    for voice in voices:
        if 'TTS_MS_PL' in voice.id:
            engine.setProperty("voice", voice.id)
    newVoiceRate = 145
    engine.setProperty('rate',newVoiceRate)
    engine.say("Dzień dobry, witamy w bibliotece.")
    engine.runAndWait()


# biblioteka = {
#     1: ['Wiedźmin', 'Andrzej Sapkowski', 1993, 5],
#     2: ['Dziady', 'Adam Mickiewicz', 1823, 2]
# }
# biblioteka = {
#     "1": ['Wiedźmin', 'Andrzej Sapkowski', 1993, 5],
#     "2": ['Dziady', 'Adam Mickiewicz', 1823, 2]
# }

with open('biblioteka.json', 'r') as f:
    try:
        biblioteka = json.load(f)
    except json.JSONDecodeError as ex:
        print(f'Błąd wczytywania pliku biblioteka.json {ex}')
        biblioteka = {}


def wyswietl_ksiazki(biblioteka):
    print('Biblioteka')
    for klucz in biblioteka:
        ksiazka = biblioteka[klucz]
        print(f'{klucz}: Tytuł: "{ksiazka[0]}", Autor: "{ksiazka[1]}", Rok wydania: {ksiazka[2]}, egzemplarze: {ksiazka[3]}')


def dodaj_ksiazke(biblioteka, id_ksiazki, tytul, autor, rok_wydania, liczba_egzemplarzy):
    ksiazka = [tytul, autor, rok_wydania, liczba_egzemplarzy]
    biblioteka[id_ksiazki] = ksiazka


def wypozycz_ksiazke(bilioteka, id_ksiazki):
    ksiazka = biblioteka.get(id_ksiazki)
    if not ksiazka:
        print('Nie ma dostępnych egzemplarzy')
    else:
        if ksiazka[3] == 0:
            print('Nie ma dostępnych egzemplarzy')
        else:
            ksiazka[3] -= 1


def zwoc_ksiazke(bilioteka, id_ksiazki):
    ksiazka = biblioteka.get(id_ksiazki)
    if not ksiazka:
        print('To nie jest ksiazka z naszej biblioteki')
    else:
        ksiazka[3] += 1


def usun_ksiazke(bilioteka, id_ksiazki):
    if id_ksiazki in biblioteka:
        del biblioteka[id_ksiazki]
    else:
        print('To nie jest ksiazka z naszej biblioteki')


def wyswietl_menu():
    print('1. Wyświetl wszystkie książki')
    print('2. Dodaj nową książkę')
    print('3. Wypożycz książkę')
    print('4. Zwróć książkę')
    print('5. Usuń książkę')
    print('6. Wyjście')


def powiedz_menu():
    tekst = ''
    tekst += '1 Wyświetl wszystkie książki,'
    tekst += '2 Dodaj nową książkę,'
    tekst += '3 Wypożycz książkę,'
    tekst += '4 Zwróć książkę,'
    tekst += '5 Usuń książkę,'
    tekst += '6 Wyjście.'
    engine.say(tekst)
    engine.runAndWait()


wyswietl_ksiazki(biblioteka)
dodaj_ksiazke(biblioteka, 3, 'Rozdroże kruków', 'Andrzej Sapkowski', 2024, 100)
wyswietl_ksiazki(biblioteka)
wypozycz_ksiazke(biblioteka, 1)
wyswietl_ksiazki(biblioteka)
zwoc_ksiazke(biblioteka, 1)
wyswietl_ksiazki(biblioteka)
usun_ksiazke(biblioteka, 3)
wyswietl_ksiazki(biblioteka)


print('Biblioteka')
wyswietl_menu()
if obsluga_mowy:
    powiedz_menu()
while True:
    try: # zabezpiecza polecenie == 2, bo inne polecenia są już obsłużone
        polecenie = input('Wybierz opcję: ')
        if polecenie == '1':
            wyswietl_ksiazki(biblioteka)
        elif polecenie == '2':
            id_ksiazki = input('Podaj ID książki: ')
            tytul = input('Podaj tytuł: ')
            autor = input('Podaj autora: ')
            rok_wydania = int(input('Podaj rok wydania: '))
            ilosc_egzemplarzy = int(input('Podaj liczbę egzemplarzy: '))
            dodaj_ksiazke(biblioteka, id_ksiazki, tytul, autor, rok_wydania, ilosc_egzemplarzy)
        elif polecenie == '3':
            id_ksiazki = input('Podaj ID książki do wypożyczenia: ')
            try:
                wypozycz_ksiazke(biblioteka, id_ksiazki)
            except ValueError:
                print('Wprowadzono błędny id książki')
        elif polecenie == '4':
            id_ksiazki = input('Podaj ID książki do zwrócenia: ')
            try:
                zwoc_ksiazke(biblioteka, id_ksiazki)
            except ValueError:
                print('Wprowadzono błędny id książki')
        elif polecenie == '5':
            id_ksiazki = input('Podaj ID książki do usunięcia: ')
            try:
                usun_ksiazke(biblioteka, id_ksiazki)
            except ValueError:
                print('Wprowadzono błędny id książki')
        elif polecenie == '6':
            with open('biblioteka.json', 'w') as f:
                biblioteka_json = json.dump(biblioteka, f)
            break
    except ValueError:
        print('Wprowadzono błędne dane')
