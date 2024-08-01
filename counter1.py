from collections import Counter

letter_count = Counter('Sasha')
print(letter_count)


sentence = 'my girlfriend is the biggest toxic girl in the world'
words = sentence.split()
word_count = Counter(words)

for word, count in word_count.items():
    print(f'{word}: {count}')