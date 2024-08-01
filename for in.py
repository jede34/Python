# Для списков
my_list = [True, 10, 'abc', {}]

for elem in my_list:        

    print(elem)


# Для кортежей
video_info = ('1920x1080', True, 27)

for elem in video_info:
    print(video_info)

# Для словарей
My_object = {
    'x': 10,
    'y': True,
    'z': 'abc'
}
for key in My_object:
    print(key, My_object[key])