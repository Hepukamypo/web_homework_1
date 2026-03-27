import re

with open('example.txt', 'r', encoding='utf-8') as file:
    text = file.read()

words = re.findall(r'\b[а-яА-ЯёЁa-zA-Z]+\b', text)

max_len = max(len(word) for word in words)

for word in words:
    if len(word) == max_len:
        print(word)