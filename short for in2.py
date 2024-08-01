my_scores = {
    'a': 10, 
    'b': 7,
    'c': 14
}

scores = {}

for k, v in my_scores.items():
    scores[k] = v * 10

print(scores)

print(my_scores)

# Сокращенный цикл for in 

scores_one = {
    'a': 10, 
    'b': 7,
    'c': 14
}

scores_two = {k: v * 10 for k, v in scores_one.items()}

print(scores_one)

print(scores_two)