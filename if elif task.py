def route_info(some_dict):
    if 'distance' in some_dict:
        print(f"Distance to your destination is {some_dict['distance']}")
    elif 'speed' in some_dict and 'time' in some_dict:
        print(f"Distance to your destination is {some_dict['speed'] * some_dict['time']}")
    else:
        print('No distance info is available')

# Пример использования:

# Словарь с информацией о расстоянии
route_info({
    'distance': 123123,
    'speed': 12312,
    'time': 123
})

# Словарь без информации о расстоянии, но с информацией о скорости и времени
route_info({
    'speed': 50,
    'time': 2
})

# Словарь без необходимой информации
route_info({
    'location': 'somewhere'
})

