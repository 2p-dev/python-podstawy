# https://www.python.org/downloads/
# https://code.visualstudio.com/

3 + 3
3*7
500 - 43 * 5
(1 - 7) * 7
8 * 3.5
8 * 3.25
4**2
8 / 5
8 % 5


# Hello World # błąd
"Hello World"
'Hello World'
# 'Hello 'World'' # błąd
'Hello "World"'
"Hello 'World'"


# 'doesn't' # błąd
"doesn't"
'doesn\'t'


"Hello" + "World"

'kawa' * 3
'kawa' + 3

"kawa" + "3"
"kawa" + str(3)



print("Witaj, co u Ciebie?")
print("Witaj", "co u Ciebie?")

print(4)
print(4, 6, 7)
print()

# Kod 1


zmienna = 5

type(zmienna)
# <class 'int'>



print("ala ma kota")
#lub
print('ala ma kota')
#lub
print('4*5', "=", 4*5) # zobaczysz: 4*5 = 20 # niezalecane mieszanie ograniczników ciągów znaków







napis = "To jest napis" # tekst zapisujemy w podwójnym cudzysłowie
napis2 = 'To także jest napis😮 \N{GREEK CAPITAL LETTER GAMMA}' # lub w pojedynczym apostrofie
print(napis+'\n'+ napis2)
print(type(napis)) # za pomocą funkcji type sprawdzisz typ swojej zmiennej


napis = """Ten tekst
zawiera kilka wierszy,
które zapisane sa w zmiennej napis!"""
print(napis)


a = 3; b = 4 # dwie instrukcje w jednym wierszu
print(a + b)



score = 10
if score >= 100: 
    print("Brawo!")


lista = [
   1,2,3, 
   4,5,6, 
]





class Osoba:

    def __init__(self, imie, nazwisko, miejsce_zamieszkania):
        self.imie = imie
        self.nazwisko = nazwisko
        self.miejsce_zamieszkania = miejsce_zamieszkania

    def przedstaw_sie(self):
        print("Nazywam się {0} {1}".format(self.imie, self.nazwisko))

    def moje_miejsce_zamieszkania(self):
        print(f"Mieszkam w: {self.miejsce_zamieszkania}")


os = Osoba("Piotr", "Piwowarczyk", "Kielce")
os.przedstaw_sie()
os.moje_miejsce_zamieszkania()




# to jest komentarz 
print("Dzień dobry") # to też jest komentarz

# print(“Dowidzenia”) # to się nie wykona

"""
komentarz
wielolinijkowy
"""





# Kod 2

x = 111
print(x, 3*2, 'hello!') # 111 6 hello!





print('ala ma kota', end = ' ')

print("jeden", "dwa", "trzy", sep="*")
# jeden*dwa*trzy

print("""ala
ma 
kota""")

x = 10
print('ala ma {0} lat'.format(x))
txt1 = "Jestem {imie}, mam {wiek} lat".format(imie = "Ala", wiek = 10)
print(txt1)


x = 10
print(f'ala ma {x} lat')



# f"{liczba:.nf}")

print(f"{5/7:.6f}") 
# 0.714286



print("ala\tma\n\n\' \\kota/ \"")


x = input() # podajmy np 22
print(x) # zostanie wypisane 22


x = input('Podaj dwie liczby: ') # np. 3 i 4
print(x) 
# 3 4
a, b = x.split() #zapiszemy kolejne wartości do tablicy x
print('Pierwsza liczba:', a, 'Druga liczba:', b) 



a, b = input('Podaj dwie liczby: ').split() # np. 2 i 3
print('Pierwsza liczba:', a, 'Druga liczba:', b) 



x = 10 # x jest zmienną typu całkowitego
print(x)
x = 'ala ma kota' # a teraz jest zmienną typu string
print(x)


x = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
y = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
print(x+y)


x = 4.25 # liczba typu float
print(x)
print(type(x))
y = 2/3 # liczba typu float
print(y)
print(type(y))


print(format(2/3, '.2f')) # 0.67

print(f"{2/3:.2f}") # 0.67
txt1 = "Jestem {imie}, mam {wiek} lat".format(imie = "Piotr", age = 40)


x = 10
print(f'ala ma {x} lat')


x = True
print(x) # True
print(type(x)) # 
y = 1 == 2 # przypisujemy wartość logiczną warunku, w tym przypadku 1 == 2 ma wartość False
print(y) # False


x = 48 + 22j
print(x) # (48 + 22j)
print(type(x)) # <class 'complex'>



x = '1234' #  typ str
print(type(x)) # 
x = int(x) # wykonujemy rzutowania zmiennej typu str na typ int
print(type(x)) # 



x = '12a34' #  typ str
print(type(x)) # 
x = int(x) # wykonujemy rzutowania zmiennej typu str na typ int
print(type(x)) # 


a = 5
b = 3
c = a / b
print(c) # zostanie wypisane 1.6666666666666667
c = a // b
print(c) # zostanie wypisane 1 — część całkowita z dzielenia 5 przez 3
c = a ** b
print(c) # zostanie wypisany wynik 5 do potęgi 3 = 125


a = 5
print(4 <= a <= 6) # zwraca True

