# Napisz program, który będzie wykonywał różne operacje na listach. Wykonaj poniższe kroki:
# Utworzenie listy:
# Utwórz listę liczby zawierającą co najmniej 10 różnych liczb całkowitych, w tym zarówno dodatnie, jak i ujemne.
# Operacje na liście:
# Wypisz wszystkie elementy listy.
# Oblicz i wyświetl sumę wszystkich liczb w liście.
# Znajdź i wypisz największy oraz najmniejszy element listy.
# Oblicz i wyświetl, ile jest liczb dodatnich w liście.

lista = [-40, 33, 98, 1, 15, -40, 3, -22, 1, 7, 67, 100]
print(lista)
print('długość:', len(lista))
print('suma:', sum(lista))

suma = 0
for i in lista:
    suma += i
print('suma 2:', suma)

najmniejszy = min(lista)
najwiejszy = max(lista)
print('najmniejszy: ', najmniejszy)
print('najwiejszy: ', najwiejszy)

# Oblicz i wyświetl, ile jest liczb dodatnich w liście.
licznik_dodatnich = 0
for i in lista:
    if i > 0:
        licznik_dodatnich += 1
print('licznik_dodatnich: ', licznik_dodatnich)

# Utwórz nową listę zawierającą tylko liczby ujemne z listy liczby.
# Za pomocą pętli for

liczby_ujemne = []
for i in lista:
    if i < 0:
        liczby_ujemne.append(i)
print('liczby_ujemne', liczby_ujemne)

# Za pomocą wyrażenia listowego
liczby_ujemne_2 = [i for i in lista if i < 0]
print('liczby_ujemne_2', liczby_ujemne_2)

# Znajdź na liście najmniejszą liczbę i ją usuń.
najmniejsza = min(lista)
indeks_najmniejszej = lista.index(najmniejsza)
print(indeks_najmniejszej)
del lista[indeks_najmniejszej]
print(lista)

# co jakby lista byla pusta
lista2 = []
try:
    najmniejsza = min(lista2)
    indeks_najmniejszej = lista2.index(najmniejsza)
    print(indeks_najmniejszej)
    del lista2[indeks_najmniejszej]
except ValueError:
    print("Lista nie zawiera elementów")


lista = [-40, 33, 98, 1, 15, -40, 3, -22, 1, 7, 67, 100, -9]
najmniejsza = min(lista)
while True:
    try:
        indeks_najmniejszej = lista.index(najmniejsza)
        del lista[indeks_najmniejszej]
    except ValueError:
        break
print(lista)


# Posortuj listę liczby rosnąco i wypisz wynik.
lista.sort()
print('posortowana lista: ', lista)

# Usuń z listy najmniejszą liczbę (po wykonaniu sortowania).
del lista[0]
print('usuniecie najmniejszego: ', lista)

# Dodaj do listy nowy element: 0, w odpowiednim miejscu tak aby lista nadal była posortowana
lista.insert(1, 0) 

print('wstawienie 0: ', lista)

# Sprawdź, czy w liście znajduje się liczba 7. Jeśli tak, wypisz komunikat: 
# "Liczba 7 jest w liście", w przeciwnym razie wypisz: "Liczba 7 nie jest w liście".

znaleziono_7 = False
for i in lista:
    if i == 7:
        znaleziono_7 = True
        break

if znaleziono_7:
    print("Liczba 7 jest w liście")
else:
    print("Liczba 7 nie jest w liście")

# alternatywa
if len([i for i in lista if i == 7]) > 0:
    print("Liczba 7 jest w liście")
else:
    print("Liczba 7 nie jest w liście")

# Pobierz ostatni element
print('ostatni element: ', lista[-1])

# Pobierz elementy od drugiego do piątego
print('elementy 2-5: ', lista[1:5])

# Pobierz elementy od początku do dziesiątego,
print('elementy od początku do dziesiątego,: ', lista[:10])

# co drugi
print('co drugi: ', lista[::2])
