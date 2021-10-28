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


# text = 'ile razy pojawia się słowo ile w tym tekście'
# words = text.split()

# counter = {}
# for word in words:
#     counter[word] = 1
#     # counter.get(word, 0)
# print("Słowo 'ile' pojawia się", counter, 'razy')

# print(counter.get('ile', 0))  # ==> 2  # zwraca wartość dla klucza 'ile'
# print(counter.get('nie-istnieje', 0))  # ==> 0  # zwraca wartość domyślną - to, co jest przekazane jako drugi argument


# counter = 0
# for word in words:
#     if word == 'ile':
#         counter += 1
# print("Słowo 'ile' pojawia się", counter, 'razy')

# list = ['a', 'b', 'c']
# dictionary = {}
# counter = 0
# for i in list:
#    dictionary[i] = counter
#    counter += 1

# print(dictionary) # dictionary = {'a':0, 'b':1, 'c':2}

