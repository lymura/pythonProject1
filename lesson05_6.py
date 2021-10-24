result = {}
with open('task6.txt') as file:
    file_lines = file.readlines()
    for line in file_lines:
        data = line.split()

        h = 0
        for elem in data[1:]:
            if elem != '-':
                num = '0'

                for i in elem:
                    if i.isdigit():
                      num += i
                    else:
                      break
                h += int(num)
        result.update({data[0].strip(':'): h})
print(result)
