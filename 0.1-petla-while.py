"""
+ Wykorzystując pętlę nieskończoną - while True:
+ poproś użytkownika o wpisanie tekstu. 
+ Jeżeli jest on równy “quit” albo "koniec" - zakończ działanie pętli.
+ Jeżeli 'kwadrat' - poproś o podanie liczby i wypisz pole powierzchni kwadratu o podanym wymiarze (dlugosc ** 2)
+ Jeżeli prostokąt - poproś o podanie dwóch liczb i wypisz pole powierzchni prostokąta o podanych wymiarach (dlugosc * szerokosc)
"""

print('dostępne polecenia:')
print('\tq - zakoneczenie programu')
print('\tprostokat - obliczenie pola prostokata')
print('\tkwadrat - obliczenie pola kwadratu')

while True:
    polecenie = input('podaj polecenie: ')
    print(f'polecenie: {polecenie}')
    if polecenie == 'quit' or polecenie == 'koniec' or polecenie == 'q':
        print('koniec programu')
        break
    elif polecenie == 'kwadrat':
        bok = int(input('Podaj bok kwadratu: '))
        print(f"Powierzchnia kwadratu o boku {bok} to {bok * bok}")
    elif polecenie == 'prostokat':
        dlugosc = int(input('Podaj dlugosc prostokąta: '))
        szerokosc = int(input('Podaj szerokosc prostokąta: '))
        print(f"Powierzchnia prostokąta o bokach {dlugosc} i {szerokosc} to {dlugosc * szerokosc}")