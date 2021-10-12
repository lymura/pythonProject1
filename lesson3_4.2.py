def get_pow(x, y):
  if x < 0:
    return 'х должен быть больше 0'
  if y > 0:
    return 'y должен быть меньше 0'
  z = 1
  for i in range(y * -1):
    z *= x
  return 1 / z
x = float(input('Введите действительное число: '))
y = int(input("Введите отрицательное целое число: "))
print(get_pow(x, y))