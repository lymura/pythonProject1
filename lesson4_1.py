import sys

if len(sys.argv) < 4:
    print(f'Введите (выработка в часах, ставка в часах, премия):')
else:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    result = a * b * c
    print(result)