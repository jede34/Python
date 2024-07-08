def get_cats_info(path):
    cats_info = []
    try:
        with open('cats.txt', 'r') as fh:
            for line in fh:
                line = line.strip()
                if line:  # проверяем, что строка не пустая
                    parts = line.split(',')
                    cat_info = {
                        "id": parts[0],
                        "name": parts[1],
                        "age": parts[2]
                    }
                    cats_info.append(cat_info)
    except FileNotFoundError:
        print(f"File '{path}' not found.")
    
    return cats_info

cats_info = get_cats_info('path/to/cats.txt')
print(cats_info)
