with open("python.txt") as file:
    file_str = file.readlines()
    str_count = 0
    for n, line in enumerate(file_str):
        w_count = len(line.split())
        str_count += 1
        print(f'#{n + 1} - {w_count} слов')
        print(f'{str_count} cтрок')
