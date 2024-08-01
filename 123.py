def add(num_1, num_2):
    return num_1 + num_2



add_lambda = lambda num_1, num_2: num_1 + num_2


for item in map(lambda num: num **2, [1, 2, 5]):
    print(item)


# map(float)