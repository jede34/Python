def merge_lists_to_dict(girl_names, boy_names):
    zipped_seq = zip(girl_names, boy_names)
    return dict(zipped_seq)

res_one = merge_lists_to_dict(['Sasha', 'Vanya', 'Renat'], ['Roma', 'Max', 'Bogdan'])
print(res_one)

res_two = merge_lists_to_dict(['vova'], ['Pidr', 'werw'])
print(res_two)

res_three = merge_lists_to_dict(['Pidr', 'werw'], ['vova'])
print(res_three)