Nums = {
'One': 'Один',
'Two': 'Два',
'Three': 'Три',
'Four': 'Четыре'}
with open('task1.txt', 'r') as file, open("new_file.txt", 'w') as new_file:
    file_lines = file.readlines()
    for line in file_lines:
        data = line.split()
        rus_num = Nums.get(data)

        new_file.write({line.replace(data), rus_num})



