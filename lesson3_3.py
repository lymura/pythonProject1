#задание 3
var_1 = int(input("введите число: "))
var_2 = int(input("введите число: "))
var_3 = int(input("введите число: "))

def my_func(var_1, var_2, var_3):
   return (var_1 + var_2 + var_3) - min(var_1, var_2, var_3)
print(my_func(var_1, var_2, var_3))

