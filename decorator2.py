def add_bait(func):
    def wrapper(catch_fish):
        print(f'Put a worm on a hook to catch {catch_fish}')
        func(catch_fish)
    return wrapper


def add_special_attention(func):
    def wrapper(catch_fish):
        print(f'Pay special attention to the float, {catch_fish} is baiting!')
        func(catch_fish)
    return wrapper

@add_bait
@add_special_attention

def catch_fishing(fish):
    print(f'{fish} cought.')

catch_fishing('karas')