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

import sys

files = sys.argv

if len(files) == 1:
    print('Missing filename.')
    sys.exit(1)

filepaths = files[1: ]

for file in filepaths:
    with open(file, encoding = 'utf-8') as stream:
        content = stream.read()

    lines = len(content.split('\n'))
    words = len(content.split())
    char = len(content) - content.count('\n')
    print(lines, words, char, file)