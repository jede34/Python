Istore_device = ['Iphone', 'Mac', 'AppleWatch', 'Ipod', 'Ipad']
price_device = [1200, 2000, 300, 200, 1250]

apple_device = zip(Istore_device, price_device)

apple_device = list(apple_device)

print(apple_device)

apple_device = dict(apple_device)

print(apple_device)
