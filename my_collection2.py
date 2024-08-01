from collections import Counter

sentence = 'the war which influance my life'
words = sentence.split()
word_count = Counter(words)

for word, count in word_count.items():
    print(f'{word}: {count}')