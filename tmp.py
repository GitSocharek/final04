### 🔴 Ćwiczenie M04L07

# 1. Mając podany tekst zlicz poszczególne słowa.
# 2. Wyświetl w tabeli ile razy występuje każde ze słów.
# 3. Nie zwracaj uwagi na wielkość liter w słowach, to znaczy "A" oraz "a" to jest to samo słowo. 
# 4. W jaki jeszcze sposób przetworzył(a)byś tekst zanim podzielisz go na słowa?

import sys
text = sys.argv

PUNCTUATIONS = '.,?!'
# print(text) # tmp

for txt in text[1: ]:
    for punc in PUNCTUATIONS:
        txt = txt.replace(punc, '').lower()
    words = txt.split()
# print(words) # tmp

dict = {}
for word in words:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1
# print(dict) # tmp

for key_ in dict:
    print(f"{dict.get(key_, 0):3}", key_)
