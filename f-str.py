my_name = 'Ivan'
my_hobby = 'cycling'
my_girlfriend = 'Sasha'
my_mother_in_law = 'Irina Anatolievna'
my_father_in_law = 'Fedya'
time = 8

info = f'{my_name} likes {my_hobby} at {str(time)} o\'clock '
info_two = f'{my_name} get married with {my_girlfriend}, and {my_mother_in_law}, {my_father_in_law} became relatives!'
print(info_two)
# Capitalize each word and split into a list
words = [word.capitalize() for word in info.split()]

print(words)
