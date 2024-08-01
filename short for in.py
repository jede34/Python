all_nums = [-3, 1, 0, 10, -20, 5]

absolute_nums = []

for num in all_nums:
    absolute_nums.append(abs(num))


print(absolute_nums)

print(all_nums)









my_set = {1, 10, 15}

new_set = set()

for val in my_set:
    new_set.add(val * val)

print(new_set)

print(my_set)

# Решения способом list comprehension

set_one = {1, 10, 15}

set_two = {val + val for val in set_one}

print(set_one)

print(set_two)