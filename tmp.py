### 🔴 Ćwiczenie M03L19

import glob

PUNCTUATIONS = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

POS_FILES = [r'M03\data\aclImdb\train\pos\3_10.txt', r'M03\data\aclImdb\train\pos\31_8.txt']
pos_reviews = []
for file in POS_FILES:
    with open(file, encoding = 'utf-8') as stream:
        content = stream.read()
        # print(content)
        content = content.replace('<br />',' ')
        for char in file:
            if char in PUNCTUATIONS:
                word = content.replace(char, '')
                word = word.lower().split()
        pos_reviews.append(word)
print(pos_reviews)

NEG_FILES = [r'M03\data\aclImdb\train\neg\1_1.txt', r'M03\data\aclImdb\train\neg\4_4.txt']
neg_reviews = []
for file in NEG_FILES:
    with open(file, encoding = 'utf-8') as stream:
        content = stream.read()
        # print(content)
        content = content.replace('<br />',' ')
        for char in file:
            if char in PUNCTUATIONS:
                word = content.replace(char, '')
                word = word.lower().split()
        neg_reviews.append(word)
print(neg_reviews)

split_comment = []
input_comment = input('Enter comment: ')
comment = input_comment.lower().replace(PUNCTUATIONS, '').split()
split_comment.append(comment)
print(split_comment)
