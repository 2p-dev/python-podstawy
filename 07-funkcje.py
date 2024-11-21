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




