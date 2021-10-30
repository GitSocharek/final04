### 🔴 Ćwiczenie M03L19
import glob

POS_FILES = [r'D:\Dokumenty\Python\M03\data\aclImdb\train\pos\61_10.txt']#, r'D:\Dokumenty\Python\M03\data\aclImdb\train\pos\31_8.txt']
PUNCTUATIONS = "'.,?!\'"

# print(split_lines)
pos_reviews = []
for file in POS_FILES:
    with open(file, encoding = 'utf-8') as stream:
        content = stream.read()
        for punc in PUNCTUATIONS:
            word = content.replace(punc, '').replace('<br />','')
            word = word.lower().split()
        pos_reviews.append(word)

print(pos_reviews)

# input_txt = input('Jakich słów szukasz? ')
# split_txt = input_txt.lower().split()

# comments_with_input_words = []
# for word in split_txt:
#     for list_ in comments_from_file:
#         if word in list_ and list_ not in comments_with_input_words:
#             comments_with_input_words.append(list_)

# number_of_comments_with_input_words = len(comments_with_input_words)
# number_of_comments = len(comments_from_file)

# print(
#     f'W {number_of_comments_with_input_words} na {number_of_comments} komentarze występuje jedno ze słów: ' + input_txt.replace(' ',',')
# )

