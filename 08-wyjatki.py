try:
    liczba = int(input('Podaj liczbę: '))
except:
    print('To nie liczba')


'''
>>> int('tekst')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'tekst'
'''

try:
    liczba = int(input('Podaj liczbę: '))
except ValueError:
    print('To nie liczba')



import time

try:
    plik = open('wiersz.txt')
    while True:
        linia = plik.readline()
        if len(linia) == 0:
            break
        print(linia),
        time.sleep(2) # zatrzymanie programu na 2 sekundy
except KeyboardInterrupt:
    print('Czytanie wiersza zostało przerwane!')
finally:
    plik.close()
    print('Sprzątanie zakończone, plik został zamknięty')