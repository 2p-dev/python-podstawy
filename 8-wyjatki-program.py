# napisać prosty kalkulator matematyczny wykonujący kilka operacaji
# program ma pobrać od użytkowanika 2 liczby oraz operację matematyczną (+ - * / % // )
# program ma obsłużyć wyjątki, które mogą występować w programie
# program ma działać non stop, do momentu aż użytkownik naciśnie Ctrl+C (ładny komunikat)

class TooBigError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

try:
    while True:
        print('Kalkulator')
        try:
            a = int(input("Podaj pierwszą liczbę, musi być < 10: "))
            if a >= 10:
                raise TooBigError('wartość jest większa lub równa 0')
            b = int(input("Podaj drugą liczbę: "))
            op = input('Podaj operację matematyczną: ')
            if op == '+':
                wynik = a + b
            elif op == '-':
                wynik = a - b
            elif op == '*':
                wynik = a * b
            elif op == '/':
                wynik = a / b
            elif op == '%':
                wynik = a % b
            elif op == '//':
                wynik = a // b
            print('wynik', wynik)
        except TooBigError as tbe:
            print('Błąd podanej wartości (TooBigError):', tbe)
        except ValueError as ve:
            print('Błąd podanej wartości (ValueError):', ve)
        except ZeroDivisionError:
            print('Błąd dzielenia przez 0')
except KeyboardInterrupt:
    print('Dziękuję za skorzystanie z kalkulatora')


