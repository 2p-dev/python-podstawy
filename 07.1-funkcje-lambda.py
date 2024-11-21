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


# sumowanie elementów listy z wykorzystaniem reduce
from functools import reduce
lista = [2, 4, 6, 8]
rezultat = reduce(lambda x, y: x + y, lista, 0) # 0 to element początkowy, podstawiany za zmienną x przy pierwszym przejściu pętli
# Wynik 20
