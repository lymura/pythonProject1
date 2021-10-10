n_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [n_list[i] for i in range(1, len(n_list)) if n_list[i] > n_list[i - 1]]
print(result)