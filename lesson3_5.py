#

def sum_nums(nums_str, stop):
    nums_list = nums_str.split(' ')
    sum_list = 0
    for i in nums_list:
        if i == stop:
            break
        sum_list += int(i)
    return sum(nums_str)

stopper = '*'
finished = False
s = 0
while not finished:
   my_list = input("Введите набор чисел через пробел: ")
   s += sum_nums(my_list, stopper)
   finished = stopper in my_list
   print(f"Cумма = {s}")