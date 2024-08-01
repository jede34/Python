from copy import deepcopy

info = {
    'name': 'Bogdan',
    'is_instructor': True,
    'reviews': []
}

info_shallow_copy = info.copy()

info_shallow_copy['reviews'].append('Great course!')
info_shallow_copy['reviews'].append('Super')

info['new_key'] = 10

print(info)

print(info_shallow_copy)