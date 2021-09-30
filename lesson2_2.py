#задание 2
#
my_list = input('list: ')
input_list = my_list.split()
len_list = len(input_list)
i = 0
if len_list > 1:
    while i < len_list - 1:

        tmp = input_list[i]
        input_list[i] = input_list[i+1]
        input_list[i+1] = tmp
        i += 2

print(input_list)
