n_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [a for a in n_list if n_list.count(a) == 1]
print(result)