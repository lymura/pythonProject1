# задание 5
a = int(input("Введите Выручка:"))
b = int(input("Введите Затраты: "))
if b > a:
   print("Предприятие в убытке")
elif a > b:
  print("Предприятие работает с прибылью")
  c = round((a - b) / b, 2)
  print(f"Рентабельность предприятия = {c}")
  n = int(input("Ведите численность сотрудников: n = "))
  p = (a - b) / n
  str = f"Прибыль в расчете на одного сотрудника = {p}"
  print(str)
elif a == b:
  print("Предприятие работает в 0")
