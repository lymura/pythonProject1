for line in file
    stuff_info = line.split()
    stuff.update({stuff_info[0]: float(stuff_info[1])})
    wage += float(stuff_info[1])
average_wage = wage / len(stuff)
print(f'Средняя з/п = {average_wage}')

for n, k in stuff.items():
    if k < 20000:
        print(f'{n}: {k}')