### 🔴 Ćwiczenie M04L02

# Napisz program, który otwiera wskazany przez użytkownika plik (wskazany jako argument linii poleceń, a nie przez input()) i zlicza ile jest w nim znaków, słów i linii.

# import sys

# file = sys.argv
# filepath = file[1]

# with open(filepath, encoding = 'utf-8') as stream:
#     content = stream.read()

# lines = len(content.split('\n'))
# words = len(content.split())
# char = len(content) - content.count('\n')

# print() 
# print(lines, words, char, filepath)

### 🔴 Ćwiczenie M04L03

# Rozwiń program z poprzedniej lekcji tak, aby wyświetlał komunikat błędu, gdy użytkownik nie poda nazwy pliku. Wyświetl błąd także wtedy, gdy poda więcej niż jeden plik.

# import sys

# EXT = '.txt'

# files = sys.argv

# file_counter = 0
# for item in files:
#     if item.endswith(EXT):
#         file_counter += 1

# if file_counter == 0:
#     print('Missing filename.')
#     sys.exit(1)
# elif file_counter > 1:
#     print('You can pass only one filename!')
#     sys.exit(2)

# filepath = files[1]

# with open(filepath, encoding = 'utf-8') as stream:
#     content = stream.read()

# lines = len(content.split('\n'))
# words = len(content.split())
# char = len(content) - content.count('\n')

# print() 
# print(lines, words, char, filepath)

### 🔴 Ćwiczenie M04L04

# Rozwiń program z poprzedniej lekcji tak, aby mógł przyjmować wiele nazw plików. Dla każdego pliku wyświetl ile ma linii, słów i znaków.

# import sys

# files = sys.argv

# if len(files) == 1:
#     print('Missing filename.')
#     sys.exit(1)

# filepaths = files[1: ]

# for file in filepaths:
#     with open(file, encoding = 'utf-8') as stream:
#         content = stream.read()

#     lines = len(content.split('\n'))
#     words = len(content.split())
#     char = len(content) - content.count('\n')
#     print(lines, words, char, file)

### 🔴 Ćwiczenie M04L05

# Rozwiń program z poprzedniej lekcji tak, aby wyniki wyświetlić w tabeli. Użyj string interpolation. Dodaj nagłówek tabeli.

# import sys

# files = sys.argv
# LINES = 'LINES'
# WORDS = 'WORDS'
# CHARS = 'CHARS'
# FILENAME = 'FILENAME'

# if len(files) == 1:
#     print('Missing filename(s).')
#     sys.exit(1)

# filepaths = files[1: ]

# print(f"{LINES:6} {WORDS:6} {CHARS:6} {FILENAME}")

# for file in filepaths:
#     with open(file, encoding = 'utf-8') as stream:
#         content = stream.read()

#     lines = len(content.split('\n'))
#     words = len(content.split())
#     char = len(content) - content.count('\n')
#     print(f"{lines:5} {words:6} {char:6}  {file}")

### 🔴 Ćwiczenie M04L06

# Narodowy Bank Polski udostępnia przez swoje API historyczne kursy walut. Otrzymałæś odpowiedź taką jak poniżej

# response = {
#     "table": "A",
#     "currency": "dolar amerykański",
#     "code": "USD",
#     "rates": [
#         {
#             "no": "148/A/NBP/2021",
#             "effectiveDate": "2021-08-03",
#             "mid": 3.8315,
#         },
#     ],
# }

# rate = response['rates']
# mid_currency = rate[0]
# mid = mid_currency['mid']

# print(mid)

# Jest to kurs waluty USD z dnia 3 sierpnia 2021. Z tak zagnieżdżonej struktury wyciągnij kurs waluty (klucz "mid").

### 🔴 Ćwiczenie M04L07

# 1. Mając podany tekst zlicz poszczególne słowa.
# 2. Wyświetl w tabeli ile razy występuje każde ze słów.
# 3. Nie zwracaj uwagi na wielkość liter w słowach, to znaczy "A" oraz "a" to jest to samo słowo. 
# 4. W jaki jeszcze sposób przetworzył(a)byś tekst zanim podzielisz go na słowa?

PUNCTUATIONS = '.,?!'

txt = 'Słowa. Jak policzyć słowa w słowniku. No jak, jak?'
words = txt.split()

print(words)
split_words = []
for word in words:
    for punc in PUNCTUATIONS:
        word = word.replace(punc, '').lower()
    split_words.append(word)

print(split_words)  
stats = {}
for i in split_words:
    if i in stats:
        stats[i] += 1
    else:
        stats[i] = 1

for i in sorted(stats, key=stats.get):
    print("%d×'%s'" % (stats[i], i))