from functools import reduce
n_list = [x for x in range(100, 1001)if x % 2 == 0]
print(reduce(lambda a, b: a * b, n_list))
