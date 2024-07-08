def total_salary(path):
    tot_salary = 0
    count = len(path)

    for employee in path:
        tot_salary += employee['salary']

    if count > 0:
        avg_salary = tot_salary / count
    else:
        avg_salary = 0

    return (tot_salary, avg_salary)

path = [
    {'name': 'Alex Korp', 'salary': 3000},
    {'name': 'Nikita Borisenko', 'salary': 2000},
    {'name': 'Sitarama Raju', 'salary': 1000}
]

try:
    total, average = total_salary(path)

    # Відкриття файлу для додавання результатів
    with open('salary.txt', 'a') as fh:
        fh.write(f'Total salary employees: {total}\n')
        fh.write(f'Average salary employees: {average}\n')

    print(f'Total salary employees: {total}')
    print(f'Average salary employees: {average}')

except FileNotFoundError:
    print("Error: The file 'salary.txt' was not found.")







