# задание 6
n = 0
print(n)
a = int(input("Введите результат первого дня: "))
b = int(input("Введите общий результат: "))
print(a)
print(b)

c = a + 0.1 * (n - 1) * a
while c < b:
  n += 1
  c += 1
  str1 = f"{n}-й день = {c}км"
  print(str1)
  continue
if c == b:
  str2 = f"{n}-й день = {b} км"
  print(str2)

str3 = f"На {n} -й день спортсен достиг результата не менее {b}км"
print(str3)
