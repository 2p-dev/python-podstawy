"""
poprosic uzytkownika o podawanie liczb
tekst q ma zakonczyc wprowadzqnie liczb
tekst p ma wypisac bieżącą zawartość listy
po zakończeniu wprowadzania program ma:
- wypisać listę
- obliczyć i wypisac średnią
dodać warunki zabezpieczające, np przed dzieleniem przez 0
"""

wartosc = ''
lst = []
while wartosc != 'q':
    wartosc = input('podaj liczbę, q = quit, p = print: ')
    if wartosc == 'p':
        print(lst)
    elif wartosc != 'q':
        wartosc_int = int(wartosc)
        #lst += wartosc_int
        lst.append(wartosc_int)

print(lst)
if len(lst) == 0:
    print('nie mozna policzyc sredniej')
else:
    srednia = sum(lst) / len(lst)
    print(f'srednia: {srednia}')
