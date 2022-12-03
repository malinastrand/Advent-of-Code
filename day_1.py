from read_input import *

input_list = read_input('input_1.in')

temp_sum = 0
sum_list = []
for entry in input_list:
    if entry == '':
        sum_list.append(temp_sum)
        temp_sum = 0
    else:
        temp_sum += int(entry)

sum_list.sort(reverse=True)

print(sum_list[0], sum(sum_list[:3]))