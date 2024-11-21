with open('dane.csv', 'r') as infile:  # plik zostanie automatycznie zamknięty po zakończeniu ‘with’
    for line in infile:
        print(line)

print(30 * "=")

with open('dane.csv', 'r', encoding="utf-8") as infile: # wczytanie pliku z kodowaniem utf-8
    for line in infile:
        columns = line.split(";")
        for column in columns:
            print(column)
