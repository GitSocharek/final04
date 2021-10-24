### 🔴 Ćwiczenie M04L04

# Rozwiń program z poprzedniej lekcji tak, aby mógł przyjmować wiele nazw plików. Dla każdego pliku wyświetl ile ma linii, słów i znaków.

import sys

EXT = '.txt'

files = sys.argv

# print(files)

if len(files) == 1:
    print('Missing filename.')
    sys.exit(1)

filepaths = files[1: ]

# print(filepaths)
for file in filepaths:
    with open(file, encoding = 'utf-8') as stream:
        content = stream.read()

    lines = len(content.split('\n'))
    words = len(content.split())
    char = len(content) - content.count('\n')
    print(lines, words, char, file)
# print() 