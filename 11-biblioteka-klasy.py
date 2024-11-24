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


class Ksiazka:
    def __init__(self, id_ksiazki, tytul, autor, rok_wydania, liczba_egzemplarzy):
        self.id_ksiazki = id_ksiazki
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania
        self.liczba_egzemplarzy = liczba_egzemplarzy
    def wyswietl(self):
        print(f'{self.id_ksiazki}: Tytuł: "{self.tytul}", Autor: "{self.autor}", Rok wydania: {self.rok_wydania}, egzemplarze: {self.liczba_egzemplarzy}')
    def wypozycz(self):
        if self.liczba_egzemplarzy == 0:
            print('Nie ma dostępnych egzemplarzy')
        else:
            self.liczba_egzemplarzy -= 1
    def zwroc(self):
        self.liczba_egzemplarzy += 1

# biblioteka = {
#     1: ['Wiedźmin', 'Andrzej Sapkowski', 1993, 5],
#     2: ['Dziady', 'Adam Mickiewicz', 1823, 2]
# }

# biblioteka = {
#     "1": ['Wiedźmin', 'Andrzej Sapkowski', 1993, 5],
#     "2": ['Dziady', 'Adam Mickiewicz', 1823, 2]
# }

# biblioteka_klasy = {
#     "1": Ksiazka("1", 'Wiedźmin', 'Andrzej Sapkowski', 1993, 5),
#     "2": Ksiazka("2", 'Dziady', 'Adam Mickiewicz', 1823, 2)
# }


try:
    with open('biblioteka-klasy.json', 'r') as f:
        try:
            biblioteka = json.load(f)
            biblioteka_klasy = {}
            for klucz in biblioteka:
                ksiazka_arr = biblioteka[klucz]
                biblioteka_klasy[klucz] = Ksiazka(klucz, ksiazka_arr[0], ksiazka_arr[1], ksiazka_arr[2], ksiazka_arr[3])
        except json.JSONDecodeError as ex:
            print(f'Błąd wczytywania pliku biblioteka.json {ex}')
            biblioteka_klasy = {}
except FileNotFoundError as ex:
    print(f'Błąd wczytywania pliku biblioteka.json, plik nie istnieje {ex}')
    biblioteka_klasy = {}


def wyswietl_ksiazki(biblioteka_klasy):
    print('Biblioteka')
    for klucz in biblioteka_klasy:
        ksiazka = biblioteka_klasy[klucz]
        ksiazka.wyswietl()


def dodaj_ksiazke(biblioteka, id_ksiazki, tytul, autor, rok_wydania, liczba_egzemplarzy):
    ksiazka = Ksiazka(id_ksiazki, tytul, autor, rok_wydania, liczba_egzemplarzy)
    biblioteka[id_ksiazki] = ksiazka


def wypozycz_ksiazke(bilioteka_klasy, id_ksiazki):
    ksiazka = bilioteka_klasy.get(id_ksiazki)
    if not ksiazka:
        print('Nie ma dostępnych egzemplarzy')
    else:
        ksiazka.wypozycz()


def zwoc_ksiazke(bilioteka_klasy, id_ksiazki):
    ksiazka = bilioteka_klasy.get(id_ksiazki)
    if not ksiazka:
        print('To nie jest ksiazka z naszej biblioteki')
    else:
        ksiazka.zwroc()


def usun_ksiazke(bilioteka_klasy, id_ksiazki):
    if id_ksiazki in bilioteka_klasy:
        del bilioteka_klasy[id_ksiazki]
    else:
        print('To nie jest ksiazka z naszej biblioteki')


def zapisz_biblioteke(biblioteka_klasy):
    biblioteka = {}
    for klucz in biblioteka_klasy:
        ksiazka = biblioteka_klasy[klucz]
        biblioteka[klucz] = [ksiazka.tytul, ksiazka.autor, ksiazka.rok_wydania, ksiazka.liczba_egzemplarzy]
    with open('biblioteka-klasy.json', 'w') as f:
        biblioteka_json = json.dump(biblioteka, f)


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


# wyswietl_ksiazki(biblioteka_klasy)
# dodaj_ksiazke(biblioteka_klasy, 3, 'Rozdroże kruków', 'Andrzej Sapkowski', 2024, 100)
# wyswietl_ksiazki(biblioteka_klasy)
# wypozycz_ksiazke(biblioteka_klasy, 1)
# wyswietl_ksiazki(biblioteka_klasy)
# zwoc_ksiazke(biblioteka_klasy, 1)
# wyswietl_ksiazki(biblioteka_klasy)
# usun_ksiazke(biblioteka_klasy, 3)
# wyswietl_ksiazki(biblioteka_klasy)


print('Biblioteka')
wyswietl_menu()
if obsluga_mowy:
    powiedz_menu()
while True:
    try: # zabezpiecza polecenie == 2, bo inne polecenia są już obsłużone
        polecenie = input('Wybierz opcję: ')
        if polecenie == '1':
            wyswietl_ksiazki(biblioteka_klasy)
        elif polecenie == '2':
            id_ksiazki = input('Podaj ID książki: ')
            tytul = input('Podaj tytuł: ')
            autor = input('Podaj autora: ')
            rok_wydania = int(input('Podaj rok wydania: '))
            ilosc_egzemplarzy = int(input('Podaj liczbę egzemplarzy: '))
            dodaj_ksiazke(biblioteka_klasy, id_ksiazki, tytul, autor, rok_wydania, ilosc_egzemplarzy)
        elif polecenie == '3':
            id_ksiazki = input('Podaj ID książki do wypożyczenia: ')
            wypozycz_ksiazke(biblioteka_klasy, id_ksiazki)
        elif polecenie == '4':
            id_ksiazki = input('Podaj ID książki do zwrócenia: ')
            zwoc_ksiazke(biblioteka_klasy, id_ksiazki)
        elif polecenie == '5':
            id_ksiazki = input('Podaj ID książki do usunięcia: ')
            usun_ksiazke(biblioteka_klasy, id_ksiazki)
        elif polecenie == '6':
            zapisz_biblioteke(biblioteka_klasy)
            break
    except ValueError:
        print('Wprowadzono błędne dane')
