import collections

Device = collections.namedtuple('Device', ['device_brand', 'device_cost', 'device_color'])

device = Device('HyperX', 1500, 'black')

print(f'This is the most popular heardphones: {device.device_brand}. Their cost: {device.device_cost}. The most popular color wich users used: {device.device_color}.')