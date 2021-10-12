#задание 6

#txt = txt.capitalize()
def int_func(str):
  return str.capitalize()
txt = input("Введите строку латинскими буквами: ")
for txt in txt.split(' '):
  print(int_func(txt), end = ' ')