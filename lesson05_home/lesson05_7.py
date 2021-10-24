import json

firms = {}
prof_count, prof_sum = 0, 0
with open('task7.txt') as file:
    file_lines = file.readlines()
    for line in file_lines:
        data = line.split()
        profit = float(data[1]) - float(data[2])
        firms.update({data[0]: profit})
        if profit > 0:
            prof_count += 1
            prof_sum += profit

average_profit = prof_sum / prof_count
result = [firms, {'average_profit': average_profit}]

with open("result.json", 'w') as file:
    json.dump(result, file)
print(result)