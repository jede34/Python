# Добавление в набор других элементов
photo_sizes = {'1920x1080', '800x600'}
photo_sizes.add('1024x768')

print(photo_sizes)

photo_sizes = {'1920x1080', '800x600'}
other_sizes = {'800x600', '1024x768'}
# Все уникальные элементы двух наборов
all_sizes = photo_sizes.union(other_sizes)

print(all_sizes)

# Пересечение двух наборов

photo_s = {'1920x1080', '800x600'}
other_s = {'800x600', '1024x768'}

common_s = photo_s.intersection(other_s)

print(common_s)

# Один набор включён в другой

nums = {10, 5, 35}
other_nums = {20, 5, 12, 10, 35}

res = nums.issubset(other_nums)

print(res)