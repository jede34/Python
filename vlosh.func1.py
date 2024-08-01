g = 'gray'
def colors(param= 'r'):
    y = 'yellow'
    g = 'green'
    def print_red():
        r = 'red'
        print(r)

    def print_blue():
        b = 'blue'
        print(b)
    if param  == 'r':
        print_red()
    elif param == 'b':
        print_blue()
    else:
        print('idc this color')

colors(23)