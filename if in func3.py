def nums_info(a, b): 
    if (type(a) is not int) or (type(b) is not int):
        info = 'One of this arg not integer'
    elif a >= b:
        info = f'{a} >= {b}'
    else: 
        info = f'{a} < {b}'
    return info 

print(nums_info(True, 10))

print(nums_info(10, 2))
print(nums_info(4, 15))