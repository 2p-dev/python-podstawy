# utworzyć strukturę klas zawierającą figury geometryczne: figura (klasa bazowa), prostokąt, kwadrat (to też prostokąt), koło
# dla każdej figury podać wymagane parametry - prostokąta: długość, szerokość, kwadratu: długość, koła: promień
# każda z klas powinna implementować metody zwracające wartości: oblicz_obwod(), oblicz_powierzchnie()
# dla kwadratu skorzystać z obliczania obwodu oraz powierzchni klasy bazowej (prostokąta), podając bok kwadratu 2 razy

# utworzyć strukturę klas zawierającą figury geometryczne: figura (klasa bazowa), prostokąt, 
# kwadrat (to też prostokąt), koło
# dla każdej figury podać wymagane parametry - prostokąta: długość, szerokość, kwadratu: 
# długość, koła: promień
# każda z klas powinna implementować metody zwracające wartości: oblicz_obwod(), 
# oblicz_powierzchnie()
# dla kwadratu skorzystać z obliczania obwodu oraz powierzchni klasy bazowej (prostokąta), 
# podając bok kwadratu 2 razy
# utworzyc liste przykładowych obiektów i wykorzystując pętlę for, wywołać obliczanie obwodu i prostokąta

import math

class Figura():

    def wypisz(self):
        print('Figura')

    def oblicz_obwod():
        return None
    
    def oblicz_powierzchnie():
        return None


class Prostokat(Figura):

    def __init__(self, dlugosc, szerokosc):
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def wypisz(self):
        print(f'Prostokat, dlugosc: {self.dlugosc}, szerokosc: {self.szerokosc}')

    def oblicz_obwod(self):
        return 2 * self.dlugosc + 2 * self.szerokosc
    
    def oblicz_powierzchnie(self):
        return self.dlugosc * self.szerokosc


class Kwadrat(Prostokat):

    def __init__(self, dlugosc):
        super().__init__(dlugosc, dlugosc) # super().__init__ = wywolanie __init__ z klasy Prostokat
    def wypisz(self):

        print(f'Kwadrat: dlugosc: {self.dlugosc}')


class Kolo(Figura):

    def __init__(self, promien):
        self.promien = promien

    def wypisz(self):
        print(f'Kolo, promien: {self.promien}')

    def oblicz_obwod(self):
        return 2 * math.pi * self.promien
    
    def oblicz_powierzchnie(self):
        return math.pi * self.promien * self.promien

k = Kolo(5)
k.wypisz()
print('kolo obwod: ', k.oblicz_obwod(), 'powierzchnia: ', k.oblicz_powierzchnie())
kwadrat = Kwadrat(15)
kwadrat.wypisz()
print('Kwadrat obwod: ', kwadrat.oblicz_obwod(), 'powierzchnia: ', kwadrat.oblicz_powierzchnie())
pro = Prostokat (12, 5)
pro.wypisz()
print('Prostokat obwod: ', pro.oblicz_obwod(), 'powierzchnia: ', pro.oblicz_powierzchnie())

print('lista')
lista = [Kolo(7), Kwadrat(1), Prostokat(4, 2)]
for figura in lista:
    figura.wypisz()
    print('obwod: ', figura.oblicz_obwod(), 'powierzchnia: ', figura.oblicz_powierzchnie())



