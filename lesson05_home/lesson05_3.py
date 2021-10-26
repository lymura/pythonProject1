with open('task_5.txt') as file:
    file_lines = file.readlines()
    stuff = {}
    sum_wage = 0
    for line in file_lines:
        stuff_info = line.split()
        stuff.update({stuff_info[0]: float(stuff_info[1])})
        sum_wage += float(stuff_info[1])
average_wage = sum_wage / len(stuff)
print(f'Средняя з/п = {average_wage}')

for n, k in stuff.items():
    if k < 20000:
        print(f'{n}: {k}')