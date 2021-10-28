### 🔴 Ćwiczenie M04L07

# 1. Mając podany tekst zlicz poszczególne słowa.
# 2. Wyświetl w tabeli ile razy występuje każde ze słów.
# 3. Nie zwracaj uwagi na wielkość liter w słowach, to znaczy "A" oraz "a" to jest to samo słowo. 
# 4. W jaki jeszcze sposób przetworzył(a)byś tekst zanim podzielisz go na słowa?

import sys

txt = sys.argv
PUNCTUATIONS = '.,?!'

print(txt)
# words = txt.split()
for word in txt[1: ]:
    split_txt = word.split()
print(split_txt)

# print(words)
split_words = []
for word in split_txt:
    for punc in PUNCTUATIONS:
        word = word.replace(punc, '').lower()
    split_words.append(word)

# print(split_words)  
stats = {}
for i in split_words:
    if i in stats:
        stats[i] += 1
    else:
        stats[i] = 1

# print(stats)

for i in stats:
    # print(f"{stats.get(i, 0), i:3}")
    print(stats.get(i, 0), i)


# print(f"{lines:5} {words:6} {char:6}  {file}")

