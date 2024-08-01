try:
    print('10' / 0)
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else: 
    print('There was no error')
finally:
    print('Continue...')