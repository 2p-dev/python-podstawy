# przyklad 1
for i in [1, 2, 7, 8, -5, 6, 4]:
    if i < 0:
        print('dane są nieprawidlowe, koniec petli')
        break
    print(i)

# przyklad 2
lista = [6, 4, 1, 9]
# lista = [] - blad dzielenia przez 0
suma = 0
for i in lista:
    print(f'ocena {i}')
    suma += i
srednia = suma / len(lista)
print('srednia', srednia)