n = 5
k = 7
print(n > 3 or k > 10) # zostanie wypisane True, ponieważ przynajmniej jeden warunek musi mieć wartość logiczną True (musi być prawdziwy)
print(n > 3 and k > 10) # zostanie wypisane False, ponieważ wszystkie warunki muszą mieć wartość logiczną True
print(not(n > 3 and k > 10)) # zostanie wypisane True, ponieważ zaprzeczamy wartość logiczną False, którą otrzymujemy z warunków (n > 3 and k > 10)


a = 5
b = 5
if a == b:
    print("wartości zmiennych a i b są takie same")
a = 11
if a != b:
    print('wartości zmiennych a i b są różne')
if a > b:
    print('a jest większe od b')


a = 45 # przypisanie liczby 45 do zmiennej a
print(a)
b = a # przypisanie do zmiennej b wartości przechowywanej przez zmienną a, czyli liczbę 45
print(b)
a = 2 ** 10 # przypisanie do zmiennej a wyniku działania 2 do potęgi 10 = 1024
print(a)


a = 45
print(a)
a += 10 # zwiększenie wartości zmiennej a o 10 (teraz a = 55)
print(a)
a -= 50 # zmniejszenie wartości zmiennej a o 50 (teraz a = 5)
print(a)
a **= 3 # wykonanie potęgowania 5 do 3 i zapisanie wyniku w zmiennej a (teraz a = 125)
print(a)
a //= 30 # wykonanie dzielenia całkowitego 125 // 30 = 4 (teraz a = 4)
# itd.



tekst_uzytkownika = input('podaj liczbę')
liczba = int(tekst_uzytkownika)
if liczba < 0:
    print('Liczba jest mniejsza od 0')
elif liczba > 10:
    print('Liczba jest większa od 10')
else:
    print('Liczba jest pomiędzy 0 a 10')


wiek_str = input("Podaj wiek")
print("tak" if int(wiek_str) >= 18 else "nie")





x = "ala ma kota"
y = "ala nie ma kota"
if x is not y:
    print("Obiekty x i y to nie te same obiekty")
x = y
if x is y:
    print("Obiekty x i y to  te same obiekty")


x = "ala ma kota"
y = 25
if type(x) is str:
    print("obiekt x jest typem str")

if type(y) is int:
    print("obiekt x jest typem int")



tekst = "ala ma kota"
if "ma" in tekst:
    print("wyraz 'ma' występuje w ciągu'", tekst, "'")
lista = [2, 3, 4, 100]
if 4 in lista:
    print("Liczba 4 występuje w zbiorze", lista)
else:
    print("Liczba 4 nie występuje w zbiorze", lista)


## Pętle

# while-do loop
while test:     # nie potrzeba nawiasów
    true_block
else:           # opcjonalnie, jeżeli warunek nie jest spełniony
    else_block


# for-each loop
for item in sequence:
    true_block
else:           # opcjonalnie, jeżeli warunke nie jest spełniony
    else_block


wartosc = 101
while wartosc > 100 and wartosc <110:
    wartosc += 1
    print('wartość jest pomiędzy 100 a 110')
else:
    print('wartość jest spoza zakresu')




for i in range(11):
    print(i)


for i in range(10, 20):
    print(i)


oceny = [4, 5, 2, 4]
suma = 0
for ocena in oceny:
    print(f'Ocena to {ocena}')
    suma += ocena

srednia = suma / len(oceny)
print(srednia) 



a = int(input("Podaj początek zakresu: "))
b = int(input("Podaj koniec zakresu: "))

for i in range(a, b+1):
    if i % 2 == 0: # jeśli liczba jest parzysta to przechodzimy do kolejnej iterację pętli
        continue
    print(i)






    
import math 
#importujemy bibliotekę
print(f'Pierwiastek z liczby 2 wynosi {math.sqrt(2)}') 
# Pierwiastek z liczby 2 wynosi 1.4142135623730951

import math as m 
#importujemy bibliotekę
print(f'Pierwiastek z liczby 2 wynosi {m.sqrt(2)}') 
# Pierwiastek z liczby 2 wynosi 1.4142135623730951

from math import * 
#importujemy wszystko z modułu math - niezalecane
print(f'Pierwiastek z liczby 2 wynosi {sqrt(2)}') 
# Pierwiastek z liczby 2 wynosi 1.4142135623730951


from math import *
#importujemy wszystko z modułu math
print(f'Pierwiastek z liczby 2 wynosi {sqrt(2)}') 
# Pierwiastek z liczby 2 wynosi 1.4142135623730951

import math, os, time 
#importujemy wiele modułów oddzielając je przecinkiem
print(f'Pierwiastek z liczby 2 wynosi {sqrt(2)}') 
# Pierwiastek z liczby 2 wynosi 1.4142135623730951


# W terminalu poza Pythonem
# pip install matplotlib


import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [1**2, 2**2, 3**2, 4**2, 5**2]
plt.plot(x, y)
plt.show()


"""
with ... as ...:
    instrukcje
   
# More than one items
with ... as ..., ... as ..., ...:
    instrukcje

"""

with open('test.log', 'r') as infile:  # automatically close the file at the end of with
    for line in infile:
        print(line)

infile = open('test.log', 'r')
try:
    for line in infile:
        print(line)
finally:
    infile.close()