my_phone = {
    'price': 200
}

if my_phone.get('brand'):
    print('Phones brand is', my_phone['brand'])
else:
    print('There is no phone brand')