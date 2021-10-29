### 🔴 Ćwiczenie M04L07

# 1. Mając podany tekst zlicz poszczególne słowa.
# 2. Wyświetl w tabeli ile razy występuje każde ze słów.
# 3. Nie zwracaj uwagi na wielkość liter w słowach, to znaczy "A" oraz "a" to jest to samo słowo. 
# 4. W jaki jeszcze sposób przetworzył(a)byś tekst zanim podzielisz go na słowa?

import sys

text = sys.argv
PUNCTUATIONS = '.,?!'

print(text) # tmp

for txt in text[1: ]:
    for punc in PUNCTUATIONS:
        txt = txt.replace(punc, '').lower()
    split_text = txt.split()
print(split_text) # tmp
  
dict = {}
for word in split_text:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1

print(dict) # tmp

for key in dict:
    # print(f"{dict.get(i, 0), i:3}")
    print(f"{dict.get(key, 0):3}", key)
