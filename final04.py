### 馃敶 膯wiczenie M04L02

# Napisz program, kt贸ry otwiera wskazany przez u偶ytkownika plik (wskazany jako argument linii polece艅, a nie przez input()) i zlicza ile jest w nim znak贸w, s艂贸w i linii.

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

### 馃敶 膯wiczenie M04L03

# Rozwi艅 program z poprzedniej lekcji tak, aby wy艣wietla艂 komunikat b艂臋du, gdy u偶ytkownik nie poda nazwy pliku. Wy艣wietl b艂膮d tak偶e wtedy, gdy poda wi臋cej ni偶 jeden plik.

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

### 馃敶 膯wiczenie M04L04

# Rozwi艅 program z poprzedniej lekcji tak, aby m贸g艂 przyjmowa膰 wiele nazw plik贸w. Dla ka偶dego pliku wy艣wietl ile ma linii, s艂贸w i znak贸w.

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

### 馃敶 膯wiczenie M04L05

# Rozwi艅 program z poprzedniej lekcji tak, aby wyniki wy艣wietli膰 w tabeli. U偶yj string interpolation. Dodaj nag艂贸wek tabeli.

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

### 馃敶 膯wiczenie M04L06

# Narodowy Bank Polski udost臋pnia przez swoje API historyczne kursy walut. Otrzyma艂忙艣 odpowied藕 tak膮 jak poni偶ej

# response = {
#     "table": "A",
#     "currency": "dolar ameryka艅ski",
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

# Jest to kurs waluty USD z dnia 3 sierpnia 2021. Z tak zagnie偶d偶onej struktury wyci膮gnij kurs waluty (klucz "mid").

### 馃敶 膯wiczenie M04L07

# 1. Maj膮c podany tekst zlicz poszczeg贸lne s艂owa.
# 2. Wy艣wietl w tabeli ile razy wyst臋puje ka偶de ze s艂贸w.
# 3. Nie zwracaj uwagi na wielko艣膰 liter w s艂owach, to znaczy "A" oraz "a" to jest to samo s艂owo. 
# 4. W jaki jeszcze spos贸b przetworzy艂(a)by艣 tekst zanim podzielisz go na s艂owa?

PUNCTUATIONS = '.,?!'

txt = 'S艂owa. Jak policzy膰 s艂owa w s艂owniku. Jak, jak?'
words = txt.split()

# print(words)
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

for i in stats:
    print(stats.get(i, 0), i)