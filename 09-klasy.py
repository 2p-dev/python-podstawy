
class Osoba:
    pass # Pusty blok

o = Osoba()
print(o)
# <__main__.Osoba object at 0x0000019028620280>



class Osoba:
    def przywitaj_sie(self):
        print('Witaj, jak się masz?')

o = Osoba()
o.przywitaj_sie()

# Ten krótki przykład można także zapisać jako Osoba().przywitaj_sie()


class Osoba:
    def __init__(self, imie):
        self.imie = imie
    def przywitaj_sie(self):
        print (f'Witaj, mam na imię {self.imie}')

o = Osoba('Adam')
o.przywitaj_sie()




class Robot:
    # Zmienna klasy pokazująca liczbę robotów
    # Odpowiednik zmiennej statycznej
    populacja = 0

    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.__nazwa_duza = nazwa.upper()
        print(f'Inicjalizacja robota o nazwie {nazwa}')

        Robot.populacja += 1

    def __del__(self):
        print(f'Usunięcie robota o nazwie {self.nazwa}')

        Robot.populacja -= 1

        if Robot.populacja == 0:
            print(f'{self.nazwa} był ostatnim robotem.')
        else:
            print(f'Postały {Robot.populacja} roboty.')

    # domyślnie metody w klasie to classmethod
    def przywitaj_sie(self): 
        print(f'Dzień dobry, jestem {self.__nazwa_duza}')

    # metoda klasy a nie obiektu to metoda statyczna
    # nie zawiera parametru self
    def wypisz_populacje():
        print(f'Populacja robotów: {Robot.populacja}')
    wypisz_populacje = staticmethod(wypisz_populacje) 

    @staticmethod
    def czy_populacja_pusta():
        return Robot.populacja == 0
    



droid1 = Robot('r2-d2')
droid1.przywitaj_sie()
Robot.wypisz_populacje()
Robot.czy_populacja_pusta()

droid2 = Robot('c-3po')
droid2.przywitaj_sie()
# print(droid2.__nazwa_duza) nie zadziala bo to zmienna prywatna
Robot.wypisz_populacje()

del droid1
del droid2

Robot.wypisz_populacje()
print(f'czy populacja pusta?: {Robot.czy_populacja_pusta()}')



##### Dziedziczenie


class Osoba:
    def __init__(self, imie, staz):
        self.imie = imie
        self.wiek = staz
        print(f'Inicjalizacja Osoby: {self.imie}')

    def powiedz(self):
        print(f'Imię: {self.imie}, wiek: {self.wiek}')

class Wykladowca(Osoba):
    def __init__(self, imie, wiek, staz):
        Osoba.__init__(self, imie, wiek)
        self.staz = staz
        print(f'Inicjalizacja Wykladowcy: {self.imie}')

    def powiedz(self):
        Osoba.powiedz(self)
        print(f'Staż: {self.staz}')

class Uczen(Osoba):
    def __init__(self, imie, wiek, oceny):
        Osoba.__init__(self, imie, wiek)
        self.oceny = oceny
        print(f'Inicjalizacja Studenta: {self.imie})')

    def powiedz(self):
        Osoba.powiedz(self)
        print(f'Oceny: {self.oceny}')

w = Wykladowca('Piotr', 40, 15)
s = Uczen('Zofia', 29, [3.0, 5.0, 5.0, 4.5])


osoby = [w, s]
for osoba in osoby:
    osoba.powiedz() # działa zarówno dla Wykładowców, jak i Uczniów