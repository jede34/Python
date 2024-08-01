while True:  # Начинаем бесконечный цикл
    num = float(input('Guess the first random number: '))
    num2 = float(input('Guess the second random number: '))
    
    # Проверка деления на ноль
    if num2 == 0:
        print("Error: division by zero")
    else:
        print(num / num2)
    
    user_response = input("Do you want to continue? (yes/no): ").lower()  # Запрашиваем ответ пользователя
    
    if user_response == 'no':  # Если пользователь отвечает 'no', то выходим из цикла
        break
    elif user_response != 'yes':  # Если пользователь вводит что-то отличное от 'yes' или 'no'
        print("Invalid input. Exiting...")
        break  # Можно здесь также использовать continue, чтобы снова задать вопрос
    
# Код после цикла может продолжаться, если это необходимо
print("Program finished.")
