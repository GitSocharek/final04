### 🔴 Ćwiczenie M04L05

# Rozwiń program z poprzedniej lekcji tak, aby wyniki wyświetlić w tabeli. Użyj string interpolation. Dodaj nagłówek tabeli.

import sys

files = sys.argv
LINES = 'LINES'
WORDS = 'WORDS'
CHARS = 'CHARS'
FILENAME = 'FILENAME'
# print(files)

if len(files) == 1:
    print('Missing filename(s).')
    sys.exit(1)

filepaths = files[1: ]

print(f"{LINES:6} {WORDS:6} {CHARS:7}|  {FILENAME}")
print('-' * 32)
# print(filepaths)
for file in filepaths:
    with open(file, encoding = 'utf-8') as stream:
        content = stream.read()

    lines = len(content.split('\n'))
    words = len(content.split())
    char = len(content) - content.count('\n')
    print(f"{lines:5} {words:6} {char:6}  |  {file}")
