# Написати генератор квадратів чисел.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def get_num_squares(numbers):
    return [
        num ** 2
        for num in numbers:
    ]


def generate_num_squares(numbers):
    for num in numbers:
        yield num ** 2


gen = generate_num_squares(nums)
print(get_num_squares(nums))
print(next(gen))
print(next(gen))



