#задание 2
name = input("Имя: ")
surname = input('Фамилия: ')
data = input('год рождения: ')
city = input('город проживания: ')
email = input('email: ')
tel = input('телефон: ')
def second_func(var_1, var_2, var_3, var_4, var_5, var_6):
    print(f"Имя - {var_1}; Фамилия - {var_2}; год рождения - {var_3}; город проживания - {var_4}; email- {var_5}; телефон - {var_6}")



second_func(var_1=name, var_2=surname, var_3=data, var_4=city,var_5=email, var_6=tel)
