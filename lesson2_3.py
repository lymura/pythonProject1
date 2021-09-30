#задание 2

number_month = int(input("Введите номер месяца: "))
a, b, c, d = 'весна', 'лето', 'осень', 'зима'
month_dict = {'3': a, '4': a, '5': a, '6': b, '7': b, '8': b, '9': c, '10': c, '11': c, '12': d, '1': d, '2': d}
season_list = [a, a, a, b, b, b, c, c, c, d, d, d]
print(season_list[(number_month) - 1])


