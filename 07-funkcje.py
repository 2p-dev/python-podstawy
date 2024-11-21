def narysuj_linie(): # funkcja bez parametrow
    print(40 * "=")

narysuj_linie()
narysuj_linie()

# funkcja z jednym parametrem, bez zwracania wartosci
def narysuj_linie_2(dlugosc): 
    print(dlugosc * "=")
    return 
    # return bez zwracania wartości jest opcjonalne na zakończenie


def suma(a, b):  # funkcja z dwoma parametrami zwracająca wartość
    return a + b # zwrócenie wyniku sumy dwóch liczb 


print(suma(3, 5))  # Wynik: 8


def funkcja_z_wartoscia_domyslna(a, b = 10):
    return a * b

print(funkcja_z_wartoscia_domyslna(4)) # Wynik 40



# funkcja lambda

# lambda argumenty: wyrażenie

dodawanie = lambda x, y: x + y 

wynik = dodawanie(3, 5) # wynik będzie równy 8

# filtrowanie liczb parzystych
liczby = [1, 2, 3, 4, 5, 6] 
parzyste = list(filter(lambda x: x % 2 == 0, liczby)) # parzyste będzie [2, 4, 6]


# mapowanie jednej listy na drugą - ze wszystkimi elementami pomnożonymi razy 2
lista = [1, 2, 3, 4]
rezultat = list(map(lambda x: x* 2, lista)) # Wynik [2, 4, 6, 8]


# mapowanie jednej listy na drugą - ze wszystkimi elementami, które są większe od 4, zwiększonymi o 1
lista = [2, 4, 6, 8]
rezultat = list(map(lambda x: x+1, filter(lambda x: x > 4, lista))) # Wynik [7, 9]



# Listy składane / wyrażenia listowe (list comprehension)

nowa_lista = [transformacja(x) for x in stara_lista]

# Jest równoznaczne z:
nowa_lista = []
for x in stara_lista:
    nowa_lista.append(transformacja(x))


imiona = ["Ada", "Basia", "Celina"]
imiona_duze = [imie.upper() for imie in imiona]
print(imiona_duze)  # ['ADA', 'BASIA', 'CELINA']



liczby = [x + 1 for x in [0, 1, 2, 3, 4]]
print(liczby)  # [1, 2, 3, 4, 5]

# wyrażenie listowe z warunkiem
liczby = [x + 1 for x in range(0, 5) if x > 2]
print(liczby)  # [4, 5]

# powyższe jest równoznaczne z:
liczby = []
for i in range(0, 5):
    if x > 2:
        liczby.append(x + 1)

