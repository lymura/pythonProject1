# Задание 4
number = int(input("Введите целое положительное число: "))
print(number)
max_number = 0
while number > 0:
    if number % 10 > max_number:
        max_number = number % 10
        if max_number == 9:
            break
    number = number // 10
print(f"Наибольшая цифра числа равна: {max_number}")




