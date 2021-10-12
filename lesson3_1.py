var_1 = int(input("Введите значение var_1: "))
var_2 = int(input("Введите значение var_2: "))
def func(var_1, var_2):
    return var_1 /var_2
if var_2 == 0:
    print("Деление невозможно")
else:
    print(func(var_1, var_2))
