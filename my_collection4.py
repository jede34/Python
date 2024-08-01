from collections import defaultdict

words = ['Sasha', 'kent', 'slaim', 'klishe', 'Max', 'Marsh', 'Zolushka']

grouped_words = defaultdict(list)

for word in words:
    char = word[0]
    if char not in grouped_words:
        grouped_words[char] = []
    grouped_words[char].append(word)

print(dict(grouped_words))