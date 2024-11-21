# Listy składane / wyrażenia listowe (list comprehension)

# nowa_lista = [transformacja(x) for x in stara_lista]

# # Jest równoznaczne z:

# nowa_lista = []
# for x in stara_lista:
#     nowa_lista.append(transformacja(x))


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
    if i > 2:
        liczby.append(x + 1)

