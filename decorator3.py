# Глобальная переменная для имени
global_name = 'Sasha'

def add_recommedations(func):
    def wrapper(*args, **kwargs):
        print(f'I want {global_name} to quit from DTEK as soon as possible')
        return func(*args, **kwargs)
    return wrapper

def add_recommendations2(func):
    def wrapper(*args, **kwargs):
        print(f'I want {global_name} to arrive in Derenkovetz as soon as possible')
        return func(*args, **kwargs)
    return wrapper

def add_my_comments(func):
    def wrapper(*args, **kwargs):
        print(f'I miss you, {global_name}')
        return func(*args, **kwargs)
    return wrapper

@add_recommedations
@add_recommendations2
@add_my_comments
def love_story(name):
    print(f'I love {name}')

# Вызов функции
love_story(global_name)
