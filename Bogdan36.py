def get_married(name_one, name_two):
    married_persons = f'{name_one}, do you agree to join the knot of marriage with {name_two}?'
    
    answer = input(married_persons + ' ')
    
    if answer.lower() == 'yes':
        print(f'{name_one}, I love you!')
    elif answer.lower() == 'no':
        print(f'{name_one}, have a good luck with another boyfriend!')
    else:
        print(f'Sorry, {name_one}, I did not understand your answer.')

    return married_persons

married_question = get_married('Alexandra', 'Ivan')
print(married_question)
