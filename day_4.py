from read_input import *

input_list = read_input('input_4.in')

counter = 0
counter_2 = 0

for i, entry in enumerate(input_list):
    numbers = entry.split(',')
    left = numbers[0].split('-')
    right = numbers[1].split('-')
    if (int(left[0]) <= int(right[0]) and int(left[1]) >= int(right[1])) or (int(right[0]) <= int(left[0]) and int(right[1]) >= int(left[1])):
        counter += 1
    if (int(left[0]) <= int(right[0]) and int(left[1]) >= int(right[0])) or (int(right[0]) <= int(left[0]) and int(right[1]) >= int(left[0])):
        counter_2 += 1

print(counter, counter_2)